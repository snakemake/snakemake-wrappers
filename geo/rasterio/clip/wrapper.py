"""rasterio clip wrapper.

Clip local or remote rasters with ease!
"""

__author__ = "Ivan Ruiz Manuel"
__copyright__ = "Copyright 2025, Ivan Ruiz Manuel"
__email__ = "i.ruizmanuel@tudelft.nl"
__license__ = "MIT"


import geopandas as gpd
import rasterio

from rasterio.warp import transform_bounds
from snakemake.shell import shell

log = snakemake.log_fmt_shell(stdout=True, stderr=True)

# A sane --co / --profile configuration
PROFILE_DEFAULTS = {
    "COMPRESS": "ZSTD",
    "NUM_THREADS": snakemake.threads,  # compression threads
    "TILED": "YES",
    "BLOCKXSIZE": 512,
    "BLOCKYSIZE": 512,
    "BIGTIFF": "IF_SAFER",
}


ENV_DEFAULTS = {
    # GDAL tuning
    "GDAL_NUM_THREADS": "1",
    # single-thread avoids gdal 3.10 bugs
    # see https://github.com/OSGeo/gdal/issues/11552
    # NOTE: consider removal after rasterio is compatible with gdal>=3.11
    "GDAL_HTTP_MAX_RETRY": "6",  # diminish http connection oddities
    "GDAL_HTTP_RETRY_DELAY": "10",  # 6x10s of retrying downloads
    "GDAL_HTTP_MULTIRANGE": "YES",
    "GDAL_HTTP_MULTIPLEX": "YES",
    "GDAL_HTTP_MERGE_CONSECUTIVE_RANGES": "YES",
    "GDAL_HTTP_VERSION": "2TLS",
    "CPL_VSIL_CURL_USE_HEAD": "NO",
    "CPL_VSIL_CURL_USE_S3_REDIRECT": "YES",
    "VSI_CACHE": "TRUE",
    "GDAL_DISABLE_READDIR_ON_OPEN": "EMPTY_DIR",  # do not load auxiliary files
    "GDAL_CACHEMAX": "256MB",
    # /vsicurl settings following GDAL recommendations
    # see https://gdal.org/en/release-3.10/user/virtual_file_systems.html
    "CPL_VSIL_CURL_CHUNK_SIZE": str(1024 * 1024),  # 1 MiB
    "CPL_VSIL_CURL_CACHE_SIZE": str(128 * 1024 * 1024),  # 128 times the chunk size
    # Assume S3 endpoint is open
    "AWS_NO_SIGN_REQUEST": "YES",
}


def parse_bounds(raw) -> tuple[float, ...]:
    """Ensures the given bbox is correct for both strings and lists of numbers.

    e.g.: "5,45,10,47" -> (5,45,10,47
    """
    tokens = raw
    if isinstance(tokens, str):
        tokens = tokens.replace(",", " ").split()
    tokens = tuple(map(float, tokens))
    if len(tokens) != 4:
        raise ValueError("bbox must be in the form [minx, miny, maxx, maxy]")
    return tokens


def clip_wrapper(
    output_path: str,
    input_raster: str | None,
    like_raster: str | None,
    like_vector: str | None,
    cog_url: str | None,
    bounds: str | list | None,
    bounds_crs: str | None,
    buffer: float,
    extra_options: list[str] | None,
    profile_overrides: dict | None,
    environment_overrides: dict | None,
):
    if sum(x is not None for x in (like_raster, like_vector, bounds)) != 1:
        raise ValueError(
            "Multiple clipping references given. Specify only one of "
            "input.like_raster, input.like_vector or params.bounds."
        )
    if sum(x is not None for x in (input_raster, cog_url)) != 1:
        raise ValueError(
            "Multiple target rasters given. Specify only one of "
            "input.raster or params.cog_url."
        )
    if (like_raster or like_vector) and any([bounds, bounds_crs]):
        raise ValueError("Bounds cannot be specified when clipping to files.")
    if bounds and not bounds_crs:
        raise ValueError("params.bounds and params.crs must be specified together")

    like_crs = None
    if bounds:
        l_minx, l_miny, l_maxx, l_maxy = parse_bounds(bounds)
        like_crs = bounds_crs
    elif like_vector:
        gdf = gpd.read_parquet(like_vector)
        if gdf.empty or not gdf.crs:
            raise ValueError("Failed to obtain bounds from input vector file.")
        l_minx, l_miny, l_maxx, l_maxy = gdf.total_bounds
        like_crs = gdf.crs
    else:
        with rasterio.open(like_raster) as rst:
            l_minx, l_miny, l_maxx, l_maxy = rst.bounds
            like_crs = rst.crs

    if buffer:
        buffer = float(buffer)
        if buffer < 0:
            raise ValueError(f"buffer_degrees must be non-negative, got {buffer}.")
        l_minx -= buffer
        l_miny -= buffer
        l_maxx += buffer
        l_maxy += buffer

    input_raster = cog_url or input_raster
    with rasterio.open(input_raster) as rst:
        dst_crs = rst.crs

    r_minx, r_miny, r_maxx, r_maxy = transform_bounds(
        like_crs, dst_crs, l_minx, l_miny, l_maxx, l_maxy, densify_pts=21
    )

    profile = PROFILE_DEFAULTS | profile_overrides
    co_commands = " ".join([f"--co {key}={value}" for key, value in profile.items()])

    cmd = f"""
    rio clip {input_raster} {output_path} \
        --bounds '{r_minx} {r_miny} {r_maxx} {r_maxy}' \
        {co_commands} \
        {" ".join(extra_options)}
        {log}
    """
    environment = ENV_DEFAULTS | environment_overrides
    shell(cmd, additional_envvars=environment)


clip_wrapper(
    output_path=snakemake.output.path,
    input_raster=snakemake.input.get("raster", None),
    like_raster=snakemake.input.get("like_raster", None),
    like_vector=snakemake.input.get("like_vector", None),
    cog_url=snakemake.params.get("cog_url", None),
    bounds=snakemake.params.get("bounds", None),
    bounds_crs=snakemake.params.get("bounds_crs", None),
    buffer=snakemake.params.get("buffer", 0),
    extra_options=snakemake.params.get("clip_options", []),
    profile_overrides=snakemake.params.get("profile_overrides", {}),
    environment_overrides=snakemake.params.get("environment_overrides", {}),
)

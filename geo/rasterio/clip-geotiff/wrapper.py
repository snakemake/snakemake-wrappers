"""TIFF clipper.

Clip a local GeoTIFF or a remote COG (Cloud Optimised GeoTIFF) to a vector AOI
or a simple bounding box, keeping the raster's native CRS.
"""

__author__ = "Ivan Ruiz Manuel"
__copyright__ = "Copyright 2025, Ivan Ruiz Manuel"
__email__ = "i.ruizmanuel@tudelft.nl"
__license__ = "MIT"

from ast import literal_eval

import geopandas as gpd
import rasterio
from rasterio.warp import transform_bounds
from rasterio.windows import from_bounds


BOX_CRS = "EPSG:4326"


def parse_bbox(raw) -> list[float]:
    """Ensures the given bbox is correct for both strings and lists of numbers.

    e.g.: "5,45,10,47" -> (5,45,10,47)
    """
    if isinstance(raw, str):
        raw = literal_eval(raw)  #
    if not (isinstance(raw, (list, tuple)) and len(raw) == 4):
        raise ValueError("bbox must be [minx, miny, maxx, maxy]")
    return list(map(float, raw))


bbox: list[float] | None = snakemake.params.get("bbox", None)
buffer_degrees: float | None = snakemake.params.get("buffer_degrees", None)
cog_url: str | None = snakemake.params.get("cog_url", None)
vector_path: str | None = snakemake.input.get("vector", None)
tiff_path: str | None = snakemake.input.get("raster", None)

assert (bbox is None) ^ (vector_path is None), (
    "Specify either params.bbox OR input.vector."
)
assert (cog_url is None) ^ (tiff_path is None), (
    "Specify either params.cog_url OR input.raster."
)
assert (bbox is None) or (isinstance(bbox, (list, tuple)) and len(bbox) == 4), (
    "params.bbox must be a 4-element list [minx, miny, maxx, maxy]."
)


if vector_path is None:
    b_minx, b_miny, b_maxx, b_maxy = parse_bbox(bbox)
else:
    gdf = gpd.read_file(vector_path)
    if gdf.empty:
        raise ValueError("The given vector file is empty.")
    if gdf.crs is None:
        raise ValueError("The given vector file has no valid CRS.")
    gdf = gdf.to_crs(BOX_CRS)
    b_minx, b_miny, b_maxx, b_maxy = gdf.total_bounds

if buffer_degrees:
    b_minx -= buffer_degrees
    b_miny -= buffer_degrees
    b_maxx += buffer_degrees
    b_maxy += buffer_degrees

# ------------------------------------------------------------------
# Identify if remote or local raster .TIFF and set options
# ------------------------------------------------------------------
raster_uri = cog_url or tiff_path
environment_options: dict[str, str] = {}
if raster_uri is cog_url:
    environment_options = {
        "GDAL_DISABLE_READDIR_ON_OPEN": "YES",
        "CPL_VSIL_CURL_USE_HEAD": "YES",
        "CPL_VSIL_CURL_ALLOWED_EXTENSIONS": "tif,tiff",
    }

# ------------------------------------------------------------------
# Open raster, convert bounds to raster CRS and clip
# ------------------------------------------------------------------
with (
    rasterio.Env(**environment_options),
    rasterio.open(raster_uri) as src,
):
    if src.crs is None:
        raise ValueError("Source raster has no CRS.")

    r_minx, r_miny, r_maxx, r_maxy = transform_bounds(
        BOX_CRS, src.crs, b_minx, b_miny, b_maxx, b_maxy, densify_pts=21
    )

    window = from_bounds(r_minx, r_miny, r_maxx, r_maxy, src.transform)
    data = src.read(window=window, boundless=True)
    out_tr = src.window_transform(window)

    meta = src.meta.copy()
    meta.update(
        driver="GTiff",
        height=data.shape[1],
        width=data.shape[2],
        transform=out_tr,
        compress="deflate",
        tiled=True,
    )

with rasterio.open(snakemake.output.path, "w", **meta) as dst:
    dst.write(data)

__author__ = "Ivan Ruiz Manuel"
__copyright__ = "Copyright 2025, Ivan Ruiz Manuel"
__email__ = "i.ruizmanuel@tudelft.nl"
__license__ = "MIT"

import geopandas as gpd
import rasterio
from rasterio.warp import transform_bounds
from rasterio.windows import from_bounds


bbox: list[float] | None = snakemake.params.get("bbox", None)
buffer_degrees: float | None = snakemake.params.get("buffer_degrees", None)
vector_path: str | None = snakemake.input.get("vector", None)


assert (bbox is None) ^ (vector_path is None), (
    "Specify either params.bbox OR input.vector, not both."
)


box_crs = "EPSG:4326"

if vector_path is not None:
    gdf = gpd.read_file(vector_path)
    if gdf.empty:
        raise ValueError("The given vector file is empty.")
    if gdf.crs is None:
        raise ValueError("The given vector file has no valid CRS.")
    gdf = gdf.to_crs(box_crs)
    b_minx, b_miny, b_maxx, b_maxy = gdf.total_bounds

else:
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValueError(
            "params.bbox must be a 4-element list [minx, miny, maxx, maxy]."
        )
    b_minx, b_miny, b_maxx, b_maxy = map(float, bbox)  # force numeric

if buffer_degrees:
    b_minx -= buffer_degrees
    b_miny -= buffer_degrees
    b_maxx += buffer_degrees
    b_maxy += buffer_degrees

# ------------------------------------------------------------------
# open raster and convert bounds to raster CRS
# ------------------------------------------------------------------
with (
    rasterio.Env(
        GDAL_DISABLE_READDIR_ON_OPEN="YES",
        CPL_VSIL_CURL_USE_HEAD=True,
        CPL_VSIL_CURL_ALLOWED_EXTENSIONS="tif",
    ),
    rasterio.open(snakemake.params.tiff_url) as src,
):
    # ── safety check ────────────────────────────────────────────────
    if src.crs is None:
        raise ValueError("Source raster has no CRS.")

    # densify_pts>4 avoids distortions when crossing UTM zones
    r_minx, r_miny, r_maxx, r_maxy = transform_bounds(
        box_crs, src.crs, b_minx, b_miny, b_maxx, b_maxy
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

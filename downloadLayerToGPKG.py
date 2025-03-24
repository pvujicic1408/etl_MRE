import requests
import geopandas as gpd
import os

import downloadLayer


def download(layerID):
    os.makedirs("datasets", exist_ok=True)
    gdf = downloadLayer.download(layerID)
    gpkgPath = f"datasets/dataset_{layerID}.gpkg"
    gdf.set_crs(epsg=4326, inplace=True)
    gdf.to_file(gpkgPath, layer=f"layer_{layerID}", driver="GPKG")
    print(f"Podaci za sloj {layerID} sačuvani u {gpkgPath}")
    return gdf

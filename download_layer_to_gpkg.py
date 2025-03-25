import os

import download_layer


def download(layer_id):
    os.makedirs("datasets", exist_ok=True)
    gdf = download_layer.download(layer_id)
    gpkg_path = f"datasets/dataset_{layer_id}.gpkg"
    gdf.set_crs(epsg=4326, inplace=True)
    gdf.to_file(gpkg_path, layer=f"layer_{layer_id}", driver="GPKG")
    print(f"Podaci za sloj {layer_id} sacuvani u {gpkg_path}")
    return gdf

import os

import utils


def download(layer_id):
    """
        Funkcija koja preuzima podatke za layer, postavlja koordinatni referentni sistem
        i cuva podatke u GeoPackage formatu.

        Parameters:
            layer_id (int): ID sloja koji se preuzima i konvertuje.

        Returns:
            gdf (GeoDataFrame): GeoDataFrame sa podacima za sloj.
    """
    os.makedirs("datasets", exist_ok=True)
    gdf = utils.download_layer(layer_id)
    gpkg_path = f"datasets/dataset_{layer_id}.gpkg"
    gdf.set_crs(epsg=4326, inplace=True)
    gdf.to_file(gpkg_path, layer=f"layer_{layer_id}", driver="GPKG")
    print(f"Podaci za sloj {layer_id} sacuvani u {gpkg_path}")
    return gdf

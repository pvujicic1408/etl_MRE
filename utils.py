import requests
import geopandas as gpd

import available_layers
import change_crs_and_store_to_postgis
import download_layer_to_gpkg
import store_layer_to_postgis

URL = "https://gis.mre.gov.rs/arcgis/rest/services/OpenData/CISGIR/MapServer"


def validate_layer_id(layer_id):
    """Proverava da li je ID layera validan."""
    available_layer_ids = [str(layer[0]) for layer in available_layers.get()]
    if layer_id not in available_layer_ids:
        print(f"Layer sa ID {layer_id} nije dostupan.")
        return False
    return True


def handle_layer_action(action, layer_id):
    """Poziva odgovarajucu funkciju za rad sa layerom na osnovu akcije."""
    if action == "download_gpkg":
        download_layer_to_gpkg.download(layer_id)
    elif action == "store_postgis":
        store_layer_to_postgis.store(layer_id)
    elif action == "change_crs_postgis":
        change_crs_and_store_to_postgis.change_and_store(layer_id)


def get_layer_id():
    """Ispisi dostupne layere, zatrazi i proveri unos ID layera od korisnika."""
    available_layers.preview()
    layer_id = input("Upisite ID layera: ")
    if validate_layer_id(layer_id):
        return layer_id
    else:
        return None


def download_layer(layer_id):
    """
        Funkcija koja preuzima podatke za odredjeni layer sa ArcGIS REST servisa u GeoJSON formatu
        i vraca ga kao GeoDataFrame.

        Parameters:
            layer_id (int): ID sloja koji zelimo da preuzmemo sa ArcGIS servisa.

        Returns:
            gdf (GeoDataFrame): GeoDataFrame sa podacima za sloj, ili None ako dodje do greske.
    """
    query_url = f"{URL}/{layer_id}/query"
    params = {
        "where": "1=1",
        "outFields": "*",
        "returnGeometry": "true",
        "f": "geojson"
    }

    response = requests.get(query_url, params=params)

    if response.status_code == 200:
        data = response.json()
        gdf = gpd.GeoDataFrame.from_features(data["features"])
        gdf.set_crs(epsg=4326, inplace=True)
        return gdf
    else:
        print(f"Greska pri preuzimanju sloja {layer_id} - Status kod: {response.status_code}")
        return None

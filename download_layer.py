import requests
import geopandas as gpd

URL = "https://gis.mre.gov.rs/arcgis/rest/services/OpenData/CISGIR/MapServer"

def download(layer_id):
    """
        Funkcija koja preuzima podatke za odredjeni layer sa ArcGIS REST servisa u GeoJSON formatu
        i vraca ga kao GeoDataFrame.

        Parameters:
            layer_id (int): ID sloja koji zelimo da preuzmemo sa ArcGIS servisa.

        Returns:
            gdf (GeoDataFrame): GeoDataFrame sa podacima za sloj, ili None ako dođe do greske.
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

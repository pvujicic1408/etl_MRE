import requests
import geopandas as gpd

BASE_URL = "https://gis.mre.gov.rs/arcgis/rest/services/OpenData/CISGIR/MapServer"

def download(layer_id):
    query_url = f"{BASE_URL}/{layer_id}/query"
    params = {
        "where": "1=1",
        "outFields": "*",
        "returnGeometry": "true",
        "f": "geojson"
    }

    response = requests.get(query_url, params=params)

    if response.status_code != 200:
        print(f"Greska pri preuzimanju sloja {layer_id} - Status kod: {response.status_code}")
        return None

    data = response.json()

    gdf = gpd.GeoDataFrame.from_features(data["features"])
    gdf.set_crs(epsg=4326, inplace=True)
    return gdf


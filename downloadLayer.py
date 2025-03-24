import requests
import geopandas as gpd

BASE_URL = "https://gis.mre.gov.rs/arcgis/rest/services/OpenData/CISGIR/MapServer"

def download(layerID):
    queryUrl = f"{BASE_URL}/{layerID}/query"
    params = {
        "where": "1=1",
        "outFields": "*",
        "returnGeometry": "true",
        "f": "geojson"
    }

    response = requests.get(queryUrl, params=params)

    if response.status_code != 200:
        print(f"Greska pri preuzimanju sloja {layerID} - Status kod: {response.status_code}")
        return None

    data = response.json()

    if "features" not in data or not data["features"]:
        print(f"Sloj {layerID} nema dostupne podatke u formatu {format}.")
        return None

    try:
        gdf = gpd.GeoDataFrame.from_features(data["features"])
        gdf.set_crs(epsg=4326, inplace=True)
        return gdf
    except Exception as e:
        print(f"Greska pri konverziji sloja {layerID}: {e}")
        return None

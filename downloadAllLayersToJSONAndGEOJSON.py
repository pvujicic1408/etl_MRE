import requests
import json
import os

import Consts
import availableLayers


def downloadLayerData(layer_id, layer_name):
    query_url = f"{Consts.BASE_URL}/{layer_id}/query"
    params = {
        "where": "1=1",
        "outFields": "*",
        "returnGeometry": "true",
        "f": "json"
    }

    response = requests.get(query_url, params=params)
    if response.status_code == 200:
        data = response.json()

        os.makedirs("data", exist_ok=True)

        json_path = f"data/{layer_name}.json"
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"Sačuvan JSON: {json_path}")

        geojson_params = params.copy()
        geojson_params["f"] = "geojson"
        response_geojson = requests.get(query_url, params=geojson_params)

        if response_geojson.status_code == 200:
            geojson_data = response_geojson.json()
            geojson_path = f"data/{layer_name}.geojson"
            with open(geojson_path, "w", encoding="utf-8") as geojson_file:
                json.dump(geojson_data, geojson_file, ensure_ascii=False, indent=4)
            print(f"Sačuvan GeoJSON: {geojson_path}")
        else:
            print(f"Greška pri preuzimanju GeoJSON podataka za sloj {layer_name}")

    else:
        print(f"Greška pri preuzimanju podataka za sloj {layer_name} - Status kod: {response.status_code}")


def download(layers):
    layers = availableLayers.get()
    for layer_id, layer_name in layers:
        downloadLayerData(layer_id, layer_name)

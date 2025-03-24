import requests

import Consts


def get():
    response = requests.get(f"{Consts.BASE_URL}?f=json")
    if response.status_code == 200:
        data = response.json()
        layers = data.get("layers", [])
        return [(layer["id"], layer["name"]) for layer in layers]
    return []


def list():
    layers = get()
    for layer_id, layer_name in layers:
        print(f"Layer ID: {layer_id}, Name: {layer_name}")

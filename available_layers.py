import requests

URL = "https://gis.mre.gov.rs/arcgis/rest/services/OpenData/CISGIR/MapServer"

def get():
    """
        Funkcija koja salje GET zahtev ArcGIS REST servisu da bi dobila informacije o dostupnim layerima.

        Returns:
            Lista layera u formatu (ID, ime sloja).
    """
    response = requests.get(f"{URL}?f=json")
    if response.status_code == 200:
        data = response.json()
        layers = data.get("layers", [])
        return [(layer["id"], layer["name"]) for layer in layers]
    return []


def list():
    """
        Funkcija koja koristi funkciju 'get' da bi dobila listu layera,
        a zatim ih ispisuje na ekranu.
    """
    layers = get()
    for layer_id, layer_name in layers:
        print(f"Layer ID: {layer_id}, Name: {layer_name}")

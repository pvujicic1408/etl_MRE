import available_layers
import download_all_layers_to_json_and_geojson
import utils


def main():
    actions = {
        "1": lambda: available_layers.preview(),
        "2": lambda: download_all_layers_to_json_and_geojson.download(),
        "3": lambda: utils.handle_layer_action("download_gpkg", utils.get_layer_id()),
        "4": lambda: utils.handle_layer_action("store_postgis", utils.get_layer_id()),
        "5": lambda: utils.handle_layer_action("change_crs_postgis", utils.get_layer_id()),
        "6": lambda: exit()
    }

    while True:
        print("\nIzaberite opciju:")
        print("1. Proveri dostupne slojeve")
        print("2. Preuzmi podatke za sve layere u json i geojson")
        print("3. Preuzmi i pakuj dataset u GeoPackage")
        print("4. Preuzmi i upisi dataset u PostGIS bazu")
        print("5. Preuzmi, transformisi iz EPSG:4326 u EPSG:32634 i upisi dataset u PostGIS bazu")
        print("6. Izlaz")

        choice = input("Unesi broj opcije:")

        if choice in actions:
            actions[choice]()
        else:
            print("Pogresan unos. Unesite broj izmedju 1 i 6.")


if __name__ == "__main__":
    main()

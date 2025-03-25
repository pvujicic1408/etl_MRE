import available_layers
import change_crs_and_store_to_postgis
import download_all_layers_to_json_and_geojson
import download_layer_to_gpkg
import store_layer_to_postgis


def prikazi_opcije():
    while True:
        print("\nIzaberite opciju:")
        print("1. Proveri dostupne slojeve")
        print("2. Preuzmi podatke za sve layere u json i geojson")
        print("3. Preuzmi i pakuj dataset u GeoPackage")
        print("4. Preuzmi i upisi dataset u PostGIS bazu")
        print("5. Preuzmi, transformisi iz EPSG:4326 u EPSG:32634 i upisi dataset u PostGIS bazu")
        print("6. Izlaz")

        choice = input("Unesi broj opcije:")

        if choice == "1":
            available_layers.list()
        elif choice == "2":
            download_all_layers_to_json_and_geojson.download()
        elif choice == "3":
            available_layers.list()
            layer_id = input("Upisite ID sloja: ")
            download_layer_to_gpkg.download(layer_id)
        elif choice == "4":
            available_layers.list()
            layer_id = input("Upisite ID sloja: ")
            store_layer_to_postgis.store(layer_id)
        elif choice == "5":
            available_layers.list()
            layer_id = input("Upisite ID sloja: ")
            change_crs_and_store_to_postgis.change_and_store(layer_id)
        else:
            break
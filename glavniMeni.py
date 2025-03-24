import availableLayers
import changeCRSAndStoreToPostGIS
import downloadAllLayersToJSONAndGEOJSON
import downloadLayerToGPKG
import storeLayerToPostGIS


def prikaziOpcije():
    while True:
        print("\nIzaberite opciju:")
        print("1. Proveri dostupne slojeve")
        print("2. Preuzmi podatke za sve layer-e u json i geojson")
        print("3. Preuzmi i pakuj dataset u GeoPackage")
        print("4. Preuzmi i upisi dataset u PostGIS bazu")
        print("5. Preuzmi, transformisi iz EPSG:4326 u EPSG:32634 i upisi dataset u PostGIS bazu")
        print("6. Izlaz")

        choice = input("Unesi broj opcije:")

        if choice == "1":
            availableLayers.list()
        elif choice == "2":
            downloadAllLayersToJSONAndGEOJSON.download()
        elif choice == "3":
            availableLayers.list()
            layerID = input("Upisite ID sloja: ")
            downloadLayerToGPKG.download(layerID)
        elif choice == "4":
            availableLayers.list()
            layerID = input("Upisite ID sloja: ")
            storeLayerToPostGIS.store(layerID)
        elif choice == "5":
            availableLayers.list()
            layerID = input("Upisite ID sloja: ")
            changeCRSAndStoreToPostGIS.changeAndStore(layerID)
        else:
            break
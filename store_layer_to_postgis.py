import create_engine
import download_layer


def store(layer_id):
    """
        Funkcija preuzima podatke za dati layer sa GIS servera i upisuje ih u PostgreSQL bazu podataka.
        Preuzimanje podataka se vrsi korišćenjem funkcije 'download' iz modula 'download_layer'.

        Args:
        layer_id (int): ID layera ciji se podaci preuzimaju i upisuju u bazu.
    """
    gdf = download_layer.download(layer_id)
    if gdf is not None:
        table_name = f"layer_{layer_id}"
        gdf.to_postgis(table_name, create_engine.create(), if_exists="replace", index=False)
        print(f"Podaci za sloj {layer_id} su uspesno upisani u tabelu {table_name} u PostgreSQL bazi.")
    else:
        print(f"Greska: Podaci za sloj {layer_id} nisu preuzeti.")

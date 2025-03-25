import create_engine
import download_layer


def store(layer_id):
    gdf = download_layer.download(layer_id)
    if gdf is not None:
        table_name = f"layer_{layer_id}"
        gdf.to_postgis(table_name, create_engine.create(), if_exists="replace", index=False)
        print(f"Podaci za sloj {layer_id} su uspesno upisani u tabelu {table_name} u PostgreSQL bazi.")

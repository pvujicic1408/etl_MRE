import pandas as pd

import create_engine
import utils


def change_and_store(layer_id):
    """
        Funkcija koja preuzima layer, transformise koordinate iz EPSG:4326 u EPSG:32634, dodaje datum upisa i
        upisuje podatke u PostgreSQL bazu podataka sa PostGIS ekstenzijom.

        Args:
        - layer_id: ID sloja koji se preuzima i transformise
    """
    gdf = utils.download_layer(layer_id)

    if gdf is not None:
        gdf = gdf.to_crs("EPSG:32634")
        gdf['datum_upisa'] = pd.to_datetime('now').strftime('%d-%m-%Y %H-%M-%S')
        gdf.columns = [col.lower().replace(' ', '_') for col in gdf.columns]

        table_name = f"layer_{layer_id}_transformed"
        gdf.to_postgis(table_name, create_engine.create(), if_exists="replace", index=False)
        print(
            f"Podaci za sloj {layer_id} sa transformisanim koordinatama su uspesno upisani u tabelu {table_name} u PostgreSQL bazi.")
    else:
        print(f"Greska: Podaci za sloj {layer_id} nisu preuzeti.")
import createEngine
import downloadLayer
import pandas as pd


def changeAndStore(layerID):
    gdf = downloadLayer.download(layerID)

    if gdf is not None:
        gdf = gdf.to_crs("EPSG:32634")
        gdf['datum_upisa'] = pd.to_datetime('now').strftime('%d-%m-%Y %H-%M-%S')
        gdf.columns = [col.lower().replace(' ', '_') for col in gdf.columns]

        tableName = f"layer_{layerID}_transformed"
        gdf.to_postgis(tableName, createEngine.create(), if_exists="replace", index=False)
        print(
            f"Podaci za sloj {layerID} sa transformisanim koordinatama su uspešno upisani u tabelu {tableName} u PostgreSQL bazi.")

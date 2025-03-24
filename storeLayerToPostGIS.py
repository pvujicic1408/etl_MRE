import createEngine
import downloadLayer


def store(layerID):
    gdf = downloadLayer.download(layerID)
    if gdf is not None:
        tableName = f"layer_{layerID}"
        gdf.to_postgis(tableName, createEngine.create(), if_exists="replace", index=False)
        print(f"Podaci za sloj {layerID} su uspešno upisani u tabelu {tableName} u PostgreSQL bazi.")

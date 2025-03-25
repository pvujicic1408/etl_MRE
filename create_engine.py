from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "1408"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "gis_database"


def create():
    return create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

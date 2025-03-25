from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "1408"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "gis_database"


def create():
    """
       Funkcija koja kreira i vraca konekciju sa PostgreSQL bazom podataka.
       Konekcija koristi korisnicke podatke, host, port i ime baze podataka definisane na pocetku.

       Returns:
           engine: Objekat koji omogucava rad sa bazom podataka
    """
    return create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

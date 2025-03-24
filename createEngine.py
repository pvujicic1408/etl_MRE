from sqlalchemy import create_engine

import Consts


def create():
    return create_engine(
        f"postgresql://{Consts.DB_USER}:{Consts.DB_PASSWORD}@{Consts.DB_HOST}:{Consts.DB_PORT}/{Consts.DB_NAME}")

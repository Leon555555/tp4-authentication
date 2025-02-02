from sqlalchemy import create_engine, MetaData
from files.config import DATABASE_URL

# Crear la conexión a la base de datos
engine = create_engine(DATABASE_URL)
metadata = MetaData()

def get_db():
    """
    Genera una conexión con la base de datos.
    """
    with engine.connect() as connection:
        yield connection

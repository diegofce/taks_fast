from database.base import Base, engine
from models.tarea import Tarea

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas correctamente")
"""
Crea las tablas en la base de datos
"""
if __name__ == "__main__":
    init_db()

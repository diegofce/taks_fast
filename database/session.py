from sqlalchemy.orm import sessionmaker
from database.base import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

#Autocommit: No enviar cambios automatica si no manual

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

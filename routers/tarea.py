from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.tarea import TareaCreate, TareaOut
from crud import tarea as crud_tarea
from database.session import get_db

router = APIRouter()

#Crear un registro de tarea o tarea nueva
@router.post("/")

# La siguiente funcion, crea una tarea llamando a la clase TareaCreate, la sesion de la base de datos, que depende de get_db y retorna la tarea creada.
def crear(tarea: TareaCreate, db: Session = Depends(get_db)):
    return crud_tarea.crear_tarea(db, tarea)


@router.get("/", response_model=list[TareaOut])
def listar(db: Session = Depends(get_db)):
    return crud_tarea.obtener_tareas(db)

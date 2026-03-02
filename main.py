from fastapi import FastAPI
from routers import tarea
from fastapi.responses import Response
from init_db import init_db
from database.create import crear_db
from config import settings

app = FastAPI()

crear_db(
    settings.DB_NAME,
    settings.DB_USER,
    settings.DB_PASSWORD,
    settings.DB_HOST,
)

init_db()

app.include_router(tarea.router, prefix="/tareas", tags=["Tareas"])

@app.get("/Favicon.ico")
async def favicon():
    return Response(status_code=204)

@app.get("/")
def root():
    return {"Mensaje:": "Gestion de tareas"}


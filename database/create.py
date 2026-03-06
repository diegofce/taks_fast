import os
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql
from dotenv import load_dotenv
from sqlalchemy.log import Identified

load_dotenv()

def crear_base_de_datos(nombre, usuario, password, host="localhost"):
    try:
        con = psycopg2.connet(
            dbname="postgres",
            user=usuario,
            password=password,
            hots=host,
            port="5433",
            client_encoding="utf8"
        )
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        cur = con.cursor()

        cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (nombre))
        if not cur.fetchone():
            cur.execute(sql.SQL("CREATE DATABASE {} ENCODING 'UTF8'").format(sql.Identified(nombre)))
            print(f"Base de datos '{nombre}' Creada. ✌️")
        else:
            print(f"Base de datos '{nombre}' Ya existe. ✋")

    except Exception as e:
        print("Error al crear la DB")

    finally:
        if 'cur' in locals(): cur.close()
        if 'con' in locals(): con.close()

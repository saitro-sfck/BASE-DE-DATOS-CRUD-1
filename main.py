import sqlite3
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="CRUD Materias y Estudiantes - SQLite")
DB_NAME = "database.db"


def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS inscripciones (
            id INTEGER NOT NULL,
            usuario TEXT NOT NULL,
            nombre_completo TEXT NOT NULL,
            materia TEXT NOT NULL,
            paralelo TEXT NOT NULL,
            semestre INTEGER NOT NULL,
            codigo_estudiante TEXT NOT NULL,
            PRIMARY KEY (id, materia)
        )
    """
    )
    conn.commit()
    conn.close()


init_db()


class RegistroCrear(BaseModel):
    id: int 
    usuario: str
    nombre_completo: str
    materia: str
    paralelo: str
    semestre: int
    codigo_estudiante: str


class RegistroActualizar(BaseModel):
    usuario: Optional[str] = None
    nombre_completo: Optional[str] = None
    materia: Optional[str] = None
    paralelo: Optional[str] = None
    semestre: Optional[int] = None
    codigo_estudiante: Optional[str] = None


@app.post("/inscripciones/", status_code=201)
def crear_registro(registro: RegistroCrear):
    conn = get_db()
    cursor = conn.cursor()
    query = """
        INSERT INTO inscripciones (id, usuario, nombre_completo, materia, paralelo, semestre, codigo_estudiante)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    try:
        cursor.execute(
            query,
            (
                registro.id,
                registro.usuario,
                registro.nombre_completo,
                registro.materia,
                registro.paralelo,
                registro.semestre,
                registro.codigo_estudiante,
            ),
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(
            status_code=400,
            detail=f"El estudiante con ID {registro.id} ya se encuentra inscrito en '{registro.materia}'.",
        )

    conn.close()
    return registro.model_dump()


@app.get("/inscripciones/")
def obtener_registros():
    conn = get_db()
    cursor = conn.cursor()
    query = "SELECT id, usuario, nombre_completo, materia, paralelo, semestre, codigo_estudiante FROM inscripciones"
    cursor.execute(query)
    filas = cursor.fetchall()
    conn.close()
    return [dict(fila) for fila in filas]



@app.get("/inscripciones/{registro_id}")
def obtener_registro(registro_id: int):
    conn = get_db()
    cursor = conn.cursor()
    query = """
        SELECT id, usuario, nombre_completo, materia, paralelo, semestre, codigo_estudiante 
        FROM inscripciones 
        WHERE id = ?
    """
    cursor.execute(query, (registro_id,))
    filas = cursor.fetchall()
    conn.close()

    if not filas:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontraron inscripciones para el ID {registro_id}",
        )

    estudiante = filas[0]

    materias_inscritas = []
    for fila in filas:
        materias_inscritas.append(
            {
                "materia": fila["materia"],
                "paralelo": fila["paralelo"],
                "semestre": fila["semestre"],
            }
        )

    return {
        "id": estudiante["id"],
        "codigo_estudiante": estudiante["codigo_estudiante"],
        "usuario": estudiante["usuario"],
        "nombre_completo": estudiante["nombre_completo"],
        "materias": materias_inscritas,
    }


@app.delete("/inscripciones/{registro_id}")
def eliminar_registro(registro_id: int):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM inscripciones WHERE id = ?", (registro_id,))
    if cursor.fetchone() is None:
        conn.close()
        raise HTTPException(
            status_code=404, detail="Estudiante no encontrado"
        )

    cursor.execute("DELETE FROM inscripciones WHERE id = ?", (registro_id,))
    conn.commit()
    conn.close()
    return {
        "mensaje": (
            f"Todas las inscripciones del estudiante con ID {registro_id}"
            " fueron eliminadas"
        )
    }





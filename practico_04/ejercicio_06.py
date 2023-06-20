from soporte.practico_04.ejercicio_01 import borrar_tabla, crear_tabla
import datetime
from soporte.practico_04.ejercicio_01 import reset_tabla
from soporte.practico_04.ejercicio_02 import agregar_persona
from soporte.practico_04.ejercicio_04 import buscar_persona
from soporte.practico_04.ejercicio_01 import con


def crear_tabla_peso():
    """Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
        - IdPersona: Int() (Clave Foranea Persona)
        - Fecha: Date()
        - Peso: Int()
    """
    query = """CREATE TABLE IF NOT EXISTS persona_peso
              (idPersona INTEGER,
              fecha DATE,
              peso INTEGER NOT NULL,
              PRIMARY KEY (idPersona, fecha),
              FOREIGN KEY (idPersona) REFERENCES persona (idPersona)
              )"""
    con.execute(query)
    con.commit()
    pass # Completar


def borrar_tabla_peso():
    """Implementar la funcion borrar_tabla, que borra la tabla creada
    anteriormente."""
    query = """DROP TABLE IF EXISTS persona_peso"""
    con.execute(query)
    con.commit()
    pass # Completar

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN

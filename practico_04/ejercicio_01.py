import sqlite3

def crear_tabla():
    """Implementar la funcion crear_tabla, que cree una tabla Persona con:
        - IdPersona: Int() (auto-incrementing)
        - Nombre: Char(30)
        - FechaNacimiento: Date()
        - DNI: Int()
        - Altura: Int()
    """
    con = sqlite3.connect(':memory:')
    query = """CREATE TABLE IF NOT EXISTS persona
              (idPersona INT NOT NULL,
              nombre VARCHAR(45) NOT NULL,
              fecha_nacimiento DATE NOT NULL,
              dni INT NOT NULL,
              altura INT NOT NULL,
              PRIMARY KEY (idPersona))"""
    con.execute(query)
    con.commit()
    pass # Completar


def borrar_tabla():
    """Implementar la funcion borrar_tabla, que borra la tabla creada 
    anteriormente."""
    con = sqlite3.connect(':memory:')
    query = """DROP TABLE persona"""
    con.execute(query)
    con.commit()

# NO MODIFICAR - INICIO
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
# NO MODIFICAR - FIN

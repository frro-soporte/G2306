"""Base de Datos SQL - Baja"""

import datetime

from soporte.practico_04.ejercicio_01 import reset_tabla
from soporte.practico_04.ejercicio_02 import agregar_persona
from soporte.practico_04.ejercicio_01 import con

def borrar_persona(id_persona):
    """Implementar la funcion borrar_persona, que elimina un registro en la
    tabla Persona. Devuelve un booleano en base a si encontro el registro y lo
    borro o no."""

    c = con.cursor()
    data = (id_persona,)
    statement = "DELETE FROM persona WHERE idPersona=?"
    c.execute(statement, data)
    con.commit()
    return True if c.rowcount > 0 else False
# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN

import datetime
from soporte.practico_04.ejercicio_01 import reset_tabla
from soporte.practico_04.ejercicio_02 import agregar_persona
from soporte.practico_04.ejercicio_01 import con


def buscar_persona(id_persona):
    """Implementar la funcion buscar_persona, que devuelve el registro de una
    persona basado en su id. El return es una tupla que contiene sus campos:
    id, nombre, nacimiento, dni y altura. Si no encuentra ningun registro,
    devuelve False."""
    c = con.cursor()
    data = (id_persona,)
    statement = "SELECT * FROM persona WHERE idPersona=?"
    c.execute(statement, data)
    con.commit()
    persona = c.fetchone()
    if persona:
        persona = list(persona)
        persona[2] = str(persona[2])
        return tuple(persona)
    else:
        return False
    pass # Completar

# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN

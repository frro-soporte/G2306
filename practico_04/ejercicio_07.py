from soporte.practico_04.ejercicio_01 import borrar_tabla, crear_tabla
import datetime
from soporte.practico_04.ejercicio_02 import agregar_persona
from soporte.practico_04.ejercicio_04 import buscar_persona
from soporte.practico_04.ejercicio_01 import con
from soporte.practico_04.ejercicio_02 import agregar_persona
from soporte.practico_04.ejercicio_06 import reset_tabla

def buscar_fecha(id_persona, fe):
    c = con.cursor()
    data = (id_persona,)
    statement = "SELECT MAX(fecha) FROM persona_peso WHERE idPersona=?"
    c.execute(statement, data)
    con.commit()
    f = str(c.fetchone()[0])
    fe = str(fe)
    if f < fe:
        return True
    else:
        return False

def agregar_peso(id_persona, fecha, peso):
    """Implementar la funcion agregar_peso, que inserte un registro en la tabla
    PersonaPeso.

    Debe validar:
    - Que el ID de la persona ingresada existe (reutilizando las funciones ya
        implementadas).
    - Que no existe de esa persona un registro de fecha posterior al que
        queremos ingresar.

    Debe devolver:
    - ID del peso registrado.
    - False en caso de no cumplir con alguna validacion."""
    if buscar_persona(id_persona) and buscar_fecha(id_persona, fecha):
        c = con.cursor()
        data = (id_persona, fecha, peso)
        statement = "INSERT INTO persona_peso (idPersona, fecha, peso) VALUES (?, ?, ?)"
        c.execute(statement, data)
        con.commit()
        return c.lastrowid
    else: return False
    pass # Completar


# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # Test Id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # Test Registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN

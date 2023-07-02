"""Base de Datos SQL - Alta"""

import datetime
#from practico_04.ejercicio_01 import reset_tabla

con = sqlite3.connect(':memory:') 

def agregar_persona(nombre, nacimiento, dni, altura):

    c = con.cursor()
    data = (nombre, nacimiento, dni, altura)
    statement = "INSERT INTO persona (nombre, fecha_nacimiento, dni, altura) VALUES (?, ?, ?, ?)"
    c.execute(statement, data)
    con.commit()
    return c.lastrowid



# NO MODIFICAR - INICIO
@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()
# NO MODIFICAR - FIN

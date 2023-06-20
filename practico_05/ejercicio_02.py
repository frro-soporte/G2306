"""Base de Datos - ORM"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from ejercicio_01 import Base, Socio
from typing import List, Optional
from sqlalchemy.orm.exc import UnmappedInstanceError

class DatosSocio():

    def __init__(self):
        self.__engine = create_engine("sqlite:///:memory:")
        self.__Session = sessionmaker(bind=self.__engine)
        Base.metadata.create_all(bind=self.__engine)

    def buscar(self, id_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su id. Devuelve None si no
        encuentra nada.
        """
        session = self.__Session
        s = session.query(Socio).filter(id_socio == Socio.id_socio).first()
        session.close()
        return s
        pass  # Completar

    def buscar_dni(self, dni_socio: int) -> Optional[Socio]:
        """Devuelve la instancia del socio, dado su dni. Devuelve None si no
        encuentra nada.
        """
        session = self.__Session
        s = session.query(Socio).filter(dni_socio == Socio.dni).first()
        session.close()
        return s
        pass  # Completar

    def todos(self) -> List[Socio]:
        """Devuelve listado de todos los socios en la base de datos."""
        session = self.__Session
        ls = session.query(Socio).all()
        print('Lista de socios:')
        for p in ls:
            print('Socio: ', p.id, p.nombre)
        session.close()
        return ls
        pass  # Completar

    def borrar_todos(self) -> bool:
        """Borra todos los socios de la base de datos. Devuelve True si el
        borrado fue exitoso.
        """
        session = self.__Session
        session.query(Socio).delete()
        session.close()
        return True
        pass  # Completar

    def alta(self, socio: Socio) -> Socio:
        """Agrega un nuevo socio a la tabla y lo devuelve"""
        session = self.__Session
        session.add(socio)
        session.commit()
        session.close()
        return socio
        pass  # Completar

    def baja(self, id_socio: int) -> bool:
        """Borra el socio especificado por el id. Devuelve True si el borrado
        fue exitoso.
        """
        session = self.__Session
        s = self.buscar(id_socio)
        if s is not None:
            session.delete(s)
            session.commit()
            rta = True
        else:
            print('No se encontró el registro')
            rta = False
        session.close()
        return rta
        pass  # Completar

    def modificacion(self, socio: Socio) -> Socio:
        """Guarda un socio con sus datos modificados. Devuelve el Socio
        modificado.
        """
        session = self.__Session
        s = self.buscar(socio.id_socio)
        if s is not None:
            s.nombre = socio.nombre
            s.apellido = socio.apellido
            s.dni = socio.dni
            session.merge(s)
            session.commit()
        else:
            print('No se encontró el registro')
        session.close()
        return s
        pass  # Completar

    def contarSocios(self) -> int:
        """Devuelve el total de socios que existen en la tabla"""
        session = self.__Session
        cont = session.query(Socio).count()
        session.close()
        return cont
        pass  # Completar


# NO MODIFICAR - INICIO

# Test Creación
datos = DatosSocio()

# Test Alta
socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
assert socio.id_socio > 0

# Test Baja
assert datos.baja(socio.id) == True

# Test Consulta
socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
assert datos.buscar(socio_2.id) == socio_2

# Test Buscar DNI
socio_2 = datos.alta(Socio(dni=12345670, nombre='Carlos', apellido='Perez'))
assert datos.buscar_dni(socio_2.dni) == socio_2

# Test Modificación
socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
socio_3.nombre = 'Moria'
socio_3.apellido = 'Casan'
socio_3.dni = 13264587
datos.modificacion(socio_3)
socio_3_modificado = datos.buscar(socio_3.id)
assert socio_3_modificado.id == socio_3.id
assert socio_3_modificado.nombre == 'Moria'
assert socio_3_modificado.apellido == 'Casan'
assert socio_3_modificado.dni == 13264587

# Test Conteo
assert len(datos.todos()) == 3

# Test Delete
datos.borrar_todos()
assert len(datos.todos()) == 0

# NO MODIFICAR - FIN

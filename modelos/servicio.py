from abc import ABC, abstractmethod

# Clase abstracta base para los servicios de Software FJ.
# Las clases que se coloquen como hijas deben implementar sus métodos abstractos.

class Servicio(ABC):

    
    def __init__(self, id_servicio, nombre):
        self.__id_servicio = id_servicio
        self.__nombre = nombre
        self.__disponible = True  # Por defecto el servicio esta disponible

    # Retorna el identificador unico del servicio
    @property
    def id_servicio(self):
        return self.__id_servicio

    # Retorna el nombre del servicio
    @property
    def nombre(self):
        return self.__nombre

    # Retorna Verdadero si el servicio esta disponible, Falso si no
    @property
    def disponible(self):
        return self.__disponible

    # Establece la disponibilidad del servicio
    # valor verdadero para disponible, Falso para no disponible
    @disponible.setter
    def disponible(self, valor):
        self.__disponible = valor

    # Metodo abstracto para calcular el costo del servicio
    @abstractmethod
    def calcular_costo(self, horas, descuento=0, con_impuesto=False):
        pass

    # Metodo abstracto para retorna descripción detallada del servicio
    @abstractmethod
    def describir_servicio(self):
        pass

    # Metodo abstracto para validar que los parametros sean correctos
    @abstractmethod
    def validar_parametros(self):
        pass

    # Retorna una representación en texto del servicio
    def __str__(self):
        return f"Servicio [{self.__id_servicio}]: {self.__nombre}"
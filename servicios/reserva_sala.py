from modelos.servicio import Servicio
from excepciones.excepciones_personalizadas import ServicioNoDisponibleError, ParametroInvalidoError

# Clase concreta que representa el servicio de reserva de salas
# de reunion o trabajo de Software FJ.
# Hereda de la clase abstracta Servicio.

class ReservaSala(Servicio):

    # Constructor de la clase ReservaSala
    # id_servicio: Identificador unico del servicio
    # capacidad: Numero de personas que caben en la sala
    # precio_hora: Costo por hora de uso de la sala

    def __init__(self, id_servicio, capacidad, precio_hora):
        super().__init__(id_servicio, "Reserva de Sala")
        self.__capacidad = capacidad
        self.__precio_hora = precio_hora

    # Retorna la capacidad de la sala
    @property
    def capacidad(self):
        return self.__capacidad

    # Retorna el precio por hora de la sala
    @property
    def precio_hora(self):
        return self.__precio_hora

    # Valida que los parametros del servicio sean correctos
    # Lanza ParametroInvalidoError si la capacidad o precio no son válidos
    # Lanza ServicioNoDisponibleError si el servicio no está disponible

    def validar_parametros(self):
        if self.__capacidad <= 0:
            raise ParametroInvalidoError("La capacidad debe ser mayor a 0")
        if self.__precio_hora <= 0:
            raise ParametroInvalidoError("El precio por hora debe ser mayor a 0")
        if not self.disponible:
            raise ServicioNoDisponibleError("El servicio de reserva de sala no esta disponible")

    # Calcula el costo de la reserva segun las horas, impuesto y descuento
    # horas: cantidad de horas de uso de la sala
    # descuento: porcentaje de descuento (0 a 1). Por defecto 0
    # con_impuesto: si True aplica IVA del 19%. Por defecto False
    def calcular_costo(self, horas, descuento=0, con_impuesto=False):
        try:
            self.validar_parametros()
            impuesto = 0.19 if con_impuesto else 0
            costo = self.__precio_hora * horas * (1 + impuesto) * (1 - descuento)
            return round(costo, 2)
        except Exception as e:
            raise e

    # Retorna una descripcion detallada del servicio de reserva de sala
    def describir_servicio(self):
        return (f"Servicio: Reserva de Sala\n"
                f"Capacidad: {self.__capacidad} personas\n"
                f"Precio por hora: ${self.__precio_hora}\n"
                f"Disponible: {'Sí' if self.disponible else 'No'}")

    # Retorna una representacion en texto del servicio
    def __str__(self):
        return f"ReservaSala [{self.id_servicio}]: Capacidad {self.__capacidad} - ${self.__precio_hora}/hora"
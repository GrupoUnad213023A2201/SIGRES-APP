from modelos.servicio import Servicio
from excepciones.excepciones_personalizadas import ServicioNoDisponibleError, ParametroInvalidoError

# Clase concreta que representa el servicio de alquiler de equipos
# tecnologicos de Software FJ. Hereda de la clase abstracta Servicio.

class AlquilerEquipo(Servicio):

    # Constructor de la clase AlquilerEquipo
    # id_servicio: Identificador único del servicio
    # tipo_equipo: Tipo de equipo a alquilar (computador, proyector, etc.)
    # precio_dia: Costo por día de alquiler

    def __init__(self, id_servicio, tipo_equipo, precio_dia):
        super().__init__(id_servicio, "Alquiler de Equipo")
        self.__tipo_equipo = tipo_equipo
        self.__precio_dia = precio_dia

    # Retorna el tipo de equipo
    @property
    def tipo_equipo(self):
        return self.__tipo_equipo

    # Retorna el precio por día
    @property
    def precio_dia(self):
        return self.__precio_dia

    # Valida que los parametros del servicio sean correctos
    # Lanza ParametroInvalidoError si el tipo de equipo está vacio
    # Lanza ServicioNoDisponibleError si el servicio no está disponible

    def validar_parametros(self):
        if not self.__tipo_equipo or self.__tipo_equipo.strip() == "":
            raise ParametroInvalidoError("El tipo de equipo no puede estar vacio")
        if self.__precio_dia <= 0:
            raise ParametroInvalidoError("El precio por día debe ser mayor a 0")
        if not self.disponible:
            raise ServicioNoDisponibleError("El servicio de alquiler no está disponible")

    # Calcula el costo del alquiler segun los dias, impuesto y descuento
    # dias: cantidad de dias de alquiler
    # descuento: porcentaje de descuento (0 a 1). Por defecto 0
    # con_impuesto: si True aplica IVA del 19%. Por defecto False

    def calcular_costo(self, dias, descuento=0, con_impuesto=False):
        try:
            self.validar_parametros()
            impuesto = 0.19 if con_impuesto else 0
            costo = self.__precio_dia * dias * (1 + impuesto) * (1 - descuento)
            return round(costo, 2)
        except Exception as e:
            raise e

    # Retorna una descripcion detallada del servicio de alquiler
    def describir_servicio(self):
        return (f"Servicio: Alquiler de Equipo\n"
                f"Tipo de equipo: {self.__tipo_equipo}\n"
                f"Precio por día: ${self.__precio_dia}\n"
                f"Disponible: {'Si' if self.disponible else 'No'}")

    # Retorna una representación en texto del servicio
    def __str__(self):
        return f"AlquilerEquipo [{self.id_servicio}]: {self.__tipo_equipo} - ${self.__precio_dia}/día"
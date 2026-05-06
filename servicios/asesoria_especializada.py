from modelos.servicio import Servicio
from excepciones.excepciones_personalizadas import ServicioNoDisponibleError, ParametroInvalidoError

# Clase concreta que representa el servicio de asesorías
# tecnicas o profesionales de Software FJ.
# Hereda de la clase abstracta Servicio.

class AsesoriaEspecializada(Servicio):

    # Constructor de la clase AsesoriaEspecializada
    # id_servicio: Identificador unico del servicio
    # especialidad: Area de conocimiento de la asesoria (tecnologia, legal, financiera, etc.)
    # precio_hora: Costo por hora de asesoria

    def __init__(self, id_servicio, especialidad, precio_hora):
        super().__init__(id_servicio, "Asesoria Especializada")
        self.__especialidad = especialidad
        self.__precio_hora = precio_hora

    # Retorna la especialidad de la asesoria
    @property
    def especialidad(self):
        return self.__especialidad

    # Retorna el precio por hora de la asesoria
    @property
    def precio_hora(self):
        return self.__precio_hora

    # Valida que los parametros del servicio sean correctos
    # Lanza ParametroInvalidoError si la especialidad está vacia o el precio no es valido
    # Lanza ServicioNoDisponibleError si el servicio no esta disponible
    def validar_parametros(self):
        if not self.__especialidad or self.__especialidad.strip() == "":
            raise ParametroInvalidoError("La especialidad no puede estar vacia")
        if self.__precio_hora <= 0:
            raise ParametroInvalidoError("El precio por hora debe ser mayor a 0")
        if not self.disponible:
            raise ServicioNoDisponibleError("El servicio de asesoria no esta disponible")

    # Calcula el costo de la asesoria segun las horas, impuesto y descuento
    # horas: cantidad de horas de asesoria
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

    # Retorna una descripción detallada del servicio de asesoria
    def describir_servicio(self):
        return (f"Servicio: Asesoria Especializada\n"
                f"Especialidad: {self.__especialidad}\n"
                f"Precio por hora: ${self.__precio_hora}\n"
                f"Disponible: {'Sí' if self.disponible else 'No'}")

    # Retorna una representación en texto del servicio
    def __str__(self):
        return f"AsesoriaEspecializada [{self.id_servicio}]: {self.__especialidad} - ${self.__precio_hora}/hora"
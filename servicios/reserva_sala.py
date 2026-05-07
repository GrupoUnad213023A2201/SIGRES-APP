# =============================================================================
# SIGRES - Software FJ
# Archivo: servicios/reserva_sala.py
# Responsable: David
# =============================================================================

from modelos.servicio import Servicio
from excepciones.excepciones_personalizadas import ServicioInvalidoError, CalculoInconsistenteError
from utils.logger import log_info, log_error


class ReservaSala(Servicio):
    """Servicio especializado para reserva de salas de trabajo."""

    def __init__(self, nombre: str, capacidad: int, precio_hora: float):
        super().__init__(nombre, precio_hora)
        self.__capacidad = capacidad
        self.__precio_hora = precio_hora

    @property
    def capacidad(self) -> int:
        return self.__capacidad

    def calcular_costo(self, duracion: float, impuesto: float = 0, descuento: float = 0) -> float:
        try:
            self._validar_calculo(impuesto, descuento)
            if duracion <= 0:
                raise ServicioInvalidoError("La duración debe ser mayor a cero.")
            costo = self.__precio_hora * duracion * (1 + impuesto) * (1 - descuento)
            log_info(f"Costo ReservaSala '{self.nombre}': ${costo:,.0f} ({duracion}h, IVA:{impuesto}, Desc:{descuento})")
            return costo
        except (CalculoInconsistenteError, ServicioInvalidoError) as e:
            log_error(str(e))
            raise

    def describir_servicio(self) -> str:
        return (f"Reserva de Sala '{self.nombre}' | "
                f"Capacidad: {self.__capacidad} personas | "
                f"Precio: ${self.__precio_hora:,.0f}/hora")

    def validar_parametros(self) -> bool:
        try:
            if self.__capacidad <= 0:
                raise ServicioInvalidoError(f"La capacidad de la sala '{self.nombre}' debe ser mayor a cero.")
            if self.__precio_hora <= 0:
                raise ServicioInvalidoError(f"El precio por hora de '{self.nombre}' debe ser mayor a cero.")
        except ServicioInvalidoError as e:
            log_error(str(e))
            raise
        else:
            log_info(f"Servicio '{self.nombre}' validado correctamente.")
            return True
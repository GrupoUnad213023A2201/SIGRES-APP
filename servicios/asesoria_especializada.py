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


# =============================================================================
# Archivo: servicios/alquiler_equipo.py
# Responsable: David
# =============================================================================

from modelos.servicio import Servicio
from excepciones.excepciones_personalizadas import ServicioInvalidoError, CalculoInconsistenteError
from utils.logger import log_info, log_error


class AlquilerEquipo(Servicio):
    """Servicio especializado para alquiler de equipos tecnológicos."""

    def __init__(self, nombre: str, tipo_equipo: str, precio_dia: float):
        super().__init__(nombre, precio_dia)
        self.__tipo_equipo = tipo_equipo
        self.__precio_dia = precio_dia

    @property
    def tipo_equipo(self) -> str:
        return self.__tipo_equipo

    def calcular_costo(self, duracion: float, impuesto: float = 0, descuento: float = 0) -> float:
        try:
            self._validar_calculo(impuesto, descuento)
            if duracion <= 0:
                raise ServicioInvalidoError("La duración debe ser mayor a cero.")
            costo = self.__precio_dia * duracion * (1 + impuesto) * (1 - descuento)
            log_info(f"Costo AlquilerEquipo '{self.nombre}': ${costo:,.0f} ({duracion}d, IVA:{impuesto}, Desc:{descuento})")
            return costo
        except (CalculoInconsistenteError, ServicioInvalidoError) as e:
            log_error(str(e))
            raise

    def describir_servicio(self) -> str:
        return (f"Alquiler de Equipo '{self.nombre}' | "
                f"Tipo: {self.__tipo_equipo} | "
                f"Precio: ${self.__precio_dia:,.0f}/día")

    def validar_parametros(self) -> bool:
        try:
            if not self.__tipo_equipo or not self.__tipo_equipo.strip():
                raise ServicioInvalidoError(f"El tipo de equipo para '{self.nombre}' no puede estar vacío.")
            if self.__precio_dia <= 0:
                raise ServicioInvalidoError(f"El precio por día de '{self.nombre}' debe ser mayor a cero.")
        except ServicioInvalidoError as e:
            log_error(str(e))
            raise
        else:
            log_info(f"Servicio '{self.nombre}' validado correctamente.")
            return True


# =============================================================================
# Archivo: servicios/asesoria_especializada.py
# Responsable: David
# =============================================================================

from modelos.servicio import Servicio
from excepciones.excepciones_personalizadas import ServicioInvalidoError, CalculoInconsistenteError
from utils.logger import log_info, log_error


class AsesoriaEspecializada(Servicio):
    """Servicio especializado para asesorías técnicas o profesionales."""

    def __init__(self, nombre: str, especialidad: str, precio_hora: float):
        super().__init__(nombre, precio_hora)
        self.__especialidad = especialidad
        self.__precio_hora = precio_hora

    @property
    def especialidad(self) -> str:
        return self.__especialidad

    def calcular_costo(self, duracion: float, impuesto: float = 0, descuento: float = 0) -> float:
        try:
            self._validar_calculo(impuesto, descuento)
            if duracion <= 0:
                raise ServicioInvalidoError("La duración debe ser mayor a cero.")
            costo = self.__precio_hora * duracion * (1 + impuesto) * (1 - descuento)
            log_info(f"Costo Asesoría '{self.nombre}': ${costo:,.0f} ({duracion}h, IVA:{impuesto}, Desc:{descuento})")
            return costo
        except (CalculoInconsistenteError, ServicioInvalidoError) as e:
            log_error(str(e))
            raise

    def describir_servicio(self) -> str:
        return (f"Asesoría Especializada '{self.nombre}' | "
                f"Especialidad: {self.__especialidad} | "
                f"Precio: ${self.__precio_hora:,.0f}/hora")

    def validar_parametros(self) -> bool:
        try:
            if not self.__especialidad or not self.__especialidad.strip():
                raise ServicioInvalidoError(f"La especialidad de '{self.nombre}' no puede estar vacía.")
            if self.__precio_hora <= 0:
                raise ServicioInvalidoError(f"El precio por hora de '{self.nombre}' debe ser mayor a cero.")
        except ServicioInvalidoError as e:
            log_error(str(e))
            raise
        else:
            log_info(f"Servicio '{self.nombre}' validado correctamente.")
            return True

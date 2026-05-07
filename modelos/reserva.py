# =============================================================================
# SIGRES - Software FJ
# Archivo: modelos/reserva.py
# Responsable: Cristian
# Descripción: Clase Reserva que integra Cliente y Servicio con manejo
#              completo de estados y excepciones.
# =============================================================================

from datetime import datetime
from excepciones.excepciones_personalizadas import (
    ReservaInvalidaError,
    ReservaYaCanceladaError,
    ReservaYaConfirmadaError,
    ParametroFaltanteError
)
from utils.logger import log_info, log_warning, log_error


class Reserva:
    """
    Clase que representa una reserva dentro del sistema SIGRES.
    Integra un Cliente, un Servicio, fecha, hora, duración y estado.

    Estados posibles:
        'pendiente'  → Estado inicial al crear la reserva.
        'confirmada' → Reserva aceptada y lista para ejecutarse.
        'cancelada'  → Reserva anulada por el cliente o el sistema.
    """

    _contador_id = 0  # Autogeneración de IDs únicos

    def __init__(self, cliente, servicio, fecha: str, hora: str, duracion: float):
        """
        Constructor de la reserva.

        Args:
            cliente  : Objeto Cliente válido.
            servicio : Objeto Servicio válido.
            fecha    : Fecha en formato 'YYYY-MM-DD'.
            hora     : Hora en formato 'HH:MM'.
            duracion : Duración en horas o días (debe ser positiva).

        Raises:
            ParametroFaltanteError : Si cliente o servicio son None.
            ReservaInvalidaError   : Si fecha, hora o duración son inválidas.
        """
        try:
            if cliente is None:
                raise ParametroFaltanteError("cliente")
            if servicio is None:
                raise ParametroFaltanteError("servicio")
            if not fecha or not fecha.strip():
                raise ParametroFaltanteError("fecha")
            if not hora or not hora.strip():
                raise ParametroFaltanteError("hora")
            if duracion is None or duracion <= 0:
                raise ReservaInvalidaError(
                    "La duración debe ser un valor positivo mayor a cero."
                )

            # Validar formato de fecha
            datetime.strptime(fecha, "%Y-%m-%d")

            # Validar formato de hora
            datetime.strptime(hora, "%H:%M")

        except (ParametroFaltanteError, ReservaInvalidaError):
            raise
        except ValueError as e:
            raise ReservaInvalidaError(
                f"Formato de fecha u hora inválido: {e}"
            ) from e

        Reserva._contador_id += 1
        self.__id = Reserva._contador_id
        self.__cliente = cliente
        self.__servicio = servicio
        self.__fecha = fecha
        self.__hora = hora
        self.__duracion = duracion
        self.__estado = "pendiente"
        self.__fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_info(
            f"Reserva ID {self.__id} creada: "
            f"Cliente '{cliente.nombre}' - Servicio '{servicio.nombre}' "
            f"el {fecha} a las {hora}."
        )

    # ─────────────────────────────────────────
    #  GETTERS (Encapsulación)
    # ─────────────────────────────────────────

    @property
    def id(self) -> int:
        return self.__id

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def fecha(self) -> str:
        return self.__fecha

    @property
    def hora(self) -> str:
        return self.__hora

    @property
    def duracion(self) -> float:
        return self.__duracion

    @property
    def estado(self) -> str:
        return self.__estado

    # ─────────────────────────────────────────
    #  MÉTODOS DE GESTIÓN DE ESTADO
    # ─────────────────────────────────────────

    def confirmar(self):
        """
        Confirma la reserva cambiando su estado a 'confirmada'.
        Usa bloque try/except/else.

        Raises:
            ReservaYaConfirmadaError: Si la reserva ya estaba confirmada.
            ReservaInvalidaError    : Si la reserva está cancelada.
        """
        try:
            if self.__estado == "confirmada":
                raise ReservaYaConfirmadaError(self.__id)
            if self.__estado == "cancelada":
                raise ReservaInvalidaError(
                    f"No se puede confirmar la reserva ID {self.__id} porque está cancelada."
                )
        except (ReservaYaConfirmadaError, ReservaInvalidaError) as e:
            log_warning(str(e))
            raise
        else:
            self.__estado = "confirmada"
            log_info(f"Reserva ID {self.__id} confirmada exitosamente.")

    def cancelar(self):
        """
        Cancela la reserva cambiando su estado a 'cancelada'.
        Usa bloque try/except/finally.

        Raises:
            ReservaYaCanceladaError: Si la reserva ya estaba cancelada.
        """
        try:
            if self.__estado == "cancelada":
                raise ReservaYaCanceladaError(self.__id)
            self.__estado = "cancelada"
            log_info(f"Reserva ID {self.__id} cancelada exitosamente.")
        except ReservaYaCanceladaError as e:
            log_warning(str(e))
            raise
        finally:
            log_info(f"Proceso de cancelación de reserva ID {self.__id} finalizado.")

    def validar(self) -> bool:
        """
        Valida que los datos de la reserva sean correctos.

        Returns:
            bool: True si la reserva es válida.

        Raises:
            ReservaInvalidaError: Si algún dato es inválido.
        """
        try:
            datetime.strptime(self.__fecha, "%Y-%m-%d")
            datetime.strptime(self.__hora, "%H:%M")
            if self.__duracion <= 0:
                raise ReservaInvalidaError("La duración debe ser mayor a cero.")
        except ReservaInvalidaError:
            raise
        except ValueError as e:
            raise ReservaInvalidaError(f"Datos de reserva inválidos: {e}") from e
        return True

    def mostrar_info(self) -> str:
        """
        Retorna una cadena con la información completa de la reserva.
        """
        costo = self.__servicio.calcular_costo(self.__duracion)
        return (
            f"[Reserva ID: {self.__id}] "
            f"Cliente: {self.__cliente.nombre} | "
            f"Servicio: {self.__servicio.nombre} | "
            f"Fecha: {self.__fecha} {self.__hora} | "
            f"Duración: {self.__duracion} | "
            f"Costo base: ${costo:,.0f} | "
            f"Estado: {self.__estado.upper()}"
        )

    def __str__(self) -> str:
        return self.mostrar_info()

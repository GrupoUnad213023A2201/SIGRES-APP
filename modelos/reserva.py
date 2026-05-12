# =============================================================================
# SIGRES - Software FJ
# Archivo: modelos/reserva.py
# Responsable: Cristian
# Descripción: Clase Reserva que integra Cliente y Servicio con gestión
#              completa de estados y manejo avanzado de excepciones.
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

    Integra un objeto Cliente y un objeto Servicio con fecha, hora,
    duración y estado. Gestiona el ciclo de vida de la reserva mediante
    manejo avanzado de excepciones.

    Estados posibles:
        'pendiente'  → Estado inicial al crear la reserva.
        'confirmada' → Reserva aceptada y lista para ejecutarse.
        'cancelada'  → Reserva anulada por el cliente o el sistema.
    """

    # Contador de clase para autogenerar IDs únicos de reserva
    _contador_id = 0

    def __init__(self, cliente, servicio, fecha: str, hora: str, duracion: float):
        """
        Constructor de la reserva.

        Valida todos los parámetros antes de crear la reserva.
        Usa bloque try/except para capturar errores durante la creación.

        Args:
            cliente  : Objeto Cliente válido y registrado en el sistema.
            servicio : Objeto Servicio válido y disponible.
            fecha    : Fecha en formato 'YYYY-MM-DD'.
            hora     : Hora en formato 'HH:MM'.
            duracion : Duración en horas o días (debe ser mayor a cero).

        Raises:
            ParametroFaltanteError: Si cliente, servicio, fecha u hora son None.
            ReservaInvalidaError  : Si fecha, hora o duración son inválidas.
        """
        try:
            # Validar que cliente no sea None
            if cliente is None:
                raise ParametroFaltanteError("cliente")

            # Validar que servicio no sea None
            if servicio is None:
                raise ParametroFaltanteError("servicio")

            # Validar que fecha no esté vacía
            if not fecha or not fecha.strip():
                raise ParametroFaltanteError("fecha")

            # Validar que hora no esté vacía
            if not hora or not hora.strip():
                raise ParametroFaltanteError("hora")

            # Validar que la duración sea positiva
            if duracion is None or duracion <= 0:
                raise ReservaInvalidaError(
                    "La duración debe ser un valor positivo mayor a cero."
                )

            # Validar formato de fecha usando datetime
            datetime.strptime(fecha, "%Y-%m-%d")

            # Validar formato de hora usando datetime
            datetime.strptime(hora, "%H:%M")

        except (ParametroFaltanteError, ReservaInvalidaError):
            # Relanza las excepciones propias del sistema
            raise

        except ValueError as e:
            # Captura errores de formato de fecha u hora y los encadena
            raise ReservaInvalidaError(
                f"Formato de fecha u hora inválido. Use YYYY-MM-DD y HH:MM. Detalle: {e}"
            ) from e

        # Autogenerar ID único para la reserva
        Reserva._contador_id += 1
        self.__id = Reserva._contador_id

        # Asignar atributos privados de la reserva
        self.__cliente = cliente
        self.__servicio = servicio
        self.__fecha = fecha
        self.__hora = hora
        self.__duracion = duracion
        self.__estado = "pendiente"
        self.__fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Registrar creación exitosa en el log
        log_info(
            f"Reserva ID {self.__id} creada: "
            f"Cliente '{cliente.nombre}' - "
            f"Servicio '{servicio.nombre}' - "
            f"Fecha: {fecha} {hora}."
        )

    # ─────────────────────────────────────────
    #  GETTERS (Encapsulación)
    # ─────────────────────────────────────────

    @property
    def id(self) -> int:
        """Retorna el ID único de la reserva."""
        return self.__id

    @property
    def cliente(self):
        """Retorna el objeto Cliente asociado a la reserva."""
        return self.__cliente

    @property
    def servicio(self):
        """Retorna el objeto Servicio asociado a la reserva."""
        return self.__servicio

    @property
    def fecha(self) -> str:
        """Retorna la fecha de la reserva."""
        return self.__fecha

    @property
    def hora(self) -> str:
        """Retorna la hora de la reserva."""
        return self.__hora

    @property
    def duracion(self) -> float:
        """Retorna la duración de la reserva."""
        return self.__duracion

    @property
    def estado(self) -> str:
        """Retorna el estado actual de la reserva."""
        return self.__estado

    # ─────────────────────────────────────────
    #  MÉTODOS DE GESTIÓN DE ESTADO
    # ─────────────────────────────────────────

    def confirmar(self):
        """
        Confirma la reserva cambiando su estado a 'confirmada'.

        Usa bloque try/except/else para:
            - try   : Verificar que la reserva puede confirmarse
            - except: Capturar y registrar errores de estado
            - else  : Confirmar y registrar el éxito

        Raises:
            ReservaYaConfirmadaError: Si la reserva ya estaba confirmada.
            ReservaInvalidaError    : Si la reserva está cancelada.
        """
        try:
            # Verificar que no esté ya confirmada
            if self.__estado == "confirmada":
                raise ReservaYaConfirmadaError(self.__id)

            # Verificar que no esté cancelada
            if self.__estado == "cancelada":
                raise ReservaInvalidaError(
                    f"No se puede confirmar la reserva ID {self.__id} "
                    f"porque ya fue cancelada."
                )

        except (ReservaYaConfirmadaError, ReservaInvalidaError) as e:
            # Registra la advertencia en el log y relanza la excepción
            log_warning(f"No se pudo confirmar reserva ID {self.__id}: {e}")
            raise

        else:
            # Se ejecuta solo si no hubo excepciones: cambia el estado
            self.__estado = "confirmada"
            log_info(f"Reserva ID {self.__id} confirmada exitosamente.")
            print(f"  ✅ Reserva ID {self.__id} confirmada para '{self.__cliente.nombre}'.")

    def cancelar(self):
        """
        Cancela la reserva cambiando su estado a 'cancelada'.

        Usa bloque try/except/finally para:
            - try    : Verificar que la reserva puede cancelarse
            - except : Capturar y registrar errores de estado
            - finally: Registrar siempre que el proceso finalizó

        Raises:
            ReservaYaCanceladaError: Si la reserva ya estaba cancelada.
        """
        try:
            # Verificar que no esté ya cancelada
            if self.__estado == "cancelada":
                raise ReservaYaCanceladaError(self.__id)

            # Cambiar el estado a cancelada
            self.__estado = "cancelada"
            log_info(f"Reserva ID {self.__id} cancelada exitosamente.")
            print(f"  ✅ Reserva ID {self.__id} cancelada correctamente.")

        except ReservaYaCanceladaError as e:
            # Registra la advertencia en el log y relanza la excepción
            log_warning(f"No se pudo cancelar reserva ID {self.__id}: {e}")
            raise

        finally:
            # Se ejecuta siempre, haya o no excepción
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
            # Validar formato de fecha
            datetime.strptime(self.__fecha, "%Y-%m-%d")

            # Validar formato de hora
            datetime.strptime(self.__hora, "%H:%M")

            # Validar duración positiva
            if self.__duracion <= 0:
                raise ReservaInvalidaError(
                    "La duración debe ser mayor a cero."
                )

        except ReservaInvalidaError:
            raise

        except ValueError as e:
            raise ReservaInvalidaError(
                f"Datos de reserva inválidos: {e}"
            ) from e

        return True

    def mostrar_info(self) -> str:
        """
        Retorna una cadena con la información completa de la reserva,
        incluyendo el costo base calculado desde el servicio asociado.

        Returns:
            str: Información formateada de la reserva.
        """
        # Calcula el costo base usando el método del servicio asociado
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
        """Representación en cadena de la reserva."""
        return self.mostrar_info()
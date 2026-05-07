# =============================================================================
# SIGRES - Software FJ
# Archivo: excepciones/excepciones_personalizadas.py
# Descripción: Excepciones personalizadas del sistema
# =============================================================================


class SIGRESError(Exception):
    """
    Excepción base del sistema SIGRES.
    Todas las excepciones personalizadas heredan de esta clase.
    """
    def __init__(self, mensaje: str, codigo: str = "SIGRES-000"):
        self.mensaje = mensaje
        self.codigo = codigo
        super().__init__(f"[{codigo}] {mensaje}")


# ─────────────────────────────────────────
#  EXCEPCIONES DE CLIENTE
# ─────────────────────────────────────────

class ClienteInvalidoError(SIGRESError):
    """
    Se lanza cuando los datos de un cliente no cumplen las validaciones.
    Ejemplos: nombre vacío, correo sin @, teléfono no numérico.
    """
    def __init__(self, mensaje: str):
        super().__init__(mensaje, "SIGRES-101")


class ClienteNoEncontradoError(SIGRESError):
    """
    Se lanza cuando se intenta operar con un cliente que no existe.
    """
    def __init__(self, cliente_id):
        super().__init__(f"Cliente con ID '{cliente_id}' no encontrado.", "SIGRES-102")


# ─────────────────────────────────────────
#  EXCEPCIONES DE SERVICIO
# ─────────────────────────────────────────

class ServicioInvalidoError(SIGRESError):
    """
    Se lanza cuando los parámetros de un servicio son incorrectos.
    Ejemplos: duración negativa, precio cero, tipo no permitido.
    """
    def __init__(self, mensaje: str):
        super().__init__(mensaje, "SIGRES-201")


class ServicioNoDisponibleError(SIGRESError):
    """
    Se lanza cuando se intenta reservar un servicio no disponible.
    """
    def __init__(self, nombre_servicio: str):
        super().__init__(f"El servicio '{nombre_servicio}' no está disponible.", "SIGRES-202")


# ─────────────────────────────────────────
#  EXCEPCIONES DE RESERVA
# ─────────────────────────────────────────

class ReservaInvalidaError(SIGRESError):
    """
    Se lanza cuando una reserva no puede crearse por datos incorrectos.
    Ejemplos: fecha inválida, duración negativa, cliente o servicio nulos.
    """
    def __init__(self, mensaje: str):
        super().__init__(mensaje, "SIGRES-301")


class ReservaNoEncontradaError(SIGRESError):
    """
    Se lanza cuando se busca una reserva que no existe.
    """
    def __init__(self, reserva_id):
        super().__init__(f"Reserva con ID '{reserva_id}' no encontrada.", "SIGRES-302")


class ReservaYaCanceladaError(SIGRESError):
    """
    Se lanza cuando se intenta cancelar una reserva que ya fue cancelada.
    """
    def __init__(self, reserva_id):
        super().__init__(f"La reserva con ID '{reserva_id}' ya se encuentra cancelada.", "SIGRES-303")


class ReservaYaConfirmadaError(SIGRESError):
    """
    Se lanza cuando se intenta confirmar una reserva ya confirmada.
    """
    def __init__(self, reserva_id):
        super().__init__(f"La reserva con ID '{reserva_id}' ya se encuentra confirmada.", "SIGRES-304")


# ─────────────────────────────────────────
#  EXCEPCIONES DE PARÁMETROS Y CÁLCULOS
# ─────────────────────────────────────────

class ParametroFaltanteError(SIGRESError):
    """
    Se lanza cuando un parámetro requerido no fue proporcionado.
    """
    def __init__(self, parametro: str):
        super().__init__(f"El parámetro '{parametro}' es obligatorio y no fue proporcionado.", "SIGRES-401")


class CalculoInconsistenteError(SIGRESError):
    """
    Se lanza cuando un cálculo de costo produce un resultado inválido.
    Ejemplos: descuento mayor al 100%, impuesto negativo.
    """
    def __init__(self, mensaje: str):
        super().__init__(mensaje, "SIGRES-402")


class OperacionNoPermitidaError(SIGRESError):
    """
    Se lanza cuando se intenta realizar una operación no permitida por el sistema.
    """
    def __init__(self, mensaje: str):
        super().__init__(mensaje, "SIGRES-403")

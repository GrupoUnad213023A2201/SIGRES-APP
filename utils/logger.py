import logging
import os
from datetime import datetime

# ─────────────────────────────────────────
#  CONFIGURACIÓN DEL LOGGER - SIGRES
# ─────────────────────────────────────────

# Carpeta donde se guardarán los logs
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "sigres.log")

def configurar_logger():
    """
    Configura el sistema de logs del proyecto SIGRES.
    - Crea la carpeta /logs si no existe.
    - Registra eventos en archivo y en consola simultáneamente.
    """

    # Crear carpeta logs si no existe
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    # Formato del log: fecha/hora - nivel - mensaje
    formato = "%(asctime)s - %(levelname)s - %(message)s"
    fecha_formato = "%Y-%m-%d %H:%M:%S"

    # Configuración principal del logger
    logging.basicConfig(
        level=logging.DEBUG,
        format=formato,
        datefmt=fecha_formato,
        handlers=[
            # Handler 1: Escribe en el archivo sigres.log
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            # Handler 2: Muestra en consola
            logging.StreamHandler()
        ]
    )

# Inicializar el logger al importar el módulo
configurar_logger()
logger = logging.getLogger("SIGRES")


# ─────────────────────────────────────────
#  FUNCIONES DE REGISTRO
# ─────────────────────────────────────────

def log_info(mensaje: str):
    """
    Registra un evento informativo (acción exitosa).
    Ejemplo: cliente agregado, reserva creada.
    """
    logger.info(mensaje)


def log_warning(mensaje: str):
    """
    Registra una advertencia (situación inusual pero no crítica).
    Ejemplo: cliente no encontrado, servicio ya existente.
    """
    logger.warning(mensaje)


def log_error(mensaje: str):
    """
    Registra un error del sistema (fallo o dato inválido).
    Ejemplo: fecha inválida, campo vacío, error inesperado.
    """
    logger.error(mensaje)


def log_debug(mensaje: str):
    """
    Registra información de depuración (solo para desarrollo).
    Ejemplo: valores intermedios, flujos internos.
    """
    logger.debug(mensaje)


# ─────────────────────────────────────────
#  EJEMPLO DE USO (solo para pruebas)
# ─────────────────────────────────────────

if __name__ == "__main__":
    log_info("Sistema SIGRES iniciado correctamente")
    log_info("Cliente 'Juan Pérez' agregado exitosamente")
    log_warning("Cliente con ID 99 no encontrado")
    log_error("Fecha de reserva inválida: '32-13-2026'")
    log_debug("Valor de lista clientes: []")
    print(f"\nLog guardado en: {LOG_FILE}")
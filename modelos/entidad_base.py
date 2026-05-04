# =============================================================================
# SIGRES - Software FJ
# Archivo: modelos/entidad_base.py
# Descripción: Clase abstracta base del sistema. Todas las entidades
#              principales (Cliente, Servicio) heredan de esta clase.
# =============================================================================

from abc import ABC, abstractmethod
from datetime import datetime
from excepciones.excepciones_personalizadas import ParametroFaltanteError


class EntidadBase(ABC):
    """
    Clase abstracta que representa cualquier entidad general del sistema SIGRES.

    Define la estructura mínima que deben cumplir todas las entidades,
    garantizando abstracción, encapsulación y un contrato común.

    Atributos:
        __id (int)              : Identificador único autogenerado.
        __fecha_creacion (str)  : Fecha y hora de creación de la entidad.
        __activo (bool)         : Estado activo/inactivo de la entidad.
    """

    _contador_id = 0  # Contador global para autogenerar IDs únicos

    def __init__(self, nombre: str):
        """
        Constructor base. Valida que el nombre no esté vacío
        y asigna ID y fecha de creación automáticamente.

        Args:
            nombre (str): Nombre descriptivo de la entidad.

        Raises:
            ParametroFaltanteError: Si el nombre está vacío o es None.
        """
        if not nombre or not nombre.strip():
            raise ParametroFaltanteError("nombre")

        EntidadBase._contador_id += 1
        self.__id = EntidadBase._contador_id
        self.__nombre = nombre.strip()
        self.__fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__activo = True

    # ─────────────────────────────────────────
    #  GETTERS (Encapsulación)
    # ─────────────────────────────────────────

    @property
    def id(self) -> int:
        """Retorna el ID único de la entidad."""
        return self.__id

    @property
    def nombre(self) -> str:
        """Retorna el nombre de la entidad."""
        return self.__nombre

    @property
    def fecha_creacion(self) -> str:
        """Retorna la fecha y hora de creación."""
        return self.__fecha_creacion

    @property
    def activo(self) -> bool:
        """Retorna True si la entidad está activa."""
        return self.__activo

    # ─────────────────────────────────────────
    #  SETTERS (Encapsulación con validación)
    # ─────────────────────────────────────────

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        """
        Actualiza el nombre de la entidad con validación.

        Raises:
            ParametroFaltanteError: Si el nuevo nombre está vacío.
        """
        if not nuevo_nombre or not nuevo_nombre.strip():
            raise ParametroFaltanteError("nombre")
        self.__nombre = nuevo_nombre.strip()

    @activo.setter
    def activo(self, estado: bool):
        """Actualiza el estado activo/inactivo de la entidad."""
        self.__activo = estado

    # ─────────────────────────────────────────
    #  MÉTODOS ABSTRACTOS (Contrato obligatorio)
    # ─────────────────────────────────────────

    @abstractmethod
    def mostrar_info(self) -> str:
        """
        Muestra la información detallada de la entidad.
        Cada clase hija debe implementar su propia versión.
        """
        pass

    @abstractmethod
    def validar(self) -> bool:
        """
        Valida que los datos de la entidad sean correctos y completos.
        Cada clase hija define sus propias reglas de validación.

        Returns:
            bool: True si los datos son válidos.

        Raises:
            Exception: Si algún dato no cumple las validaciones.
        """
        pass

    # ─────────────────────────────────────────
    #  MÉTODOS COMUNES (Heredados por todos)
    # ─────────────────────────────────────────

    def desactivar(self):
        """Desactiva la entidad del sistema."""
        self.__activo = False

    def activar(self):
        """Reactiva la entidad en el sistema."""
        self.__activo = True

    def __str__(self) -> str:
        """Representación en cadena de la entidad."""
        estado = "Activo" if self.__activo else "Inactivo"
        return (f"[ID: {self.__id}] {self.__nombre} | "
                f"Creado: {self.__fecha_creacion} | Estado: {estado}")

    def __repr__(self) -> str:
        """Representación técnica de la entidad."""
        return f"{self.__class__.__name__}(id={self.__id}, nombre='{self.__nombre}')"

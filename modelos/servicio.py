# =============================================================================
# SIGRES - Software FJ
# Archivo: modelos/servicio.py
# Responsable: David
# Descripción: Clase abstracta Servicio. Base de todos los servicios
#              especializados del sistema.
# =============================================================================

from abc import abstractmethod
from modelos.entidad_base import EntidadBase
from excepciones.excepciones_personalizadas import (
    ServicioInvalidoError,
    CalculoInconsistenteError
)
from utils.logger import log_info, log_warning, log_error


class Servicio(EntidadBase):
    """
    Clase abstracta que representa un servicio genérico de Software FJ.
    Todas las clases de servicio especializadas deben heredar de esta.

    Implementa:
        - Polimorfismo mediante métodos abstractos sobrescritos en hijos.
        - Sobrecarga simulada de calcular_costo() con parámetros opcionales.
        - Validaciones y manejo de excepciones.
    """

    def __init__(self, nombre: str, precio_base: float):
        """
        Constructor del servicio.

        Args:
            nombre      (str)  : Nombre del servicio.
            precio_base (float): Precio base del servicio.

        Raises:
            ServicioInvalidoError: Si el precio base es negativo o cero.
            ParametroFaltanteError: Si el nombre está vacío.
        """
        super().__init__(nombre)
        if precio_base is None or precio_base <= 0:
            raise ServicioInvalidoError(
                f"El precio base del servicio '{nombre}' debe ser mayor a cero."
            )
        self.__precio_base = precio_base
        self.__disponible = True

    # ─────────────────────────────────────────
    #  GETTERS Y SETTERS
    # ─────────────────────────────────────────

    @property
    def precio_base(self) -> float:
        return self.__precio_base

    @precio_base.setter
    def precio_base(self, nuevo_precio: float):
        if nuevo_precio <= 0:
            raise ServicioInvalidoError("El precio base debe ser mayor a cero.")
        self.__precio_base = nuevo_precio

    @property
    def disponible(self) -> bool:
        return self.__disponible

    @disponible.setter
    def disponible(self, estado: bool):
        self.__disponible = estado

    # ─────────────────────────────────────────
    #  MÉTODOS ABSTRACTOS (Contrato obligatorio)
    # ─────────────────────────────────────────

    @abstractmethod
    def calcular_costo(self, duracion: float, impuesto: float = 0, descuento: float = 0) -> float:
        """
        Calcula el costo del servicio según la duración.
        Simula sobrecarga con parámetros opcionales:
            - Sin extras         : calcular_costo(duracion)
            - Con impuesto       : calcular_costo(duracion, impuesto=0.19)
            - Con descuento      : calcular_costo(duracion, descuento=0.10)
            - Con ambos          : calcular_costo(duracion, impuesto=0.19, descuento=0.10)

        Raises:
            CalculoInconsistenteError: Si impuesto < 0 o descuento > 1.
        """
        pass

    @abstractmethod
    def describir_servicio(self) -> str:
        """
        Retorna una descripción detallada y específica del servicio.
        Cada clase hija implementa su propia versión.
        """
        pass

    @abstractmethod
    def validar_parametros(self) -> bool:
        """
        Valida los parámetros específicos de cada tipo de servicio.
        Cada clase hija define sus propias reglas.
        """
        pass

    # ─────────────────────────────────────────
    #  MÉTODO VALIDAR (Implementación del abstracto de EntidadBase)
    # ─────────────────────────────────────────

    def validar(self) -> bool:
        """
        Implementa el método abstracto de EntidadBase.
        Delega la validación específica a validar_parametros().
        """
        return self.validar_parametros()

    # ─────────────────────────────────────────
    #  MÉTODO MOSTRAR INFO (Implementación del abstracto de EntidadBase)
    # ─────────────────────────────────────────

    def mostrar_info(self) -> str:
        estado = "Disponible" if self.__disponible else "No disponible"
        return (
            f"[Servicio ID: {self.id}] "
            f"{self.describir_servicio()} | "
            f"Estado: {estado}"
        )

    # ─────────────────────────────────────────
    #  VALIDACIÓN DE PARÁMETROS DE CÁLCULO
    # ─────────────────────────────────────────

    def _validar_calculo(self, impuesto: float, descuento: float):
        """
        Valida los parámetros de cálculo antes de aplicarlos.
        Método protegido compartido por todos los servicios hijos.

        Raises:
            CalculoInconsistenteError: Si los valores son inválidos.
        """
        if impuesto < 0:
            raise CalculoInconsistenteError(
                f"El impuesto no puede ser negativo. Valor recibido: {impuesto}"
            )
        if descuento < 0 or descuento > 1:
            raise CalculoInconsistenteError(
                f"El descuento debe estar entre 0 y 1. Valor recibido: {descuento}"
            )

    def __str__(self) -> str:
        return self.mostrar_info()

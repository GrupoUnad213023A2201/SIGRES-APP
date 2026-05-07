# =============================================================================
# SIGRES - Software FJ
# Archivo: main.py
# Descripción: Punto de entrada del sistema. Incluye menú principal
#              y 10 simulaciones de operaciones válidas e inválidas.
# =============================================================================

from utils.logger import log_info, log_warning, log_error
from excepciones.excepciones_personalizadas import (
    ClienteInvalidoError, ClienteNoEncontradoError,
    ServicioInvalidoError, ServicioNoDisponibleError,
    ReservaInvalidaError, ReservaYaCanceladaError,
    ReservaYaConfirmadaError, ParametroFaltanteError,
    CalculoInconsistenteError, OperacionNoPermitidaError
)
from modelos.cliente import Cliente
from modelos.reserva import Reserva
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria_especializada import AsesoriaEspecializada


# ─────────────────────────────────────────
#  LISTAS GLOBALES EN MEMORIA
# ─────────────────────────────────────────

clientes = []
servicios = []
reservas = []


# =============================================================================
#  SECCIÓN 1: GESTIÓN DE CLIENTES
# =============================================================================

def menu_clientes():
    while True:
        print("\n╔══════════════════════════════╗")
        print("║     GESTIÓN DE CLIENTES      ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Agregar cliente           ║")
        print("║ 2. Listar clientes           ║")
        print("║ 3. Buscar cliente            ║")
        print("║ 0. Volver                    ║")
        print("╚══════════════════════════════╝")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "0":
            break
        else:
            print("⚠️  Opción inválida.")


def agregar_cliente():
    try:
        nombre = input("Nombre: ").strip()
        correo = input("Correo: ").strip()
        telefono = input("Teléfono: ").strip()
        cliente = Cliente(nombre, correo, telefono)
        cliente.validar()
        clientes.append(cliente)
        log_info(f"Cliente '{nombre}' registrado exitosamente con ID {cliente.id}.")
        print(f"✅ Cliente registrado: {cliente}")
    except (ClienteInvalidoError, ParametroFaltanteError) as e:
        log_error(str(e))
        print(f"❌ Error al registrar cliente: {e}")
    except Exception as e:
        log_error(f"Error inesperado al agregar cliente: {e}")
        print(f"❌ Error inesperado: {e}")


def listar_clientes():
    if not clientes:
        print("ℹ️  No hay clientes registrados.")
        return
    print("\n── Clientes registrados ──")
    for c in clientes:
        print(f"  {c.mostrar_info()}")


def buscar_cliente():
    try:
        termino = input("Ingrese ID o nombre del cliente: ").strip()
        resultado = [c for c in clientes
                     if str(c.id) == termino or termino.lower() in c.nombre.lower()]
        if not resultado:
            raise ClienteNoEncontradoError(termino)
        for c in resultado:
            print(f"  {c.mostrar_info()}")
        log_info(f"Búsqueda de cliente '{termino}': {len(resultado)} resultado(s).")
    except ClienteNoEncontradoError as e:
        log_warning(str(e))
        print(f"⚠️  {e}")


# =============================================================================
#  SECCIÓN 2: GESTIÓN DE SERVICIOS
# =============================================================================

def menu_servicios():
    while True:
        print("\n╔══════════════════════════════╗")
        print("║     GESTIÓN DE SERVICIOS     ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Agregar servicio          ║")
        print("║ 2. Listar servicios          ║")
        print("║ 0. Volver                    ║")
        print("╚══════════════════════════════╝")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            agregar_servicio()
        elif opcion == "2":
            listar_servicios()
        elif opcion == "0":
            break
        else:
            print("⚠️  Opción inválida.")


def agregar_servicio():
    try:
        print("\nTipos de servicio:")
        print("  1. Reserva de Sala")
        print("  2. Alquiler de Equipo")
        print("  3. Asesoría Especializada")
        tipo = input("Seleccione tipo: ").strip()

        nombre = input("Nombre del servicio: ").strip()

        if tipo == "1":
            capacidad = int(input("Capacidad (personas): "))
            precio_hora = float(input("Precio por hora: "))
            servicio = ReservaSala(nombre, capacidad, precio_hora)
        elif tipo == "2":
            tipo_equipo = input("Tipo de equipo: ").strip()
            precio_dia = float(input("Precio por día: "))
            servicio = AlquilerEquipo(nombre, tipo_equipo, precio_dia)
        elif tipo == "3":
            especialidad = input("Especialidad: ").strip()
            precio_hora = float(input("Precio por hora: "))
            servicio = AsesoriaEspecializada(nombre, especialidad, precio_hora)
        else:
            raise OperacionNoPermitidaError("Tipo de servicio no válido.")

        servicio.validar()
        servicios.append(servicio)
        log_info(f"Servicio '{nombre}' agregado exitosamente con ID {servicio.id}.")
        print(f"✅ Servicio registrado: {servicio}")

    except (ServicioInvalidoError, ParametroFaltanteError, OperacionNoPermitidaError) as e:
        log_error(str(e))
        print(f"❌ Error al registrar servicio: {e}")
    except ValueError as e:
        log_error(f"Valor numérico inválido al crear servicio: {e}")
        print(f"❌ Valor inválido: {e}")
    except Exception as e:
        log_error(f"Error inesperado al agregar servicio: {e}")
        print(f"❌ Error inesperado: {e}")


def listar_servicios():
    if not servicios:
        print("ℹ️  No hay servicios registrados.")
        return
    print("\n── Servicios registrados ──")
    for s in servicios:
        print(f"  {s.describir_servicio()}")


# =============================================================================
#  SECCIÓN 3: GESTIÓN DE RESERVAS
# =============================================================================

def menu_reservas():
    while True:
        print("\n╔══════════════════════════════╗")
        print("║     GESTIÓN DE RESERVAS      ║")
        print("╠══════════════════════════════╣")
        print("║ 1. Crear reserva             ║")
        print("║ 2. Listar reservas           ║")
        print("║ 3. Confirmar reserva         ║")
        print("║ 4. Cancelar reserva          ║")
        print("║ 0. Volver                    ║")
        print("╚══════════════════════════════╝")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            crear_reserva()
        elif opcion == "2":
            listar_reservas()
        elif opcion == "3":
            confirmar_reserva()
        elif opcion == "4":
            cancelar_reserva()
        elif opcion == "0":
            break
        else:
            print("⚠️  Opción inválida.")


def crear_reserva():
    try:
        cliente_id = int(input("ID del cliente: "))
        servicio_id = int(input("ID del servicio: "))
        fecha = input("Fecha (YYYY-MM-DD): ").strip()
        hora = input("Hora (HH:MM): ").strip()
        duracion = float(input("Duración (en horas): "))

        cliente = next((c for c in clientes if c.id == cliente_id), None)
        if not cliente:
            raise ClienteNoEncontradoError(cliente_id)

        servicio = next((s for s in servicios if s.id == servicio_id), None)
        if not servicio:
            raise ServicioNoDisponibleError(f"ID {servicio_id}")

        reserva = Reserva(cliente, servicio, fecha, hora, duracion)
        reservas.append(reserva)
        log_info(f"Reserva creada: Cliente '{cliente.nombre}' - Servicio '{servicio.nombre}'.")
        print(f"✅ Reserva creada exitosamente:\n  {reserva.mostrar_info()}")

    except (ClienteNoEncontradoError, ServicioNoDisponibleError,
            ReservaInvalidaError, ParametroFaltanteError) as e:
        log_error(str(e))
        print(f"❌ Error al crear reserva: {e}")
    except ValueError as e:
        log_error(f"Valor inválido al crear reserva: {e}")
        print(f"❌ Valor inválido: {e}")
    except Exception as e:
        log_error(f"Error inesperado al crear reserva: {e}")
        print(f"❌ Error inesperado: {e}")


def listar_reservas():
    if not reservas:
        print("ℹ️  No hay reservas registradas.")
        return
    print("\n── Reservas registradas ──")
    for r in reservas:
        print(f"  {r.mostrar_info()}")


def confirmar_reserva():
    try:
        reserva_id = int(input("ID de la reserva a confirmar: "))
        reserva = next((r for r in reservas if r.id == reserva_id), None)
        if not reserva:
            raise ReservaInvalidaError(f"Reserva con ID '{reserva_id}' no encontrada.")
        reserva.confirmar()
        log_info(f"Reserva ID {reserva_id} confirmada exitosamente.")
        print(f"✅ Reserva confirmada.")
    except (ReservaInvalidaError, ReservaYaConfirmadaError) as e:
        log_warning(str(e))
        print(f"⚠️  {e}")
    except Exception as e:
        log_error(f"Error inesperado al confirmar reserva: {e}")
        print(f"❌ Error inesperado: {e}")


def cancelar_reserva():
    try:
        reserva_id = int(input("ID de la reserva a cancelar: "))
        reserva = next((r for r in reservas if r.id == reserva_id), None)
        if not reserva:
            raise ReservaInvalidaError(f"Reserva con ID '{reserva_id}' no encontrada.")
        reserva.cancelar()
        log_info(f"Reserva ID {reserva_id} cancelada exitosamente.")
        print(f"✅ Reserva cancelada.")
    except (ReservaInvalidaError, ReservaYaCanceladaError) as e:
        log_warning(str(e))
        print(f"⚠️  {e}")
    except Exception as e:
        log_error(f"Error inesperado al cancelar reserva: {e}")
        print(f"❌ Error inesperado: {e}")


#
# =============================================================================
#  MENÚ PRINCIPAL
# =============================================================================

def menu_principal():
    log_info("Sistema SIGRES iniciado.")
    while True:
        print("\n╔══════════════════════════════════════╗")
        print("║     SIGRES - Software FJ             ║")
        print("║  Sistema de Gestión de Reservas      ║")
        print("╠══════════════════════════════════════╣")
        print("║  1. Gestión de Clientes              ║")
        print("║  2. Gestión de Servicios             ║")
        print("║  3. Gestión de Reservas              ║")
        print("║  0. Salir                            ║")
        print("╚══════════════════════════════════════╝")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_servicios()
        elif opcion == "3":
            menu_reservas()
        elif opcion == "0":
            log_info("Sistema SIGRES cerrado correctamente.")
            print("\n👋 ¡Hasta luego! Sistema SIGRES cerrado.")
            break
        else:
            print(" Opción inválida. Intente de nuevo.")


# =============================================================================
#  PUNTO DE ENTRADA
# =============================================================================

if __name__ == "__main__":
    menu_principal()

#=============================================================================
#  SECCIÓN 4: SIMULACIONES (10 operaciones obligatorias)
# =============================================================================

def ejecutar_simulaciones():
    print("\n" + "=" * 60)
    print("   SIMULACIONES DEL SISTEMA - Software FJ")
    print("=" * 60)
    log_info("Inicio de simulaciones del sistema SIGRES.")

    # ── Simulación 1: Cliente válido ──────────────────────────────
    print("\n▶ Simulación 1: Registrar cliente válido")
    try:
        c1 = Cliente("Ana Torres", "ana@softwarefj.com", "3001234567")
        c1.validar()
        clientes.append(c1)
        log_info(f"[SIM-1] Cliente '{c1.nombre}' registrado correctamente.")
        print(f"  ✅ {c1.mostrar_info()}")
    except Exception as e:
        log_error(f"[SIM-1] {e}")
        print(f"  ❌ {e}")

    # ── Simulación 2: Cliente con correo inválido ─────────────────
    print("\n▶ Simulación 2: Cliente con correo inválido")
    try:
        c2 = Cliente("Pedro Ruiz", "correo-sin-arroba", "3009876543")
        c2.validar()
        clientes.append(c2)
    except ClienteInvalidoError as e:
        log_error(f"[SIM-2] {e}")
        print(f"  ❌ Error esperado: {e}")

    # ── Simulación 3: Cliente con nombre vacío ────────────────────
    print("\n▶ Simulación 3: Cliente con nombre vacío")
    try:
        c3 = Cliente("", "valido@email.com", "3001111111")
        c3.validar()
        clientes.append(c3)
    except (ClienteInvalidoError, ParametroFaltanteError) as e:
        log_error(f"[SIM-3] {e}")
        print(f"  ❌ Error esperado: {e}")

    # ── Simulación 4: Crear ReservaSala válida ────────────────────
    print("\n▶ Simulación 4: Crear servicio ReservaSala válido")
    try:
        s1 = ReservaSala("Sala Innovación", 10, 50000)
        s1.validar()
        servicios.append(s1)
        log_info(f"[SIM-4] Servicio '{s1.nombre}' creado correctamente.")
        print(f"  ✅ {s1.describir_servicio()}")
    except Exception as e:
        log_error(f"[SIM-4] {e}")
        print(f"  ❌ {e}")

    # ── Simulación 5: Crear AlquilerEquipo válido ─────────────────
    print("\n▶ Simulación 5: Crear servicio AlquilerEquipo válido")
    try:
        s2 = AlquilerEquipo("Portátil HP", "Computador", 35000)
        s2.validar()
        servicios.append(s2)
        log_info(f"[SIM-5] Servicio '{s2.nombre}' creado correctamente.")
        print(f"  ✅ {s2.describir_servicio()}")
    except Exception as e:
        log_error(f"[SIM-5] {e}")
        print(f"  ❌ {e}")

    # ── Simulación 6: Crear AsesoriaEspecializada válida ──────────
    print("\n▶ Simulación 6: Crear servicio AsesoriaEspecializada válido")
    try:
        s3 = AsesoriaEspecializada("Consultoría TI", "Tecnología", 120000)
        s3.validar()
        servicios.append(s3)
        log_info(f"[SIM-6] Servicio '{s3.nombre}' creado correctamente.")
        print(f"  ✅ {s3.describir_servicio()}")
    except Exception as e:
        log_error(f"[SIM-6] {e}")
        print(f"  ❌ {e}")

    # ── Simulación 7: Servicio con parámetros inválidos ───────────
    print("\n▶ Simulación 7: Servicio con precio negativo")
    try:
        s4 = ReservaSala("Sala Error", 5, -1000)
        s4.validar()
        servicios.append(s4)
    except ServicioInvalidoError as e:
        log_error(f"[SIM-7] {e}")
        print(f"  ❌ Error esperado: {e}")

    # ── Simulación 8: Reserva exitosa con costo + impuesto ────────
    print("\n▶ Simulación 8: Reserva exitosa con cálculo de costo e impuesto")
    try:
        r1 = Reserva(clientes[0], servicios[0], "2026-06-01", "09:00", 3)
        r1.confirmar()
        costo = servicios[0].calcular_costo(3, impuesto=0.19)
        reservas.append(r1)
        log_info(f"[SIM-8] Reserva creada y confirmada. Costo total: ${costo:,.0f}")
        print(f"  ✅ Reserva confirmada. Costo con 19% IVA: ${costo:,.0f}")
    except Exception as e:
        log_error(f"[SIM-8] {e}")
        print(f"  ❌ {e}")

    # ── Simulación 9: Reserva con cliente inexistente ─────────────
    print("\n▶ Simulación 9: Reserva con cliente inexistente")
    try:
        cliente_falso = next((c for c in clientes if c.id == 9999), None)
        if not cliente_falso:
            raise ClienteNoEncontradoError(9999)
        r2 = Reserva(cliente_falso, servicios[0], "2026-06-02", "10:00", 2)
        reservas.append(r2)
    except ClienteNoEncontradoError as e:
        log_error(f"[SIM-9] {e}")
        print(f"  ❌ Error esperado: {e}")

    # ── Simulación 10: Cancelar reserva ya cancelada ──────────────
    print("\n▶ Simulación 10: Cancelar reserva ya cancelada")
    try:
        reservas[0].cancelar()  # Primera cancelación
        reservas[0].cancelar()  # Segunda cancelación → debe fallar
    except ReservaYaCanceladaError as e:
        log_error(f"[SIM-10] {e}")
        print(f"  ❌ Error esperado: {e}")

    print("\n" + "=" * 60)
    print("   ✅ Simulaciones completadas. Revisa logs/sigres.log")
    print("=" * 60)
    log_info("Simulaciones del sistema SIGRES finalizadas.")


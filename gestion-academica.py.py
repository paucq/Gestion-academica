# ============================================================
# Parcial 1 - Paula Andrea Calderon Quintero
# Sistema: Finalización de semestre y Admisión
# ============================================================

# --- Constantes ---
PROGRAMAS = ("Sistemas", "Telecomunicaciones")
GENEROS_VALIDOS = {"M", "F"}
EDAD_MINIMA = 14
EDAD_MAXIMA = 80
CANTIDAD_NOTAS = 5
NOTA_MINIMA = 0.0
NOTA_MAXIMA = 5.0


# --- Funciones de validación y entrada ---

def leer_entero(mensaje, minimo=None, maximo=None):
    """Solicita un entero válido dentro de un rango opcional."""
    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("  Error: no puede estar vacío.")
            continue
        try:
            valor = int(entrada)
        except ValueError:
            print("  Error: debe ingresar un número entero.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  Error: el valor mínimo es {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"  Error: el valor máximo es {maximo}.")
            continue
        return valor


def leer_decimal(mensaje, minimo=None, maximo=None):
    """Solicita un número decimal válido dentro de un rango opcional."""
    while True:
        entrada = input(mensaje).strip()
        if not entrada:
            print("  Error: no puede estar vacío.")
            continue
        try:
            valor = float(entrada)
        except ValueError:
            print("  Error: debe ingresar un número válido.")
            continue
        if minimo is not None and valor < minimo:
            print(f"  Error: el valor mínimo es {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"  Error: el valor máximo es {maximo}.")
            continue
        return valor


def pedir_programa():
    """Solicita y valida el programa académico."""
    print(f"  Programas disponibles: {', '.join(PROGRAMAS)}")
    while True:
        entrada = input("  Programa académico: ").strip().capitalize()
        if entrada in PROGRAMAS:
            return entrada
        print(f"  Error: programa inválido. Opciones: {', '.join(PROGRAMAS)}")


def pedir_genero():
    """Solicita y valida el género (M/F)."""
    while True:
        entrada = input("  Género (M/F): ").strip().upper()
        if entrada in GENEROS_VALIDOS:
            return entrada
        print("  Error: ingrese M o F.")


def pedir_nombre():
    """Solicita el nombre del aspirante."""
    while True:
        nombre = input("  Nombre: ").strip()
        if nombre:
            return nombre.title()
        print("  Error: el nombre no puede estar vacío.")


def pedir_edad():
    """Solicita una edad válida."""
    return leer_entero("  Edad: ", minimo=EDAD_MINIMA, maximo=EDAD_MAXIMA)


def pedir_notas():
    """Solicita 5 notas válidas y retorna la lista."""
    notas = []
    for i in range(1, CANTIDAD_NOTAS + 1):
        nota = leer_decimal(f"    Nota {i}: ", minimo=NOTA_MINIMA, maximo=NOTA_MAXIMA)
        notas.append(nota)
    return notas


# --- Estructuras de datos iniciales ---

def crear_datos_semestre():
    """Crea el diccionario acumulador para finalización de semestre."""
    return {
        programa: {
            "hombres": 0,
            "mujeres": 0,
            "total_estudiantes": 0,
            "suma_promedios": 0.0
        }
        for programa in PROGRAMAS
    }


def crear_datos_admision():
    """Crea el diccionario acumulador para admisión."""
    return {
        "total": 0,
        "hombres": 0,
        "mujeres": 0,
        "suma_edades": 0,
        "nombres": []
    }


# --- Menú ---

def mostrar_menu():
    print("\n" + "=" * 45)
    print("   SISTEMA DE GESTIÓN ACADÉMICA")
    print("=" * 45)
    print("  1. Finalización de semestre")
    print("  2. Proceso de admisión")
    print("  3. Salir")
    print("-" * 45)


# --- Proceso 1: Finalización de semestre ---

def procesar_finalizacion_semestre(semestre):
    """Registra estudiantes y acumula resultados por programa."""
    print("\n--- FINALIZACIÓN DE SEMESTRE ---")
    cantidad = leer_entero("Cantidad de alumnos a registrar: ", minimo=1)

    for i in range(1, cantidad + 1):
        print(f"\n>> Estudiante {i} de {cantidad}")
        programa = pedir_programa()
        genero = pedir_genero()
        print("  Ingrese las 5 notas:")
        notas = pedir_notas()

        # Calcular promedio individual
        promedio = sum(notas) / CANTIDAD_NOTAS

        # Acumular en el diccionario del programa
        datos = semestre[programa]
        if genero == "M":
            datos["hombres"] += 1
        else:
            datos["mujeres"] += 1
        datos["total_estudiantes"] += 1
        datos["suma_promedios"] += promedio

        print(f"  -> Promedio del estudiante: {promedio:.2f}")

    print("\nRegistro de semestre completado.")
    mostrar_reporte_semestre(semestre)


# --- Proceso 2: Admisión ---

def procesar_admision(admision):
    """Registra aspirantes de forma continua hasta que el usuario decida parar."""
    print("\n--- PROCESO DE ADMISIÓN ---")

    while True:
        print(f">> Aspirante #{admision['total'] + 1}")
        nombre = pedir_nombre()
        genero = pedir_genero()
        edad = pedir_edad()

        # Acumular datos
        admision["total"] += 1
        admision["suma_edades"] += edad
        admision["nombres"].append(nombre)
        if genero == "M":
            admision["hombres"] += 1
        else:
            admision["mujeres"] += 1

        print("  Aspirante registrado.")

        # Preguntar si desea continuar
        continuar = input("\n¿Desea registrar otro aspirante? (si/no): ").strip().lower()
        if continuar == "no":
            break
        print()

    print("\nRegistro de admisión completado.")
    mostrar_reporte_admision(admision)


# --- Reportes ---

def mostrar_reporte_semestre(semestre):
    """Muestra el reporte acumulado de finalización de semestre."""
    print("\n--- REPORTE: FINALIZACIÓN DE SEMESTRE ---")

    hay_datos = False
    for programa in PROGRAMAS:
        datos = semestre[programa]
        if datos["total_estudiantes"] == 0:
            continue
        hay_datos = True
        promedio_general = datos["suma_promedios"] / datos["total_estudiantes"]
        print(f"\n  Programa: {programa}")
        print(f"    Hombres:          {datos['hombres']}")
        print(f"    Mujeres:          {datos['mujeres']}")
        print(f"    Total estudiantes: {datos['total_estudiantes']}")
        print(f"    Promedio general:  {promedio_general:.2f}")

    if not hay_datos:
        print("  No hay datos registrados aún.")


def mostrar_reporte_admision(admision):
    """Muestra el reporte acumulado de admisión."""
    print("\n--- REPORTE: PROCESO DE ADMISIÓN ---")

    if admision["total"] == 0:
        print("  No hay datos registrados aún.")
        return

    promedio_edad = admision["suma_edades"] / admision["total"]
    print(f"  Total matriculados:  {admision['total']}")
    print(f"  Promedio de edad:    {promedio_edad:.2f}")
    print(f"  Total hombres:       {admision['hombres']}")
    print(f"  Total mujeres:       {admision['mujeres']}")
    print("  Aspirantes registrados:")
    for i, nombre in enumerate(admision["nombres"], 1):
        print(f"    {i}. {nombre}")


# --- Función principal ---

def main():
    semestre = crear_datos_semestre()
    admision = crear_datos_admision()

    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción: ").strip()

        if opcion == "1":
            procesar_finalizacion_semestre(semestre)
        elif opcion == "2":
            procesar_admision(admision)
        elif opcion == "3":
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("\n  Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()

# cli.py
from datetime import datetime
from Clinica import Clinica
from Paciente import Paciente
from Medico import Medico

def mostrar_menu():
    print("\n--- Sistema de Gestión Clínica ---")
    print("1. Agregar paciente")
    print("2. Agregar médico")
    print("3. Agendar turno")
    print("4. Emitir receta")
    print("5. Ver historia clínica")
    print("6. Salir")

def main():
    clinica = Clinica()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            dni = input("DNI del paciente: ")
            fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ")
            try:
                paciente = Paciente(nombre, dni, fecha_nac)
                clinica.agregar_paciente(paciente)
                print("Paciente agregado correctamente.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "2":
            nombre = input("Nombre del médico: ")
            matricula = input("Matrícula del médico: ")
            especialidad = input("Especialidad: ")
            medico = Medico(matricula, nombre, especialidad)
            clinica.agregar_medico(medico)
            print("Médico agregado correctamente.")

        elif opcion == "3":
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            fecha_hora_str = input("Fecha y hora del turno (yyyy-mm-dd HH:MM): ")
            try:
                fecha_hora = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M")
                clinica.agendar_turno(dni, matricula, fecha_hora)
            except ValueError:
                print("Formato de fecha y hora inválido.")

        elif opcion == "4":
            dni = input("DNI del paciente: ")
            matricula = input("Matrícula del médico: ")
            medicamentos = input("Medicamentos (separados por coma): ").split(',')
            medicamentos = [m.strip() for m in medicamentos]
            clinica.emitir_receta(dni, matricula, medicamentos)

        elif opcion == "5":
            dni = input("DNI del paciente: ")
            historia = clinica.obtener_historia_clinica(dni)
            if historia:
                print(historia)
            else:
                print("No se encontró historia clínica para ese DNI.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

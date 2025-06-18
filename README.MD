### Datos Personales
- **Nombre y Apellido**: [Leonel de la Vega]
- **Ciclo Lectivo**: 2025
- **Carrera**: [Ingenieria en Informática]

### Documentación del Sistema Clínica
1. # Cómo ejecutar el sistema

    Preparar el entorno

        Asegúrate de tener Python 3.7+ instalado.

        Ubica todos los archivos .py en un mismo directorio o estructura de paquetes.

        Verifica que las dependencias estándar (datetime, etc.) estén disponibles (vienen con Python).

    Uso desde consola o script

        Importa las clases en un archivo main.py o en la consola interactiva de Python.

        Crea instancias de Paciente, Medico y Clinica.

        Usa los métodos agregar_paciente(), agregar_medico(), agendar_turno(), emitir_receta() para interactuar con la clínica.

    ## Ejemplo básico:

        from datetime import datetime, timedelta
        from Paciente import Paciente
        from Medico import Medico
        from Clinica import Clinica

        clinica = Clinica()
        paciente = Paciente("Juan Pérez", "12345678", "01/01/1990")
        medico = Medico("MAT001", "Dra. López", "Cardiología")

        clinica.agregar_paciente(paciente)
        clinica.agregar_medico(medico)

        fecha_turno = datetime.now() + timedelta(days=2)
        clinica.agendar_turno("12345678", "MAT001", fecha_turno)

        clinica.emitir_receta("12345678", "MAT001", ["Paracetamol 500mg"])

    Ver resultados

        Puedes imprimir turnos o historias clínicas accediendo a los métodos correspondientes (obtener_turnos(), obtener_historia_clinica()).

2. # Cómo ejecutar las pruebas

    Asegúrate de tener los archivos de test

        Por ejemplo, guarda el archivo de tests test_clinica.py en el mismo directorio que las clases.

    Ejecutar tests con unittest

        En la terminal, dentro del directorio del proyecto, corre:

        python -m unittest test_clinica.py

        Esto ejecutará automáticamente todos los tests definidos y mostrará el resultado con resumen de pruebas pasadas/fallidas.

    Interpretar resultados

        OK indica que todos los tests pasaron.

        Si hay fallas, unittest indicará qué test falló y por qué, para que puedas corregir.

3. # Explicación de diseño general

    Clases principales:

        Paciente: Representa un paciente con nombre, DNI y fecha de nacimiento. Valida la fecha con formato dd/mm/aaaa.

        Medico: Representa un médico con matrícula, nombre y especialidad.

        Turno: Representa una cita entre un paciente y un médico en una fecha y hora específicas.

        Receta: Contiene la información de una receta médica, con paciente, médico, lista de medicamentos y fecha.

        HistoriaClinica: Mantiene registros de turnos y recetas asociados a un paciente.

        Clinica: Es el sistema central que administra pacientes, médicos, turnos y la historia clínica. Contiene la lógica para agregar entidades, agendar turnos (con validaciones), y emitir recetas.

    Principios aplicados:

        Encapsulamiento: Atributos privados con métodos públicos para acceso seguro.

        Validación: Se validan datos importantes, como formato de fecha, existencia previa, turno duplicado, y no permitir fechas pasadas.

        Separación de responsabilidades: Cada clase tiene una responsabilidad clara (paciente, médico, turno, receta, clínica).

        Modularidad: Clases divididas en archivos separados, facilitando mantenimiento y extensión.

    Flujo básico del sistema:

        Registrar pacientes y médicos en la clínica.

        Agendar turnos verificando disponibilidad y validez.

        Emitir recetas vinculadas a pacientes y médicos.

        Consultar historias clínicas para obtener todos los turnos y recetas asociadas a un paciente.

4. # Como ejecutar Cli 
Ejecución del sistema

    Asegurate de tener todos los archivos .py en el mismo directorio.

    Abrí una terminal en ese directorio.

    Ejecutá:

python cli.py
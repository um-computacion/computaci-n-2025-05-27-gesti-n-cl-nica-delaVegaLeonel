from errores import PacienteNoExisteError, MedicoNoExisteError, TurnoDuplicadoError
from Paciente import Paciente as paciente
from datetime import datetime

class GestorTurnos:
    def __init__(self):
        self.pacientes = {}   
        self.medicos = set()  
        self.turnos = set()   

    def registrar_paciente(self, paciente: paciente):
        self.pacientes[paciente.obtener_dni()] = paciente

    def registrar_medico(self, nombre: str):
        self.medicos.add(nombre)

    def asignar_turno(self, dni: str, medico: str, fecha: datetime):
        if dni not in self.pacientes:
            raise PacienteNoExisteError(f"Paciente con DNI {dni} no existe.")
        if medico not in self.medicos:
            raise MedicoNoExisteError(f"Médico '{medico}' no está registrado.")
        clave = (dni, medico, fecha)
        if clave in self.turnos:
            raise TurnoDuplicadoError("El turno ya está registrado.")
        self.turnos.add(clave)

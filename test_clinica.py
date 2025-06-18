import unittest
from datetime import datetime, timedelta
from Paciente import Paciente
from Medico import Medico
from Clinica import Clinica

class TestClinica(unittest.TestCase):

    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan Pérez", "12345678", "01/01/1990")
        self.medico = Medico("MAT001", "Dra. López", "Cardiología")
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_agregar_paciente_repetido(self):
        # Agregar paciente con DNI ya registrado no lo duplica
        self.clinica.agregar_paciente(self.paciente)
        self.assertEqual(len(self.clinica._pacientes), 1)

    def test_agregar_medico_repetido(self):
        # Agregar médico con matrícula ya registrada no lo duplica
        self.clinica.agregar_medico(self.medico)
        self.assertEqual(len(self.clinica._medicos), 1)

    def test_agendar_turno_exitoso(self):
        fecha_turno = datetime.now() + timedelta(days=1)
        self.clinica.agendar_turno("12345678", "MAT001", fecha_turno)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)
        self.assertEqual(turnos[0]._paciente.obtener_dni(), "12345678")
        self.assertEqual(turnos[0]._medico.obtener_matricula(), "MAT001")

    def test_agendar_turno_en_pasado(self):
        fecha_pasada = datetime.now() - timedelta(days=1)
        self.clinica.agendar_turno("12345678", "MAT001", fecha_pasada)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 0)

    def test_agendar_turno_medico_no_encontrado(self):
        fecha_turno = datetime.now() + timedelta(days=1)
        self.clinica.agendar_turno("12345678", "MAT999", fecha_turno)
        self.assertEqual(len(self.clinica.obtener_turnos()), 0)

    def test_agendar_turno_paciente_no_encontrado(self):
        fecha_turno = datetime.now() + timedelta(days=1)
        self.clinica.agendar_turno("99999999", "MAT001", fecha_turno)
        self.assertEqual(len(self.clinica.obtener_turnos()), 0)

    def test_turno_duplicado(self):
        fecha_turno = datetime.now() + timedelta(days=1)
        self.clinica.agendar_turno("12345678", "MAT001", fecha_turno)
        # Intento agendar mismo médico y fecha/hora
        self.clinica.agendar_turno("12345678", "MAT001", fecha_turno)
        self.assertEqual(len(self.clinica.obtener_turnos()), 1)

    def test_emitir_receta_exitoso(self):
        medicamentos = ["Paracetamol 500mg", "Ibuprofeno 200mg"]
        self.clinica.emitir_receta("12345678", "MAT001", medicamentos)
        historia = self.clinica.obtener_historia_clinica("12345678")
        self.assertIsNotNone(historia)
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 1)
        self.assertListEqual(recetas[0]._medicamentos, medicamentos)

    def test_emitir_receta_paciente_no_encontrado(self):
        medicamentos = ["Paracetamol 500mg"]
        self.clinica.emitir_receta("99999999", "MAT001", medicamentos)
        historia = self.clinica.obtener_historia_clinica("99999999")
        self.assertIsNone(historia)

    def test_emitir_receta_medico_no_encontrado(self):
        medicamentos = ["Paracetamol 500mg"]
        self.clinica.emitir_receta("12345678", "MAT999", medicamentos)
        historia = self.clinica.obtener_historia_clinica("12345678")
        # No se debe agregar receta si médico no existe
        recetas = historia.obtener_recetas()
        self.assertEqual(len(recetas), 0)

if __name__ == "__main__":
    unittest.main()

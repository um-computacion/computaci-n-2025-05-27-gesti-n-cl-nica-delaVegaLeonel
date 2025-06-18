import unittest
from datetime import datetime
from Paciente import Paciente
from Turno import Turno

class MedicoStub:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Medico: {self.nombre}"

class TestTurno(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Juan Perez", "12345678", "15/04/1990")
        self.medico = MedicoStub("Dr. Smith")
        self.fecha_hora = datetime(2025, 6, 17, 15, 30)
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora)

    def test_obtener_fecha_hora(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)

    def test_str_turno(self):
        esperado = (
            "Turno:\n"
            "  Fecha y hora: 2025-06-17 15:30\n"
            "  Juan Perez, 12345678, 15/04/1990\n"
            "  Medico: Dr. Smith"
        )
        self.assertEqual(str(self.turno), esperado)

if __name__ == "__main__":
    unittest.main()

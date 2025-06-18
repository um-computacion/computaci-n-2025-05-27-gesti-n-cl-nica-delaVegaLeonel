import unittest
from datetime import datetime
from Paciente import Paciente
from Receta import Receta

class MedicoStub:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f"Medico: {self.nombre}"

class TestReceta(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Laura Gomez", "98765432", "20/07/1985")
        self.medico = MedicoStub("Dra. Martinez")
        self.fecha = datetime(2025, 6, 17)
        self.medicamentos = ["Paracetamol 500mg", "Ibuprofeno 200mg"]
        self.receta = Receta(self.paciente, self.medico, self.medicamentos, self.fecha)

    def test_str_receta(self):
        esperado = (
            "Receta:\n"
            "  Fecha: 2025-06-17\n"
            "  Laura Gomez, 98765432, 20/07/1985\n"
            "  Medico: Dra. Martinez\n"
            "  Medicamentos:\n"
            "    - Paracetamol 500mg\n"
            "    - Ibuprofeno 200mg"
        )
        self.assertEqual(str(self.receta), esperado)

if __name__ == "__main__":
    unittest.main()

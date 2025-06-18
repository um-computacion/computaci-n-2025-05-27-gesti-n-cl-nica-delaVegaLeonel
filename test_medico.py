import unittest
from Medico import Medico

class TestMedico(unittest.TestCase):

    def test_creacion_y_obtener_matricula(self):
        m = Medico("12345", "Dr. López", "Cardiología")
        self.assertEqual(m.obtener_matricula(), "12345")
        self.assertEqual(m._nombre, "Dr. López")
        self.assertEqual(m._especialidad, "Cardiología")

    def test_str_medico(self):
        m = Medico("67890", "Dra. Fernández", "Pediatría")
        esperado = "Médico: Dra. Fernández, Matrícula: 67890, Especialidad: Pediatría"
        self.assertEqual(str(m), esperado)

if __name__ == "__main__":
    unittest.main()

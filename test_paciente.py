import unittest
from datetime import datetime, timedelta
from Paciente import Paciente  

class TestPaciente(unittest.TestCase):

    def test_creacion_valida(self):
        p = Paciente("Juan Perez", "12345678", "15/04/1990")
        self.assertEqual(p.nombre, "Juan Perez")
        self.assertEqual(p.obtener_dni(), "12345678")
        self.assertEqual(str(p), "Juan Perez, 12345678, 15/04/1990")

    def test_falta_campos_obligatorios(self):
        with self.assertRaises(ValueError) as cm:
            Paciente("", "12345678", "15/04/1990")
        self.assertEqual(str(cm.exception), "Todos los campos son obligatorios.")

        with self.assertRaises(ValueError) as cm:
            Paciente("Juan Perez", "", "15/04/1990")
        self.assertEqual(str(cm.exception), "Todos los campos son obligatorios.")

        with self.assertRaises(ValueError) as cm:
            Paciente("Juan Perez", "12345678", "")
        self.assertEqual(str(cm.exception), "Todos los campos son obligatorios.")

    def test_fecha_formato_incorrecto(self):
        with self.assertRaises(ValueError) as cm:
            Paciente("Juan Perez", "12345678", "1990-04-15")
        self.assertEqual(str(cm.exception), "La fecha debe estar en formato dd/mm/aaaa.")

        with self.assertRaises(ValueError) as cm:
            Paciente("Juan Perez", "12345678", "31/02/2000")  # fecha inválida
        self.assertEqual(str(cm.exception), "La fecha debe estar en formato dd/mm/aaaa.")

    def test_obtener_dni(self):
        p = Paciente("Ana", "87654321", "01/01/1980")
        self.assertEqual(p.obtener_dni(), "87654321")

    def test_obtener_fecha_hora(self):
        p = Paciente("Ana", "87654321", "01/01/1980")
        ahora = datetime.now()
        fecha_hora_paciente = p.obtener_fecha_hora()
        self.assertIsInstance(fecha_hora_paciente, datetime)
        # Verificamos que la fecha/hora esté dentro de un margen de 2 segundos
        self.assertTrue(abs((ahora - fecha_hora_paciente).total_seconds()) < 2)

if __name__ == "__main__":
    unittest.main()

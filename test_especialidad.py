import unittest
from Especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):

    def test_creacion_valida(self):
        especialidad = Especialidad(
            medicos=["Dr. Pérez", "Dra. Gómez"],
            nombre="Cardiología Avanzada",
            tipo="Cardiología",
            dias=["Lunes", "Miércoles", "Viernes"]
        )
        self.assertEqual(especialidad.obtener_especialidad(), "Cardiología")
        self.assertEqual(especialidad.obtener_nombre(), "Cardiología Avanzada")
        self.assertListEqual(
            especialidad.obtener_medicos(),
            ["Dr. Pérez", "Dra. Gómez"]
        )
        self.assertTrue(especialidad.verificar_dia("lunes"))
        self.assertTrue(especialidad.verificar_dia("Miércoles"))
        self.assertFalse(especialidad.verificar_dia("Domingo"))
        self.assertIn("lunes", str(especialidad).lower())

    def test_creacion_sin_tipo_deberia_fallar(self):
        with self.assertRaises(ValueError) as context:
            Especialidad(medicos=["Dr. Pérez"], nombre="Nombre", tipo="", dias=["Lunes"])
        self.assertEqual(str(context.exception), "La especialidad debe tener un tipo.")

    def test_creacion_con_dias_invalidos_deberia_fallar(self):
        with self.assertRaises(ValueError) as context:
            Especialidad(medicos=["Dr. Pérez"], nombre="Nombre", tipo="Cardio", dias=[])
        self.assertEqual(str(context.exception), "Debe proporcionar una lista de días válida.")

        with self.assertRaises(ValueError):
            Especialidad(medicos=["Dr. Pérez"], nombre="Nombre", tipo="Cardio", dias=["Lunes", 2])

    def test_creacion_con_medicos_invalidos_deberia_fallar(self):
        with self.assertRaises(ValueError) as context:
            Especialidad(medicos=[], nombre="Nombre", tipo="Cardio", dias=["Lunes"])
        self.assertEqual(str(context.exception), "Debe proporcionar una lista de médicos válida.")

        with self.assertRaises(ValueError):
            Especialidad(medicos=["Dr. Pérez", 123], nombre="Nombre", tipo="Cardio", dias=["Lunes"])

    def test_obtener_medicos_devuelve_copia(self):
        medicos = ["Dr. Pérez", "Dra. Gómez"]
        especialidad = Especialidad(medicos, "Nombre", "Tipo", ["Lunes"])
        lista_medicos = especialidad.obtener_medicos()
        lista_medicos.append("Dr. Nuevo")
        # Verificamos que el original no cambió
        self.assertNotIn("Dr. Nuevo", especialidad.obtener_medicos())

if __name__ == "__main__":
    unittest.main()

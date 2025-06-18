import unittest
from Paciente import Paciente
from Historia_Clinica import HistoriaClinica
from datetime import datetime

class TurnoStub:
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

class RecetaStub:
    def __init__(self, descripcion):
        self.descripcion = descripcion

    def __str__(self):
        return self.descripcion

class TestHistoriaClinica(unittest.TestCase):

    def setUp(self):
        self.paciente = Paciente("Carlos Díaz", "55555555", "10/10/1975")
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_y_obtener_turnos(self):
        turno1 = TurnoStub("Turno 1")
        turno2 = TurnoStub("Turno 2")
        self.historia.agregar_turno(turno1)
        self.historia.agregar_turno(turno2)
        turnos = self.historia.obtener_turnos()
        self.assertEqual(len(turnos), 2)
        self.assertIn(turno1, turnos)
        self.assertIn(turno2, turnos)

    def test_agregar_y_obtener_recetas(self):
        receta1 = RecetaStub("Receta A")
        receta2 = RecetaStub("Receta B")
        self.historia.agregar_receta(receta1)
        self.historia.agregar_receta(receta2)
        recetas = self.historia.obtener_recetas()
        self.assertEqual(len(recetas), 2)
        self.assertIn(receta1, recetas)
        self.assertIn(receta2, recetas)

    def test_str_sin_turnos_ni_recetas(self):
        esperado = (
            "Historia Clínica de Carlos Díaz (DNI: 55555555)\n"
            "\nTurnos:\n  No hay turnos registrados."
            "\n\nRecetas:\n  No hay recetas registradas."
        )
        self.assertEqual(str(self.historia), esperado)

    def test_str_con_turnos_y_recetas(self):
        turno = TurnoStub("Turno 1")
        receta = RecetaStub("Receta A")
        self.historia.agregar_turno(turno)
        self.historia.agregar_receta(receta)
        esperado = (
            "Historia Clínica de Carlos Díaz (DNI: 55555555)\n"
            "\nTurnos:\nTurno 1"
            "\n\nRecetas:\nReceta A"
        )
        self.assertEqual(str(self.historia), esperado)

if __name__ == "__main__":
    unittest.main()

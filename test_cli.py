import unittest
from unittest.mock import patch
from io import StringIO
import builtins
import Cli

class TestCLI(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        '1',                        # Opción: Agregar paciente
        'Juan Pérez',              # Nombre
        '12345678',                # DNI
        '01/01/1990',              # Fecha de nacimiento
        '2',                       # Opción: Agregar médico
        'Dr. Gómez',               # Nombre del médico
        'M123',                    # Matrícula
        'Cardiología',             # Especialidad
        '3',                       # Opción: Agendar turno
        '12345678',                # DNI del paciente
        'M123',                    # Matrícula del médico
        '2099-01-01 10:00',        # Fecha y hora del turno
        '5',                       # Ver historia clínica
        '12345678',                # DNI para historia
        '6'                        # Salir
    ])
    @patch('sys.stdout', new_callable=StringIO)
    def test_flujo_completo(self, mock_stdout, mock_input):
        # Ejecutamos el main
        Cli.main()

        salida = mock_stdout.getvalue()

        # Verificamos que el flujo básico se haya ejecutado correctamente
        self.assertIn("Paciente agregado correctamente", salida)
        self.assertIn("Médico agregado correctamente", salida)
        self.assertIn("Turno agendado exitosamente", salida)
        self.assertIn("Historia Clínica de Juan Pérez", salida)

if __name__ == '__main__':
    unittest.main()

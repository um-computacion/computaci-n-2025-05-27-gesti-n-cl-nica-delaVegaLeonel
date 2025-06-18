from Paciente import Paciente
from Turno import Turno
from Receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        self._paciente = paciente
        self._turnos = []   # plural
        self._recetas = []  # plural

    def agregar_turno(self, turno: Turno):
        self._turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        self._recetas.append(receta)

    def obtener_turnos(self) -> list[Turno]:
        return self._turnos

    def obtener_recetas(self) -> list[Receta]:
        return self._recetas

    def __str__(self) -> str:
        turnos_str = '\n'.join(str(turno) for turno in self._turnos)
        recetas_str = '\n'.join(str(receta) for receta in self._recetas)
        return (
            f"Historia Clínica de {self._paciente.nombre} (DNI: {self._paciente.obtener_dni()})\n"
            f"\nTurnos:\n{turnos_str if turnos_str else '  No hay turnos registrados.'}"
            f"\n\nRecetas:\n{recetas_str if recetas_str else '  No hay recetas registradas.'}"
        )


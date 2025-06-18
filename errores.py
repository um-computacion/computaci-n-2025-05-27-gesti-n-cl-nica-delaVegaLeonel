class PacienteNoExisteError(Exception):
    """Se lanza cuando el paciente no está registrado en el sistema."""
    pass

class MedicoNoExisteError(Exception):
    """Se lanza cuando el médico no está registrado en el sistema."""
    pass

class TurnoDuplicadoError(Exception):
    """Se lanza cuando se intenta registrar un turno ya existente."""
    pass



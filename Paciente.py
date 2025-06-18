from datetime import datetime 
class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        if not nombre or not dni or not fecha_nacimiento:
            raise ValueError("Todos los campos son obligatorios.")
        self.nombre = nombre
        self._dni = dni
        
        try:
            datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise ValueError("La fecha debe estar en formato dd/mm/aaaa.")
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self._dni
    
    def obtener_fecha_hora(self) -> datetime:
        return datetime.now()

    def __str__(self) -> str:
        return f"{self.nombre}, {self._dni}, {self.__fecha_nacimiento}"
                                             


class Especialidad:
    def __init__(self, medicos: list[str], nombre: str, tipo: str, dias: list[str]):
        if not tipo:
            raise ValueError("La especialidad debe tener un tipo.")
        if not dias or not all(isinstance(d, str) for d in dias):
            raise ValueError("Debe proporcionar una lista de días válida.")
        if not medicos or not all(isinstance(m, str) for m in medicos):
            raise ValueError("Debe proporcionar una lista de médicos válida.")
        self.__tipo = tipo
        self.__dias = [d.lower() for d in dias]
        self.__nombre = nombre
        self.__medicos = medicos.copy()  # copia para evitar cambios externos

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias

    def __str__(self) -> str:
        dias = ", ".join(self.__dias)
        return f"{self.__tipo} (Días: {dias})"
    
    def obtener_nombre(self) -> str:
        return self.__nombre
    
    def obtener_medicos(self) -> list[str]:
        return self.__medicos.copy()


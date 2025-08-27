class Materia:
    #Constructor
    def __init__(self, nombre: str, codigo: str, creditos: int):
        self.__nombre = nombre
        self.__codigo = codigo
        self.__creditos = creditos

    #getters y setters
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre
    
    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self, nuevo_codigo: str):
        self.__codigo = nuevo_codigo
    
    def get_creditos(self):
        return self.__creditos
    
    def set_creditos(self, nuevos_creditos: int):
        if nuevos_creditos > 0:
            self.__creditos = nuevos_creditos
        else:
            print("los creditos deben ser positivos")
    
    def informacion(self):
        return f"Materia: {self.__nombre}, Código: {self.__codigo}, Créditos: {self.__creditos}."

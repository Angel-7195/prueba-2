class Libro:
    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = True
        self.prestado_a = None

    def __str__(self):
        return f"{self.titulo} ({self.autor})"
    
    def __repr__(self):
        return self.__str__()

    def prestar(self, estudiante):
        if self.disponible:
            self.disponible = False
            self.prestado_a = estudiante
            estudiante.agregar_libro(self)
            return f"Libro '{self.titulo}' prestado a {estudiante.nombre}"
        else:
            return "ya esta prestado"
        
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            self.prestado_a.devolver_libro(self)
            self.prestado_a = None
            return f"Libro '{self.titulo}' devuelto con exito"
        else:
            return "ya esta devuelto"
    
class Estudiante:
    def __init__(self, nombre, ID):
        self.nombre = nombre
        self.ID = ID
        self.libros_prestados = []

    def agregar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
        else:
            return "El estudiante '{self.nombre}' no tiene este libro"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.estudiantes = []

libro1 = Libro("Cien años de soledad", "Gabriel Garcia M", "12345")
estudiante1 = Estudiante("Ana", 1)

print(libro1.prestar(estudiante1))
print(estudiante1.libros_prestados)
print(libro1.devolver())
print(estudiante1.libros_prestados)
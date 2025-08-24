class Libro:
    def __init__(self, titulo, autor, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.disponible = True
        self.prestado_a = None

    def prestar(self, estudiante):
        if self.disponible:
            self.disponible = False
            self.prestado_a = estudiante
            estudiante.agregar_libro(self)
            return f"Libro '{self.titulo}' prestado a {estudiante.nombre}"
        else:
            return f"El libro '{self.titulo}' ya esta prestado"
        
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            self.prestado_a.devolver_libro(self)
            self.prestado_a = None
            return f"Libro '{self.titulo}' devuelto con exito"
        else:
            return f"El libro '{self.titulo}' ya estaba disponible"
    
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
            return f"El estudiante '{self.nombre}' no tiene este libro"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.estudiantes = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_inventario(self):
        if not self.libros:
            print("no hay libros en la biblioteca")
        else:
            print("\n inventario de la biblioteca:")
            for libro in self.libros:
                if libro.disponible:
                    estado = "Disponible"
                else:
                    estado = f"Prestado a {libro.prestado_a.nombre}"
                print(f"- Titulo: {libro.titulo}, Autor: ({libro.autor}), Estado: {estado}")

biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "12345")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "67890")

estudiante1 = Estudiante("Ana", 1)
estudiante2 = Estudiante("Andres", 2)

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_estudiante(estudiante1)
biblioteca.mostrar_inventario()

print(libro1.prestar(estudiante1))
biblioteca.mostrar_inventario()

print(libro2.prestar(estudiante2))
biblioteca.mostrar_inventario()

print(libro1.devolver())
biblioteca.mostrar_inventario()

print(libro2.devolver())
biblioteca.mostrar_inventario()
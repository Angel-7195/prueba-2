class Estudiante:
     def __init__(self, nombre, edad, carrera):
          self.nombre = nombre
          self.edad = edad
          self.carrera = carrera
          self.promedio = 0.0
          self.materias_inscritas = []
          self.notas = {}

     def presentarse(self):
          return( f"Hola, mi nombre es {self.nombre}, "
                  f"tengo {self.edad} años, estudio {self.carrera}, " 
                  f"mi promedio es {self.promedio} y estoy inscrito en "
                  f"{len(self.materias_inscritas)} materias")

     def inscribir_materia(self, materia):
          if materia not in self.materias_inscritas:
               self.materias_inscritas.append(materia)
               print(f"Materia {materia} inscrita con exito")
          else:
               print(f"La materia {materia} ya esta inscrita")

     def mostrar_materias(self):
          if self.materias_inscritas:
               print("Materias inscritas:")
               for materia in self.materias_inscritas:
                    print(f"- {materia}")
          else:
               print("No hay materias inscritas aun")

     def agregar_nota(self, materia, nota):
          if materia in self.materias_inscritas:
               self.notas[materia] = nota
               self.promedio = sum(self.notas.values()) / len(self.notas)
               print(f"nota {nota} agregada a la materia '{materia}'.")
          else:
               print("f no puedes agregar a {materia} porque no esta inscrita")
               
     
estudiante = Estudiante("María González", 20, "Ingeniería de Sistemas")
estudiante.inscribir_materia("Programación I")
estudiante.inscribir_materia("Matemáticas")
estudiante.agregar_nota("Programación I", 4.5)
estudiante.agregar_nota("Matemáticas", 4.2)
print(f"Promedio: {estudiante.promedio}")


print(estudiante.presentarse())
print("Materias inscritas:", estudiante.materias_inscritas)
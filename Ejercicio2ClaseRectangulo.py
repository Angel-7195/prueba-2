class Rectangulo:
    def __init__(self, base, altura):
        if base <= 0 or altura <= 0:
            raise ValueError("la base y la altura deben ser valores positivos")
        self.base = base
        self.altura = altura

    
    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def es_cuadrado(self):
        return self.base == self.altura

    def mostrar_info(self):
        return (f"Rectangulo: \n"
                f"Base: {self.base}\n"
                f"Altura: {self.altura}\n"
                f"Perimetro: {self.calcular_perimetro()}\n")
    
try:
    rect1 = Rectangulo(5, 3)
    rect2 = Rectangulo(4, 4)

    print(rect1.mostrar_info())
    print(f"¿Es cuadrado? {rect1.es_cuadrado()}")
    print(f"¿Es cuadrado? {rect2.es_cuadrado()}")

except ValueError as e:
    print(f"Error: {e}")

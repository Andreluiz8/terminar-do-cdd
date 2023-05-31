class Forma:
    def __init__(self, perimetro, area):
        self.perimetro = perimetro
        self.area = area

class Retangulo(Forma):
    def __init__(self, perimetro, area):
        super().__init__(perimetro, area)

class triangulo(Forma):
    def __init__(self, perimetro, area):
        super().__init__(perimetro, area)


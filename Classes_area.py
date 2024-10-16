class Formas:
    def __init__(self, lado1, lado2):
        self.lado1=lado1
        self.lado2=lado2
    def get_area(self):
        return self.lado1*self.lado2
    def __str__(self):
        return f'A área de {self.__class__.__name__} é: {self.get_area()}'


class Retangulo(Formas):
    pass

class Quadrado(Retangulo):
    def __init__(self, lado):
        super().__init__(lado,lado)

class Triangulo(Formas):
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def get_area(self):
        return(self.lado1*self.lado2/2)


retangulo=Retangulo(2,4)
print(retangulo)

quadrado= Quadrado(2)
print(quadrado)


triangulo=Triangulo(4,4)
print(triangulo)

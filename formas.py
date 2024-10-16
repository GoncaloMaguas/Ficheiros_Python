class formas:
    def __init__(self, lado1, lado2):
        self.lado1=lado1
        self.lado2=lado2

    def get_area(self):
        return self.lado1*self.lado2
    def __str__(self):
        return f'A area de {self.__class__.__name__} e: {self.get_area()}'


class retangulo(formas):
    pass

class quadrado(formas):
    def __init__(self,lado):
        super().__init__(lado,lado)

class triangulo(formas):
    def get_area(self):
        return (self.lado1*self.lado2)/2
        

class circulo(formas):
    def __init__(self,raio):
                super().__init__(raio,raio)
    def get_area(self):
        return (self.lado1*self.lado1)*3.14





q=circulo(5)

print(q)

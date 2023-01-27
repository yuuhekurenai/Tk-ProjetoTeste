# Argumentos *args
def add(*args):
    valor = 0
    for i in args:
        valor += i
    return valor


print(add(20, 50, 50))


# Argumentos kwargs
def calcular(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)


calcular(2, add=3, multiply=5)


class Car:
    def __init__(self, **kwargs):
        # Utilizar .get ao invés de pegar o arqumentos diretamente , não causa erros no tempo de execução caso
        # todos os argumentos não forem chamando, no entanto aparecerá None.
         # self.make = kwargs['make']
        self.make = kwargs.get('make')
        # self.model = kwargs['model']
        self.model = kwargs.get('model')


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)

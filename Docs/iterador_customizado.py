# Escrevendo o nosso itarador personalizado
    
class Contador:
    def __init__(self , menor, maior):
        self.menor = menor
        self.maior = maior
    def __iter__(self):
        return self
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        else:
            raise StopIteration
    

cont = Contador(1, 61)

it = iter(cont)
print(next(it))
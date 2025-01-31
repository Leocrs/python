
# orientação a objeto (POO) - programação orientada a objetos

class Veiculo:
    def movimentar(self):
        print(f' Sou um veiculo e me desloco')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__numero_registro = None

#setter - conjunto

    def set_numero_registro(self, registro):
        self.__numero_registro = registro


#Getter - obter

    def get_fabricante(self):
        print(f" Modelo: {self.__modelo}, Fabricante: {self.__fabricante}.\n" )

    def get_numero_registro(self):
        return self.__numero_registro
    
class Carro(Veiculo):
    def movimentar(self):
        print(f' Ando pelas ruas')

class Moto(Veiculo):
    def movimentar(self):
        print(f' Ando pelas ruas correndo')

class Caminhao(Veiculo):
    def movimentar(self):
        print(f' Viajando pelo Brasil')

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.categoria = categoria
        super().__init__(fabricante, modelo)

if __name__ == '__main__':
    meu_veiculo = Veiculo('Ford', 'Fiesta')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabricante()
    meu_veiculo.get_numero_registro()
    print(f' Registro: {meu_veiculo.get_numero_registro()}\n')

    meu_carro = Carro('WG', 'Golf')
    meu_carro.movimentar()
    meu_carro.get_fabricante()
    print(f' Registro: {meu_carro.get_numero_registro()}\n')

    seu_carro = Carro('BMW', 'X5')
    seu_carro.movimentar()
    seu_carro.get_fabricante()
    print(f' Registro: {seu_carro.get_numero_registro()}\n')

    minha_moto = Moto('Harley Davidson', 'Night 2000')
    minha_moto.movimentar()
    minha_moto.get_fabricante()
    print(f' Registro: {minha_moto.get_numero_registro()}\n')

    meu_caminhao = Caminhao('Volvo', 'FH')
    meu_caminhao.movimentar()
    meu_caminhao.get_fabricante()
    print(f' Registro: {meu_caminhao.get_numero_registro()}\n')

    meu_aviao = Aviao('Boeing', '747', 'Jumbo')
    meu_aviao.movimentar()
    meu_aviao.get_fabricante()
    print(f' Registro: {meu_aviao.get_numero_registro()}\n')

    
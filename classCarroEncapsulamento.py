class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__quilometragem = 0  # Atributo encapsulado com dois underscores "__"

    def dirigir(self, distancia):
        self.__quilometragem += distancia

    def obter_quilometragem(self):
        return self.__quilometragem

# Criando uma instância da classe Carro
meu_carro = Carro("Evoque", "Prisma")

# Acessando os atributos e métodos públicos
print(f"Marca: {meu_carro.marca}")
print(f"Modelo: {meu_carro.modelo}")
meu_carro.dirigir(100)
print(f"Quilometragem: {meu_carro.obter_quilometragem()}")

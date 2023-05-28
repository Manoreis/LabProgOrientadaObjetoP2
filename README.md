# LabProgOrientadaObjetoP2
Repositório criado para a Atividade P2 - Polimorfismo - Herança - Encapsulamento
O polimorfismo na programação orientada a objetos é um princípio que permite que objetos de diferentes classes sejam tratados de maneira semelhante quando possuem comportamentos ou propriedades comuns.
Em outras palavras, é a capacidade de um objeto ser referenciado por meio de uma interface comum, mesmo que seja uma instância de uma classe concreta.
O polimorfismo permite que diferentes objetos respondam à mesma mensagem (método) de maneiras diferentes, dependendo de sua implementação específica. Isso dá flexibilidade ao código, tornando-o mais reutilizável e extensível.
No exemplo simples de polimorfismo que segue para análise é quando temos uma classe "Animal" e suas subclasses "Cachorro" e "Gato". Ambas as subclasses têm um método "emanarSom", mas cada classe implementa esse método de maneira diferente para reproduzir o som característico de um cachorro ou gato e distingui-los. No entanto, pode-se geralmente tratá-los como objetos do tipo "Animal" e chamar o método "emanarSom" para cada um sem se preocupar com diferenças específicas entre as subclasses.
Neste código também está comtemplado a solicitação de Herança!
Observe que as classes "Cachorro" e "Gato" herdam da classe (Herança)"Animal" e implementam o método "emanarSom" de maneira diferente. No entanto, podemos tratá-los como objetos do tipo "Animal" e chamar o método "emanarSom" para cada um sem nos preocuparmos com diferenças específicas de implementação.

Isso é possível graças ao polimorfismo, que permite que objetos de diferentes classes sejam tratados de forma semelhante, com base em uma interface comum.
O encapsulamento é um princípio de programação orientado a objetos que envolve o agrupamento de dados e métodos relacionados em uma unidade chamada classe. Ele protege os dados internos de uma classe permitindo acesso controlado e fornecendo uma interface pública para interagir com esses dados.

O encapsulamento permite que os dados internos de uma classe sejam protegidos e manipulados apenas por métodos específicos, fornecendo controle sobre o acesso e modificação desses dados.

Veja a seguir os exemplos de códigos comtemplando a solicitação do Professor Fabricio Tadeu Dias para a utilização de Polimorfismo, Herança e Encapsulamento:

1º código 

class Animal:
    def emanarSom(self):
        pass

class Cachorro(Animal):
    def emanarSom(self):
        print("O cachorro está latindo!")

class Gato(Animal):
    def emanarSom(self):
        print("O gato está miando!")

# Criando instâncias das classes Cachorro e Gato
cachorro = Cachorro()
gato = Gato()

# Chamando o método emanarSom para cada instância
cachorro.emanarSom()
gato.emanarSom()

Observe que as classes "Cachorro" e "Gato" herdam da classe (Herança) "Animal" e implementam o método "emanarSom" de maneira diferente. No entanto, podemos tratá-los como objetos do tipo "Animal" e chamar o método "emanarSom" para cada um sem nos preocuparmos com diferenças específicas de implementação.

Isso é possibilitado pelo polimorfismo, que permite que objetos de diferentes classes sejam tratados de forma semelhante, com base em uma interface comum.

2º código

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


Neste código, a classe "Carro" encapsula os atributos "marca", "modelo" e "__quilometragem". O atributo " quilometragem" é encapsulado usando dois sublinhados "__ ", tornando-o privado e inacessível diretamente de fora da classe.

Para interagir com a quilometragem, usamos o método público "dirigir", que incrementa a quilometragem internamente. Para obter o valor da quilometragem, usamos o método público "obter_quilometragem".

O encapsulamento permite que os dados internos de uma classe sejam protegidos e manipulados apenas por meio de métodos específicos, fornecendo controle sobre o acesso e a modificação desses dados.


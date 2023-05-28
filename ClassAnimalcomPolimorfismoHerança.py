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

#Programação Orientada a Objetos POO
#Python permite programar tanto em POO como em estrutura

#Objetos vão métodos e atributos

#classe é um projeto de um objeto

#METODO CONSTRUTOR / self é a pessoa1 a pessoa2 
class Pessoa:
    #METODO CONSTRUTOR
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def andar(self):
        print(f'{self.nome} está andando')

    def falar(self):
        print(f'{self.nome} está falando')

    def comer(self):
        print(f'{self.nome} está comendo')  

pessoa1 = Pessoa('Luiz', 35, 1.78)
pessoa1.andar()
pessoa1.comer()
pessoa1.falar()       
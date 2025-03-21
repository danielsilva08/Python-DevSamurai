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

pessoa1 = Pessoa('Luiz', 35, 1.78) 
pessoa2 = Pessoa('Maria',21,1.67)  

print(pessoa1.nome)
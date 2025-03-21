#Programação Orientada a Objetos POO
#Python permite programar tanto em POO como em estrutura

#Objetos vão métodos e atributos

#classe é um projeto de um objeto

#METODO CONSTRUTOR / self é a pessoa1 a pessoa2 
class Pessoa:
    #METODO CONSTRUTOR
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def imc(self):
        return self.peso / (self.altura * self.altura)
    #corrigi o erro proposital da altura. no caso na pessoa2 foi digitado como string na altura, Metodo GETTER e SETTER
    #GETTER
    @property
    def altura (self):
        return self._altura
        
    #SETTER
    @altura.setter
    def altura (self,valor):
        if isinstance(valor,str):#se está variavel for da classe string ele converte para verdadeiro. No caso altura da pessoa 2 foi digitado como string.
            valor = float(valor)
        self._altura = valor    

pessoa1 = Pessoa('Luiz', 35, 1.78, 90) 
pessoa2 = Pessoa('Maria', 21, '1.67', 50)  

#print(pessoa2.altura)
print(pessoa2.imc())
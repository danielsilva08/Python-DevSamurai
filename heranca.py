#HERANÇA = um novo objeto (objeto filho) irá herdar as caracteristicas do objeto pai

class Empregado:
    def __init__(self, identificacao, nome):
        self.identificacao = identificacao
        self.nome = nome

    def registrarponto():
        print('Registrando o ponto')

    def __str__(self):
        return(f'{self.identificacao} do empregado {self.nome}')
    
empregado = Empregado('1212', 'João')
print(empregado)        
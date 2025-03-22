#HERANÇA = um novo objeto (objeto filho) irá herdar as caracteristicas do objeto pai

class Empregado:
    def __init__(self, identificacao, nome):#construtor
        self.identificacao = identificacao
        self.nome = nome

    def registrarponto():
        print('Registrando o ponto')

    def __str__(self):
        return(f'{self.identificacao} do empregado {self.nome}')

 #herdando da classe pai   
class CorpoDocente(Empregado):
    def __init__(self, identificacao, nome, disciplina):#construtor
        super().__init__(identificacao, nome)
        self.disciplina = disciplina

    def atribuirNotas(self,nota):
        print(f'Nota atribuida = {nota}') 

class Adiministrativa(Empregado): 
    def __init__(self, identificacao, nome, cargo):
        super().__init__(identificacao, nome)
        self.cargo = cargo          

professor1 = CorpoDocente('1212', 'João', 'Programação')
empregado1 = Empregado('1213', 'Mario')
secretario1 = Adiministrativa('1210', 'Pedro','Secretário')

print(secretario1.cargo)
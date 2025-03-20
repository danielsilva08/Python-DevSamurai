#Medotos úteis em dicionários são: keys(), value(), itens()
dias = {'Sex':'sexta','Seg':'segunda','Qua':'Quarta','Qui':'Quinta'}

#Adiciona uma variavel
#dias_copy = dias
#dias_copy['Dom']='Domingo'
#print(dias)

#Importar. cria uma nova variavel mostrando a original como estava também. Na maneira acima somente cria uma nova variavel / serve para ultilizar em listas também.
import copy

dias_copy = copy.deepcopy(dias)
dias_copy['Dom']='Domingo'
print(f'Dicionario dias:{dias}')
print(f'Dicionario dias_copy: {dias_copy}')


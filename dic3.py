#DICIONÁRIOS!!!
#listas usamos[]
#tuplas usamos()
#strings usamos '' ou ""
#dicionários {chave: valor}-> chave poderá ser uma string ou um int
#O valor pode ser lista, string.

#criando um dicionário
empregados = {'01':['João',' Silva'], 
            '02':['Maria','das Graças'],
            '03':['Paulo','José']}

numero_func = input('Digite o numero do funcionario:\n')
nome = input('Digite o nome:\n')

if empregados.get(numero_func):
    print('Funcionario cadastrado')
else:
    empregados[numero_func]=[nome]    

print(empregados)
     

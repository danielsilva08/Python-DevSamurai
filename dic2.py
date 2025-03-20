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
#print(type(empregados))
#print(empregados['01'])#acessa valores atraves das chaves

#adicionar um novo funcionario
empregados['04'] = ['Rogerio','Silva']
#print(empregados)
#print(len(empregados)) #para saber quantos elementos tem dentro do dicionario

#O FUNCIONARIO 01 ESTA EM EMPREGADOS? TRUE
#print('01' in empregados)

del empregados['01'] #apaga a chave 01
print(empregados)

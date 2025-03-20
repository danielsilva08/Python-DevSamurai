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

#setdefault verifica se a chave já tem. Caso não tenha ele adiciona e caso tenha ele não faz nada.
empregados.setdefault('04',['Fulano de tal'])
print(empregados)
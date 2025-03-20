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

empregados2 = {'04':['Fulano','de Tal'],
               '05':['Beltrano','de Tal']}
#update concatena ou seja adiciona os dois empregados. não pode ter duas chaves ids iguais pois ele nã sobre escreve.
empregados.update(empregados2)
print(empregados)
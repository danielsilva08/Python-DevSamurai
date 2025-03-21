#Arquivos
#read(in), read(), readline(), readlines()

letra = open('exemplo.txt','r')

#print(letra.read(5)) Retorna os 5 primeiros caracteres dado texto

#print(letra.read()) Retorna todo o texto do meu arquivo

#print(letra.readline()) Retorna somente a primeira linha.

#print(letra.readlines()) Retorna uma lista contendo cada uma das linhas

print(len(letra.readlines())) # Retorna o numero de linhas
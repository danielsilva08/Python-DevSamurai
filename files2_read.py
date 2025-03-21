#Arquivos
#read(in), read(), readline(), readlines()

letra = open('exemplo.txt','r')

#contando as palavras
palavras = letra.read()
lista_palavras = palavras.split()
#print(lista_palavras)mostra todas as palavras
#print(len(lista_palavras)) Mostra quantas palavras tem numero
#print(lista_palavras.count('que')) conta quantas palavras ou letras tem basta colocar a palavra ou letra

#metodo para remover palavras repetidas na soma
print(f'Quantidade de palavras total: {len(lista_palavras)}')
set_palavras = set(lista_palavras)
print(f'Quantidade de palavras não repetidas:{len(set_palavras)}')
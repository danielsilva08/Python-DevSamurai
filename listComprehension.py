#List Comprehension
#Uma sinxtaxe mais curta para criar uma lista baseado em uma lista já existente
#Sintaze: novaLista = [expressão for item in interable if condition == True]

animais = ['cachorro','gato','tartura','girafa']
# novaLista = []

# for animal in animais:
#     if 't' in animal:
#         novaLista.append(animal)
# print(novaLista)  

novaLista = [animal for animal in animais if 't' in animal]
print(novaLista)
#Para cada animal dentro da minha lista animais se o meu animal tiver a letra t
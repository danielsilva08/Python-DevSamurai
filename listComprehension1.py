#List Comprehension
#Uma sintaxe mais curta para criar uma lista baseado em uma lista já existente
#Sintaxe: novaLista = [expressão for item in interable if condition == True]

#animais = ['cachorro','gato','tartura','girafa']
# novaLista = []

# for animal in animais:
#     if 't' in animal:
#         novaLista.append(animal)
# print(novaLista)

#Para cada numero dentro da minha lista de numero se o numero for divido por 2 for igual a 0 ou seja for par eu crio uma lista de numeros pares %signif. resto 
#novaLista = [numero for numero in range(10) if numero%2 == 0]  
#print(novaLista)

#Para cada animal dentro da minha lista animais colocar um upper letra maiuscula
#animais = ['cachorro','gato','tartura','girafa']
#novaLista = [animal.upper() for animal in animais]

#Para cada animal dentro da minha lista de animais se o animal dif. de cachorro retorne o animal se igual cachorro retorne macaco
animais = ['cachorro','gato','tartura','girafa']
novaLista = [animal if animal != 'cachorro' else 'macaco' for animal in animais]
print(novaLista)
#Uma função lambda é uma pequena função anônima
#Recebe os argumentos porém só pode executar uma expressão
#lambda argumentos : expressão
x = lambda a:a*3
#print(x(4))

soma = lambda a,b:a+b
print(soma(5,7))

graus_celsius = lambda f:(5/9)*(f-32)
print(f'A temperatura em graus Celsius é {graus_celsius(32)}')

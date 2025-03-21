#with open('text.txt','w') as file:
    #file.write('Meu curso de Python\n')
    #file.write('Aqui segunda linha')

with open('text.txt','a') as file:  
    # a significa append / para acrecentar no final da lista e não sobreescrever o que já tinha escrito anteriormente o w começa no primeiro arquivo linha. 
     file.write('\nAqui terceira linha')
#while True:
    #try:
        #x = int(input('Digite um numero:'))
    #except ValueError as erro:
        #print(f'Acontenceu um erro do tipo{erro}')   

        #print('O programa segue normalmente')     

try:
   lista=[]
   lista[1]
   x = int(input('Digite um numero:'))
except ValueError as erro:
   print(f'Acontenceu um erro do tipo{erro}') 
except: 
   print('Ocorreu um erro inesperado.')              

print('O programa segue normalmente')  


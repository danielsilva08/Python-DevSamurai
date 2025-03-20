#SET USA {}
#automaticamente ele remove no print os elementos duplicados

cesta = {'maça', 'banana','maça','uva','melancia','uva'}
print(cesta)

print("maça" in cesta) #maça esta na cesta? true

palavra = set('basquete')
print(palavra)

#para cada elemento x da palavra banana pega o unico elemento que não está na string
a = {x for x in 'banana' if x not in 'ab'}
print(a)
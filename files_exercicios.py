import time #pega a hora do sistema
import os.path #os é do sistema operacional o path verifica se o arquivo já foi criado ou não.

def geraLog(texto,nome_arquivo):
    #se dentro do diretorio que estou rodando já existir o arquivo log.txt/
    #ou seja de ele for falso criar arquivo
    if os.path.isfile('log.txt') is False:
       print('Criando arquivo')

    arquivo = open(nome_arquivo,'a')#'a' para não sobreescrever se colocar 'w' sobreescrever
    now = time.localtime()
    #now_formatado = time.strftime('%d/%m/%y as %H:%M:%S', now)
    now_formatado = time.strftime('%x as %X') #formato americano invertendo m e dia

    arquivo.write(f'{now_formatado} -> {texto}\n')
    arquivo.close

geraLog('usuario logou no sistema','log.txt')    
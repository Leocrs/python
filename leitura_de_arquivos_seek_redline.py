

# Forma de abrir arquivos em Python

arquivo = open('codigos_moedas.txt', 'r' ) # abre o arquivo codigos_moedas.txt no modo de leitura
print(arquivo) # <_io.TextIOWrapper name='codigos_moedas.txt' mode='r' encoding='UTF-8'> 
print(arquivo.read())    # codigos_moedas modo de leitura
print(arquivo.readline()) # codigos_moedas modo de leitura 1 linha
print(type(arquivo.readline())) # <class 'str'> 
arquivo.seek(0) # para pular uma linha do arquivo
print(arquivo.readlines()) #redlines() - para ler o arquivo no modo de leitura linha a linha

# ret retorna a quantidade de linhas do arquivo 
# redline() - para ler o arquivo no modo de leitura linha a linha
# função seek() - para ler o arquivo no modo de leitura e pular uma linha no arquivo (linha a linha) 
#exeção para ler o arquivo no modo de leitura
#arquivo.closed # fecha o arquivo
#print(arquivo.closed) # esse comando mostra se o arquivo está fechado






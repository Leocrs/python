

# Forma de abrir arquivos em Python

arquivo = open('Texto_Basico.txt', 'r' ) # abre o arquivo codigos_moedas.txt no modo de leitura
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

##########################################################################################################

# O bloco with abre o arquivo no modo de leitura e abre o arquivo no modo de escrita
# with é a forma Pythonica de abrir um arquivo, ela abre o arquivo no modo de leitura e fecha o arquivo
# exemplo
# with open('Texto_Basico.txt', 'r') as arquivo: # abre o arquivo codigos_moedas.txt no modo de leitura
    # print(arquivo.readlines()) # codigos_moedas modo de leitura

###########################################################################################################

# Escrevendo arquivos em Python
# arquivo = open('Texto_Basico.txt', 'w' ) # abre o arquivo codigos_moedas.txt no modo de escrita
# arquivo.write('Python') # escreve no arquivo codigos_moedas.txt

#exemplo 1 
arquivo = open('Texto_Basico.txt', 'w' ) # abre o arquivo codigos_moedas.txt no modo de escrita
print(arquivo.write('Python')) # escreve no arquivo 

#OBS: write() - escreve no arquivo em novo arquivo caso eu queira escrever numa boa, 
# porem se eu tentar escrever em um arquivo já existente, o python apaga o texto anterior.

#exemplo 2

with open('Texto_Basico.txt', 'w') as arquivo: # abre o arquivo codigos_moedas.txt no modo de escrita
    print(arquivo.write('Escrever dados em arquivo é muito facil. \n'))
    print(arquivo.write('Essa é a ultima linha escrita de texto. \n'))
    
with open('Texto_Basico.txt', 'r') as arquivo: # abre o arquivo codigos_moedas.txt no modo de leitura
     print(arquivo.read())

# 'x' - para escrever no arquivo CASO ELE não EXISTIR!
# 'a' - para escrever no arquivo CASO ELE EXISTIR

with open('Texto_teste.txt', 'w') as arquivo1:
    print(arquivo1.write('Escrever dados em arquivo para teste! \n'))
    print(arquivo1.readline)
#######################################################################################################

#  Forma de abrir arquivos em Python do Sistema Operacional
#  import da biblioteca io EX: from io import StringIO

from io import StringIO

mensagem = 'Python é uma linguagem de programação de alto nível' # mensagem do arquivo
arquivo = StringIO(mensagem) # cria um objeto StringIO
arquivo = open('arquivo.txt', 'w') # abre o arquivo codigos_moedas.txt no modo de leitura
print(arquivo.read())

arquivo.write('Python é uma linguagem de programação de alto nível')



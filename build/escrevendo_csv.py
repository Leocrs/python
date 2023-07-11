# Escrevendo em arquivos CSV - Python

# reader() = leitor writer() = escritor

# writer gera um arquivo CSV para poder escrever os dados em cada linha (lista)
from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Nome', 'Ano', 'Diretor'])
    while filme != 'sair':
        filme = input('Digite o nome do filme: ')
        if filme != 'sair':
            ano = input('Digite o ano do filme: ')
            diretor = input('Digite o diretor do filme: ')
            escritor_csv.writerow([filme, ano, diretor])

    
    
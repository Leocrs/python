from csv import DictWriter 

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = DictWriter (arquivo, fieldnames=['Nome', 'Ano', 'Diretor'])
    escritor_csv.writeheader()
    filme = None
    
    while filme != 'sair':
        filme = input('Digite o nome do filme: ')
        if filme != 'sair':
            ano = input('Digite o ano do filme: ')
            diretor = input('Digite o diretor do filme: ')
        
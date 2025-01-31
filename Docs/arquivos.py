

import os

# Manipulação de arquivos de texto com Python
caminho_arquivo = os.path.join(os.path.dirname(__file__), 'arquivo.txt')  # Cria o caminho para o arquivo
ler_doc = open(caminho_arquivo, 'r', encoding='utf-8')  # Abre o arquivo no modo de leitura editado para texto latino
print(ler_doc.read())  # Lê o arquivo e imprime o conteúdo



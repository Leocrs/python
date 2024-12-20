import pandas as pd

# Ler a planilha de base de vendas
df = pd.read_excel('r"C:\\Users\Leonardo\OneDrive\Documentos\Aula 4 Hashtag\Base de Vendas.xlsx"')

# Adicionar uma coluna 'estado' à planilha
df['estado'] = df['Cidade'].apply(lambda x: 'SP' if x == 'SP' else 'Outro')

# Agrupar por categoria de produtos e somar a quantidade de vendas
vendas_por_categoria = df.groupby('categoria')['vendas'].sum()

# Agrupar por estado e somar a quantidade de vendas
vendas_por_estado = df.groupby('Cidade')['vendas'].sum()

# Exibir o resultado
print("Vendas por categoria:")
print(vendas_por_categoria)
print("\nVendas por estado:")
print(vendas_por_estado)



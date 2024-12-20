import pandas as pd

# Carregar a base de dados
df = pd.read_excel(r'C:\Users\Leonardo\OneDrive\Documentos\Aula 4 Hashtag\Base de Vendas.xlsx')

# Exibir as colunas do DataFrame
print(df.columns)

# Agrupar por categoria de produtos e somar a quantidade de vendas
vendas_por_categoria = df.groupby('categoria')['vendas'].sum()

# Exibir o resultado
print(vendas_por_categoria)

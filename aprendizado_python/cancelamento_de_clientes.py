# 1 Importar a base de dados.
import pandas as pd 

# 2 Visualizar a base de dados. 
tabela = pd.read_csv(r"C:\Users\leonardo\Documents\GitHub\hashtag_Programacao\Analise_de_dados\cancelamentos.csv") # (coloque o seu caminho aqui, usei o "r" para ignorar "/")
print(tabela) # Exibir as informações da tabela padrão

# 3 Tratamento de erros da base de dados.
print(tabela.info()) # Exibir as informações da tabela
tabela = tabela.dropna() # Tratando valores vazios 
print(tabela.info()) # Exibir as informações da tabela
tabela = tabela.drop("CustomerID", axis=1) # Tratando colunas / axis=1 = coluna e axis=0 = linha
print(tabela)

# 4 Analise inicial dos dados entender como estão os cancelamentos de clientes.
print(tabela["cancelou"].value_counts(normalize=True).map(lambda x: "{:.1%}".format(x))) # Exibir a porcentagem de cancelamentos formatado 
print(tabela["duracao_contrato"].value_counts(normalize=True).map(lambda x: "{:.1%}".format(x)) ) # Exibir a porcentagem de cancelamentos formatado 
print(tabela.groupby("duracao_contrato").mean()) # Exibi media 
print(tabela.groupby("assinatura").mean()) # Exibi media 
# contrato mensal sempre cancelado 
tabela = tabela[tabela["duracao_contrato"] != "Monthly"]
# vamos ver o cancelamento de clientes na tabela mensal 
print(tabela["cancelou"].value_counts()) # Exibir a quantidade de cancelamentos
print(tabela["cancelou"].value_counts(normalize=True).map(lambda x: "{:.1%}".format(x))) # Exibir a porcentagem de cancelamentos formatado 

# 5 Analise final dos dados entender as causas dos cancelamentos dos clientes.
import plotly.express as px 
import plotly.io as pio
import matplotlib.pyplot as plt
grafico = plt.plot(tabela, x="assinatura" , color="cancelou")
plt.show()
grafico = plt.plot(tabela, x="duracao_contrato" , color="cancelou")
plt.show()
grafico = px.histogram(tabela, x="duracao_contrato" , color="cancelou")
grafico.show()
tabela = tabela[tabela["ligacoes_callcenter"] < 5]
tabela = tabela[tabela["dias_atraso"] <= 20]
# vamos ver o cancelamento de clientes na tabela mensal
print(tabela["cancelou"].value_counts()) # Exibir a quantidade de cancelamentos
print(tabela["cancelou"].value_counts(normalize=True).map(lambda x: "{:.1%}".format(x))) # Exibir a porcentagem de cancelamentos formatado


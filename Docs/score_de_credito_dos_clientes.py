import pandas as pd # importando a base de dados usando o pandas
from sklearn.preprocessing import LabelEncoder # Criar um objeto LabelEncoder, converte strings para valores numéricos

# Entender os desafios da empresa
# Importar a BD
tabela = pd.read_csv(r"C:\Users\leonardo\Documents\GitHub\hashtag_programacao\clientes.csv")
print(tabela.info()) # Exibir as informações da tabela

# Preparar e visualizar a BD para a IA.
codificador = LabelEncoder() # Criar um objeto LabelEncoder, converte strings para valores numéricos
tabela["profissao"] = codificador.fit_transform(tabela["profissao"])
tabela["mix_credito"] = codificador.fit_transform(tabela["mix_credito"])
tabela["comportamento_pagamento"] = codificador.fit_transform(tabela["comportamento_pagamento"]) # criar um objeto LabelEncoder, converte strings para valores numéricos
print(tabela.info()) # Exibir as informações da tabela

# Separar os dados em treino e teste
y = tabela["score_credito"] # coluna score_credito do banco de dados
x = tabela.drop(["score_credito","id_cliente"], axis=1) # coluna score_credito e id_cliente do banco de dados foram removidas
from sklearn.model_selection import train_test_split # importar a função train_test_split do sklearn para separar os dados em treino e teste
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, random_state=42) # separar os dados em treino e teste

# Criar um modelo de IA Score de crédito: ruim, medio e bom
# Arvore de decisão
# KNN K-Nearest Neighbors - Irmão de vizinhos mais próximos
from sklearn.neighbors import KNeighborsClassifier # importar a função KNeighborsClassifier do sklearn
from sklearn.ensemble import RandomForestClassifier # importar a função RandomForestClassifier do sklearn

modelo_arvoredecisao = RandomForestClassifier() # Criar um modelo de IA Score de crédito: ruim, medio e bom
modelo_knn = KNeighborsClassifier() # Criar um modelo de IA Score de crédito: ruim, medio e bom
modelo_arvoredecisao.fit(x_treino, y_treino) # treinar o modelo
modelo_knn.fit(x_treino, y_treino) # treinar o modelo

# Escolher o melhor modelo
# Acurácia do modelo
# O melhor modelo é a arvore de decisão 83%
from sklearn.metrics import accuracy_score # importar a função accuracy_score do sklearn
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste) # prever os resultados do modelo
previsao_knn = modelo_knn.predict(x_teste.to_numpy()) # prever os resultados do modelo
print(accuracy_score(y_teste, previsao_arvoredecisao)) # exibir a acurácia do modelo
print(accuracy_score(y_teste, previsao_knn)) # exibir a acurácia do modelo



# ESSE ULTIMO BLOCO ESTA DANDO ERRO DE TABELAS VINCULADAS!!!! BASTA RODAR ATE O DE CIMA
# Usar o modelo em um cenário real
novos_clientes = pd.read_csv(r"C:\Users\leonardo\Documents\GitHub\hashtag_programacao\clientes.csv") # "r" é necessário para ler o caminho do arquivo
novos_clientes["profissao"] = codificador.fit_transform(novos_clientes["profissao"])
novos_clientes["mix_credito"] = codificador.fit_transform(novos_clientes["mix_credito"])
novos_clientes["comportamento_pagamento"] = codificador.fit_transform(novos_clientes["comportamento_pagamento"]) # criar um objeto LabelEncoder, converte strings para valores numéricos
print(novos_clientes.info()) # Exibir as informações da tabela

previsao = modelo_arvoredecisao.predict(novos_clientes) # prever os resultados do modelo
print(previsao)

# fazendo novas previsões
novos_clientes = pd.read_csv("novos_clientes.csv")
print(novos_clientes)
for coluna in novos_clientes.columns:
    if novos_clientes[coluna].dtype == "object" and coluna != "score_credito":
        novos_clientes[coluna] = codificador.fit_transform(novos_clientes[coluna])

previsoes = modelo_arvoredecisao.predict(novos_clientes)
print(previsoes)


# Criando um banco de dados SQLite, com esse script: é possivel criar uma tabela e adicionar dados


import sqlite3 

connection = sqlite3.connect("banco.db")

cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY,\
      nome text, estrela real, diaria real, cidade text)"

cria_hotel = "INSERT INTO hoteis VALUES  ('alpha', 'Alpha Hotel', 4.3, 420.34, 'Rio de Janeiro')"

cursor.execute(cria_tabela) 
cursor.execute(cria_hotel)

connection.commit()

connection.close()

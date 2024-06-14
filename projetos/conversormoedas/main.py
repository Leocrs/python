# janela -> 500 x 500
# Titulo -> Conversor de moedas
# Campos -> selecioar a moeda de origem e a moeda de destino (campos de lista) com labels Selecione a moeda de origem e a moeda de destino
# Botoes -> Converter 
# Lista de exibição de moedas

import customtkinter
from customtkinter import *
from tkinter import *
from tkinter.messagebox import *

# criando a janela e configurando 
customtkinter.set_appearance_mode("dark") # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue") # Themes: "blue" (standard), "green", "dark-blue

janela = CTk() # janela
janela.geometry = ("500x500") # tamanho da janela

# Criar os botoes, texturas e outros elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas", font=("Arial", 20)) # Label para o texto Conversor de moedas
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem") # Label para selecionar a moeda de origem
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino") # Label para selecionar a moeda de destino
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL", "EUR", "BTC"]) # Campo para selecionar a moeda de origem
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL", "EUR", "BTC"]) # Campo para selecionar a moeda de destino
botao_converter = customtkinter.CTkButton(janela, text="Converter") # Botão para converter

def converter_moeda():
    print("Conversor de moedas")    

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda) # Botão para converter

lista_moedas = customtkinter.CTkScrollableFrame(janela) # Lista para exibir as moedas

moedas_disponiveis = ["USD: Dolar americano", "BRL: Real brasileiro", "EUR: Euro", "BTC: Bitcoin"] # Lista de moedas disponíveis
for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda) # Label para exibir as moedas disponíveis
    texto_moeda.pack()


# Colocar todos os elementos na tela 
titulo.pack(padx=20, pady=20) # Colocar o label Conversor de moedas
texto_moeda_origem.pack(padx=20, pady=10) # Colocar o label Selecione a moeda de origem
campo_moeda_origem.pack(padx=20) # Colocar o campo para selecionar a moeda de origem
texto_moeda_destino.pack(padx=20, pady=10) # Colocar o label Selecione a moeda de destino
campo_moeda_destino.pack(padx=20) # Colocar o campo para selecionar a moeda de destino
botao_converter.pack(padx=20, pady=20) # Colocar o botão Converter
lista_moedas.pack(padx=20, pady=20) # Colocar a lista para exibir as moedas


# Executar a janela
janela.mainloop()


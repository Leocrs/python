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
titulo = customtkinter.CTkLabel(janela) # Label para o texto Conversor de moedas
texto_moeda_origem = customtkinter.CTkLabel(janela) # Label para selecionar a moeda de origem


# Colocar todos os elementos na tela 


# Executar a janela
janela.mainloop()


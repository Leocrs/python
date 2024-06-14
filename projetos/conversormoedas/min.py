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
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = CTk()
janela.geometry = ("900x900")

# Criar os botoes, texturas e outros elementos
titulo = customtkinter.CTkLabel(janela)
# Colocar todos os elementos na tela 
# Executar a janela

janela.mainloop()


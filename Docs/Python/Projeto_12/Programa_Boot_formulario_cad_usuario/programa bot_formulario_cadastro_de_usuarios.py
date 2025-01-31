import pyautogui # Biblioteca para manipulação de tela
import time # Biblioteca para manipulação de tempo
pyautogui.PAUSE = 1 # tempo de pausa segundos entre tentativas
from turtle import position # Biblioteca para manipulação de posição
import pandas as pd
import tkinter as tk
import tkinter.messagebox as messagebox

# 1 Abrir o navegador e fazer login (chrome)
pyautogui.write("chrome") # escrever o navegador
pyautogui.press("enter") # entrar
pyautogui.press("win") # abrir o navegador
time.sleep(1) # espera 1 segundo
pyautogui.write("chrome") # escrever chrome
pyautogui.press("enter") # entrar
time.sleep(1) # espera 1 segundochrome
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # Entrar no link -> https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("enter") # entrar
time.sleep(1) # espera 1 segundo
pyautogui.click(x=949, y=449, duration=2) # clica na posição x=949, y=449
time.sleep(1) # espera 1 segundo
pyautogui.write("SeuEmailmeuAmigo@gmail.com") # escrever o email
time.sleep(1) # espera 1 chrome
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("123456") # escrever a senha
time.sleep(1) # espera 1 chrome
pyautogui.press("tab") # passando pro próximo campo
pyautogui.press("enter") # Aperte logar
time.sleep(1) # espera 1 chrome

# 2 Fazer cadastro dos produtos
tabela = pd.read_csv(r"C:\Users\leonardo\Documents\GitHub\hashtag_programacao\hashtag_Programacao\automacao_de_tarefas\produtos.csv") # "r" é necessário para ler o caminho do arquivo
print(tabela) # imprime a tabela
linha = 0  # contador de linhas
for linha in tabela.index: # percorre a tabela linha por linha em loop for linha in tabela.index: até que o comando break seja executado
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"] # pegar da tabela o valor do campo que a gente quer preencher
    # preencher o campo
    pyautogui.write(str(codigo)) # preencher o campo
    # passar para o próximo campo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab") 
    pyautogui.press("enter")  # cadastra o produto (botão enviar)

    linha += 1  # incrementa o contador de linhas

    if linha >= 3:
        break  # interrompe o loop após três formulários preenchidos

print("Cadastro concluído!")

# Exibir alerta personalizado
root = tk.Tk()
root.withdraw()  # Oculta a janela principal
messagebox.showinfo("Cadastro Concluído", "O cadastro dos produtos foi concluído com sucesso!")


#Comando para pegar a posição do cursor (documentação)
#posicao = pyautogui.position()
#time.sleep(5)  
#print(posicao)

 

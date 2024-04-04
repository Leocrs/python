# Programa de BOT de backup automatico de arquivos

import pyautogui # Biblioteca para manipulação de tela
import time # Biblioteca para manipulação de tempo
import os # Biblioteca para manipulação de arquivos
import shutil # Biblioteca para manipulação de arquivos
pyautogui.PAUSE = 1 # tempo de pausa segundos entre tentativas
#pyautogui.alert(" O programa vai começar, aguarde...") # mensagem de alerta 

# # abrir o gooqle drive na pasta de backup
pyautogui.press('winleft') # clica na tecla windows da esquerda
pyautogui.write('chrome') # escreva o nome do arquivo
pyautogui.press('enter') # clica no enter
time.sleep(1) # espera 1 segundo
pyautogui.write('https://drive.google.com/drive/folders/1BK33oZWE0WkzPpA8cdiWIOqe58ezU-QF') # escreva o link do arquivo
pyautogui.press('enter') # clica no enter
time.sleep(1) # espera 1 segundo

# # entrar na pasta do arquivos copiar e color no google drive
pyautogui.hotkey('winleft', 'r') # clica na tecla windows da esquerda
time.sleep(1) # espera 1 segundo    
pyautogui.typewrite(r" C:\Users\leonardo\Documents\backup ") # OBS: "r" é necessario para o Python abrir qualquer caminho sem inventar "moda"
pyautogui.press('enter') # clica no enter
pyautogui.hotkey('ctrl', 'a') # clica no ctrl + a 
pyautogui.dragTo(x=1361, y=329, duration=2)  # clica na posição x=1133, y=342 
time.sleep(1) # espera 1 segundo
pyautogui.mouseDown()  # clica no mouse
pyautogui.dragTo(x=550, y=591, duration=2)  # clica na posição x=550, y=591   
pyautogui.hotkey('alt','tab') # clica no alt + tab
time.sleep(1) # espera 1 segundo
pyautogui.mouseUp()  # clica no mouse
#pyautogui.alert("O programa terminou!") # mensagem de alerta  
#Comando nessessario para copiar o arquivo na posição exata via captura de tela
# time.sleep(5)
# from turtle import position
# posicao = pyautogui.position()
# print(posicao)






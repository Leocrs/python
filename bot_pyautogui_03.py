#Programa de BOT de backup automatico de arquivos

import pyautogui
import time
import os # Biblioteca para manipulação de arquivos
import shutil # Biblioteca para manipulação de arquivos
pyautogui.PAUSE = 3 # tempo de pausa segundos entre tentativas
pyautogui.alert(" O programa vai começar, aguarde...")


# abrir o gooqle drive na pasta de backup
pyautogui.press('winleft') # clica na tecla windows da esquerda
pyautogui.write('chrome') # escreva o nome do arquivo
pyautogui.press('enter') # clica no enter
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/folders/1BK33oZWE0WkzPpA8cdiWIOqe58ezU-QF') # escreva o link do arquivo
pyautogui.press('enter') # clica no enter
time.sleep(1)

# entrar na pasta do arquivos copiar e color no google drive
pyautogui.hotkey('winleft', 'r')
time.sleep(1)
pyautogui.typewrite(r" C:\Users\leonardo\Documents\backup ") # OBS: "r" é necessario para o Python abrir qualquer caminho sem inventar "moda"
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'a')
pyautogui.dragTo(x=1133, y=342, duration=2)
time.sleep(1)
pyautogui.mouseDown()
pyautogui.dragTo(x=550, y=591, duration=2)
pyautogui.hotkey('alt','tab')
time.sleep(1)
pyautogui.mouseUp()
pyautogui.alert("O programa terminou!")


#Comando nessessario para copiar o arquivo na posição exata via captura de tela
# time.sleep(5)
# from turtle import position
# posicao = pyautogui.position()
# print(posicao)







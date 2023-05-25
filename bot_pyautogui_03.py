# Programa de BOT de backup automatico de arquivos

import pyautogui
import time
import os # Biblioteca para manipulação de arquivos
import shutil # Biblioteca para manipulação de arquivos
pyautogui.PAUSE = 1 # tempo de pausa segundos entre tentativas
pyautogui.alert(" O codigo vai começar, Não use nada do seu computador enquanto o codigo esiver rodando!!!")

# abrir o gooqle drive na pasta de backup
pyautogui.press('winleft') # clica na tecla windows da esquerda
pyautogui.write('chrome') # escreva o nome do arquivo
pyautogui.press('enter') # clica no enter
time.sleep(1) # tempo de pausa
pyautogui.write('https://drive.google.com/drive/folders/1BK33oZWE0WkzPpA8cdiWIOqe58ezU-QF') # escreva o link do arquivo
pyautogui.press('enter') # clica no enter


#  entrar na pasta do arquivos copiar e color no google drive
pyautogui.hotkey('winleft', 'r')
time.sleep(1)
pyautogui.typewrite(r" C:\Users\leonardo\Documents\backup ") # OBS: "r" é necessario para o Python abrir qualquer caminho sem inventar "moda"
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
pyautogui.write('https://drive.google.com/drive/folders/1BK33oZWE0WkzPpA8cdiWIOqe58ezU-QF') # escreva o link do arquivo
time.sleep(1)
# Pressiona a tecla "Alt"
pyautogui.keyDown('altgr')
pyautogui.hotkey('tab', 'tab')







# Itera pelo atalho "Alt + Tab + Tab" duas vezes
# pyautogui.press('tab')
# time.sleep(0.5)
# pyautogui.press('tab')
# # Solta a tecla "Alt"
# pyautogui.keyUp('alt')


#pyautogui.hotkey('ctrl', 'v') 
pyautogui.press('enter') # copia o arquivo
pyautogui.alert("O programa terminou de rodar!")







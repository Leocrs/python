
import pyautogui  # faz automação com o pyautogui para criar o bot localmente (maquina)
pyautogui.pause= 3  # tempo de pausa  segundos
import pandas as pd  # importa o pandas para manipular os dados

import time # para pausar
time.sleep(3) # tempo de pausa segundos  

#vc precisa criar uma variavel e fazer ela retornar o valor. com print
from turtle import position
posicao = pyautogui.position()
print(posicao)

# Abrir a ferramenta/ sistema / programa
pyautogui.press ("win")
pyautogui.write ("Login.xlsx")
pyautogui.press ("backspace")
pyautogui.press ("enter")


# Preencher login e senha
pyautogui.click(x=538, y=265)
pyautogui.write("Leonardo")

# Preencher senha
pyautogui.click(x=478, y=315)
pyautogui.write("123mudar")
pyautogui.press("Fazer Login")
pyautogui.press("enter")



# Clicar em fazer login



import pyautogui
import time

pyautogui.hotkey('win')
time.sleep(2)
pyautogui.typewrite('Login.xlsx')
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.typewrite('leonardo')
pyautogui.press('tab')
pyautogui.typewrite('123mudar')
pyautogui.press('enter')

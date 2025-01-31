# -*- coding: utf-8 -*-

# Builtin
import tkinter as tk
import tkinter.messagebox


# Internal module
from app.calculadora import Calculadora

if __name__ == '__main__':
    master = tk.Tk()
    main = Calculadora(master)
    main.start()

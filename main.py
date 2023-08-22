""" Imports """
import tkinter as tk

from views.view_computer import view_new_computer
from utils.config import *

app = tk.Tk()
app.title("Inventário de TI")
app.geometry('900x600')

# Set default font
font_default = font.Font(family='Segoe UI', size=10, weight='normal')
font_bold = font.Font(family='Segoe UI', size=10, weight='bold')
app.option_add('*Font', font_default)

# Create menubar
menubar = tk.Menu(app)
app.config(menu=menubar)

# Create menu e submenu
menu_register = tk.Menu(menubar, tearoff=0)
menu_register.add_command(label="Novo Computador", command=view_new_computer)
menu_register.add_command(label="Novo Setor")
menubar.add_cascade(label="Cadastrar", menu=menu_register)

app.mainloop()

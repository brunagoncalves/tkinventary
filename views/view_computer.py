""" Imports """
import tkinter as tk

from utils.config import *


def view_new_computer():
    """ Função chama a tela para cadastro de novos computadores """
    dp_computer = tk.Toplevel()
    dp_computer.title("Novo Computador")
    dp_computer.geometry('700x600')
    dp_computer.resizable(width=False, height=False)

    # Frames
    frame_one = tk.Frame(dp_computer, bg=co2, height=30, width=100)
    frame_one.pack()

    # Inputs
    label_name = tk.Label(dp_computer, text="Nome do Computador")
    label_name.pack()
    entry_name = tk.Entry(dp_computer)
    entry_name.pack(ipadx=5, ipady=5)

    label_processor = tk.Label(dp_computer, text="Processador")
    label_processor.pack()
    entry_processor = tk.Entry(dp_computer)
    entry_processor.pack(ipadx=5, ipady=5)

    label_motherboard = tk.Label(dp_computer, text="Placa Mãe")
    label_motherboard.pack()
    entry_motherboard = tk.Entry(dp_computer)
    entry_motherboard.pack(ipadx=5, ipady=5)

    label_memory = tk.Label(dp_computer, text="Memória Ram")
    label_memory.pack()
    entry_memory = tk.Entry(dp_computer)
    entry_memory.pack(ipadx=5, ipady=5)

    label_disk = tk.Label(dp_computer, text="HD/SSD/M.2")
    label_disk.pack()
    entry_disk = tk.Entry(dp_computer)
    entry_disk.pack(ipadx=5, ipady=5)

    label_video = tk.Label(dp_computer, text="Placa de Vídeo")
    label_video.pack()
    entry_video = tk.Entry(dp_computer)
    entry_video.pack(ipadx=5, ipady=5)

    label_others = tk.Label(dp_computer, text="Outros")
    label_others.pack()
    entry_others = tk.Entry(dp_computer)
    entry_others.pack(ipadx=5, ipady=5)

    # Buttons
    btn_save = tk.Button(dp_computer, text="Salvar")
    btn_save.pack()

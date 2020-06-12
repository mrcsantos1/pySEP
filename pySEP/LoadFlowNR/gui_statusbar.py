import tkinter as tk


def set_statusbar(janela_main):
    status = tk.Label(janela_main,
                      text="teste status",
                      bd=3,
                      relief=tk.SUNKEN,
                      anchor=tk.W)
    status.pack(side=tk.BOTTOM, fill=tk.X)

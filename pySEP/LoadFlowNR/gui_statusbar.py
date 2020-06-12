import tkinter as tk


def set_statusbar(janela_main):
    status = tk.Label(janela_main,
                      text="Bem-vindo ao pySEP!",
                      justify=tk.CENTER,
                      bd=4,
                      relief=tk.FLAT,
                      anchor=tk.W,
                      bg="dark goldenrod",
                      padx=2,
                      pady=2)
    status.pack(side=tk.BOTTOM, fill=tk.X)

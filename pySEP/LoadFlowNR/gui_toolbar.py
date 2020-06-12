import tkinter as tk


def set_toolbar(janela_main):
    toolbar = tk.Frame(janela_main, bg="ghost white")

    add_barra = tk.Button(toolbar, text="Barra", command=add_bar)
    add_barra.pack(side=tk.LEFT, padx=2, pady=2)

    add_linha = tk.Button(toolbar, text="Linha", command=add_lin)
    add_linha.pack(side=tk.LEFT, padx=2, pady=2)

    toolbar.pack(side=tk.TOP, fill=tk.X)


def add_bar():
    print('\nAdicionar barra!')


def add_lin():
    print('\nAdicionar linha!')

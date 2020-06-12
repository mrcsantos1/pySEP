import tkinter as tk


def set_toolbar(janela_main):
    toolbar = tk.Frame(janela_main, bg="ghost white")

    ## Adicionar Barra

    add_barra = tk.Button(toolbar, text="Barra",
                          relief=tk.FLAT)
    # command=add_bar)
    add_barra.bind("<Button-1>", add_bar)

    add_barra.pack(side=tk.LEFT, padx=2, pady=2)

    ## Adicionar Linha

    add_linha = tk.Button(toolbar, text="Linha",
                          relief=tk.FLAT)
    add_linha.bind("<Button-1>", add_lin)
    add_linha.pack(side=tk.LEFT, padx=2, pady=2)

    toolbar.pack(side=tk.TOP, fill=tk.X)


def add_bar(event):
    print('\nAdicionar barra!', event)


def add_lin(event):
    print('\nAdicionar linha!', event)

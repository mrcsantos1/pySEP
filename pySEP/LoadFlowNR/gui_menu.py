import tkinter as tk


def menus(janela_main):
    menu = tk.Menu(janela_main, tearoff=False, bg="dark goldenrod")
    janela_main.config(menu=menu)

    sub_file = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Arquivo", menu=sub_file)
    sub_file.add_command(label="Novo Projeto", command=func_teste)
    sub_file.add_command(label="Salvar Projeto", command=func_teste)
    sub_file.add_command(label="Importar Projeto", command=func_teste)
    sub_file.add_separator()

    sub_edit = tk.Menu(menu, tearoff=False)
    menu.add_cascade(label="Editar", menu=sub_edit)
    sub_edit.add_command(label="Desfazer", command=func_teste)


    def func_teste():
        print('\ntestando')

import tkinter as tk


class JanelaMain:
    def __init__(self):
        self.__janela = tk.Tk()
        self.__info_basic = {}
        self.__text_status = tk.StringVar()

        # janela
        self.set_janela(janela_main=self.__janela)

        # menu
        self.set_menu(janela_main=self.__janela)

        # toolbar
        self.set_toolbar(janela_main=self.__janela)

        # status bar
        self.set_statusbar(janela_main=self.__janela, textvariable=self.__text_status)

        # Criando os binds com os eventos de mouse

        self.__janela.bind("<Enter>", self.bemvindo)

        # self.__janela.bind("<Button-1>", self.botaoPressionado)
        # self.__janela.bind("<ButtonRelease-1>", self.botaoLiberado)
        # self.__janela.bind("<B1-Motion>", self.mouseArrastado)

        self.__janela.mainloop()

    @staticmethod
    def set_janela(janela_main):
        janela_main.title("pySEP    -    Python em Sistemas Elétricos de Potência!")
        janela_main.geometry("1280x720+100+100")
        janela_main.wm_iconbitmap("images/logo_pySEP.ico")
        janela_main["bg"] = "light goldenrod"

    @staticmethod
    def set_menu(janela_main):
        def func_teste():
            print('\ntestando')

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

    def set_toolbar(self, janela_main):
        toolbar = tk.Frame(janela_main, bg="goldenrod")

        ## Adicionar Barra

        add_barra = tk.Button(toolbar, text="Barra",
                              relief=tk.FLAT,
                              bg="light goldenrod")
        add_barra.bind("<Button-1>", self.__add_bar)

        add_barra.pack(side=tk.LEFT, padx=2, pady=2)

        ## Adicionar Linha

        add_linha = tk.Button(toolbar, text="Linha",
                              relief=tk.FLAT,
                              bg="light goldenrod")
        add_linha.bind("<Button-1>", self.__add_lin)
        add_linha.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)

    def __add_bar(self, event):
        self.__text_status.set("Adicionando uma nova barra! ")
        print('\nAdicionar barra!', event)

    def __add_lin(self, event):
        self.__text_status.set("Adicionando uma nova linha! ")
        print('\nAdicionar linha!', event)

    @staticmethod
    def set_statusbar(janela_main, textvariable):
        status = tk.Label(janela_main,
                          justify=tk.CENTER,
                          bd=4,
                          relief=tk.FLAT,
                          anchor=tk.W,
                          bg="dark goldenrod",
                          padx=2,
                          pady=2,
                          textvariable=textvariable)
        status.pack(side=tk.BOTTOM, fill=tk.X)

    def bemvindo(self, event):
        self.__text_status.set("Bem-vindo ao pySEP!")

    # def botaoPressionado(self, event):
    #     self.__text_status.set("Pressionado em [ " + str(event.x) +
    #                            ", " + str(event.y) + " ]")

    # def botaoLiberado(self, event):
    #     self.__text_status.set("Solto em [ " + str(event.x) +
    #                            ", " + str(event.y) + " ]")

    # def mouseArrastado(self, event):
    #     self.__text_status.set("Arrastado até [ " + str(event.x) +
    #                            ", " + str(event.y) + " ]")


a = JanelaMain()

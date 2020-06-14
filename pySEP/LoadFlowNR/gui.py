import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import circuito as ckt


class JanelaMain:
    def __init__(self):
        self.__janela = tk.Tk()
        self.__info_basic = {
            'nums': {'barras': 1,
                     'linhas': 1
                     },
            'sBase': 100e6,
        }
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

        self.__circuito = ckt.Circuito(sBase=100e6)

        self.__teste = Figure(figsize=(5, 5), dpi=100)

        self.__s_base()

        self.__janela.mainloop()

    @staticmethod
    def set_janela(janela_main):
        janela_main.title("pySEP    -    Python em Sistemas Elétricos de Potência!")
        janela_main.geometry("1280x720+100+100")
        janela_main.wm_iconbitmap("images/logo_pySEP.ico")
        janela_main["bg"] = "light goldenrod"
        janela_main["bd"] = 5

    @staticmethod
    def set_menu(janela_main):
        def func_teste():
            print('\nmenu menu menu menu')

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

<<<<<<< HEAD
    def __show_grafo(self):
=======
    def __grafo_add_edge(self, list_linhas):
        self.__f = Figure(figsize=(5, 4), dpi=100)

        self.__grafo.add_edges_from(list_linhas)
        self.__grafo_pos = nx.spring_layout(self.__grafo)

        a = self.__f.add_subplot()

        self.__show_grafo(a=a)

    def __grafo_add_node(self, list_numBar):
        self.__f = Figure(figsize=(5, 4), dpi=100)

        self.__grafo.add_nodes_from(list_numBar)

        self.__grafo_pos = nx.spring_layout(self.__grafo)
>>>>>>> 29cc7eb (.)

        a = self.__teste.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7], [1, 2, -1, -2, 0, 3, 4])

        canvas = FigureCanvasTkAgg(self.__teste, self.__janela)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar_grafo = NavigationToolbar2Tk(canvas, self.__janela)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



    def set_toolbar(self, janela_main):
        toolbar = tk.Frame(janela_main, bg="goldenrod")

        # Adicionar Barra
        add_barra = tk.Button(
            master=toolbar,
            text="Adicionar Nova Barra",
            font=("Helvetica", 11),
            relief=tk.FLAT,
            bg="light goldenrod",
            bd=2,
            justify=tk.CENTER,
        )

        add_barra.bind("<Button-1>", self.__add_bar)
        add_barra.pack(side=tk.LEFT, padx=2, pady=2)

        # Adicionar Linha
        add_linha = tk.Button(
            master=toolbar,
            text="Adicionar Nova Linha",
            font=("Helvetica", 11),
            relief=tk.FLAT,
            bg="light goldenrod",
            bd=2,
            justify=tk.CENTER,
        )
        add_linha.bind("<Button-1>", self.__add_lin)
        add_linha.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)

    def __add_bar(self, event):
        self.__config_bar()
        self.__text_status.set("Adicionando uma nova barra! ")

    def __s_base(self):
        s_base = tk.Toplevel(master=self.__janela)
        s_base.title("\tBem-vindo ao pySEP!!\t")
        s_base.geometry("500x150+500+500")
        s_base.wm_iconbitmap("images/logo_pySEP.ico")
        s_base["bg"] = "light goldenrod"

        label_s_base = tk.Label(
            master=s_base,
            anchor=tk.CENTER,
            bg="light goldenrod",
            justify=tk.CENTER,
            padx=2,
            pady=2,
            text="Defina um valor base para o sistema em VA!\nInserir conforme exemplo: 100e6",
            font=("Helvetica", 18)
        )
        label_s_base.grid(row=0, columnspan=3, padx=5, pady=5)

        frame_s_base = tk.Entry(
            master=s_base,
            justify=tk.CENTER, width=30,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        frame_s_base.focus_set()
        frame_s_base.grid(row=1, columnspan=3, padx=5, pady=5)

        def __s_base_butt():
            self.__info_basic['sBase'] = float(frame_s_base.get())
            self.__circuito.set_s_base(sBase=float(frame_s_base.get()))
            print('Sbase = ', float(frame_s_base.get()))
            s_base.destroy()

        button_s_base = tk.Button(
            master=s_base,
            text="Vamos lá!", font=("Helvetica", 12), width=10,
            bg="goldenrod",
            bd=3,
            command=__s_base_butt,
            anchor=tk.CENTER,
            justify=tk.CENTER,
            compound=tk.CENTER,
            padx=2,
            pady=2,
            # relief=tk.FLAT,
        )
        button_s_base.grid(row=2, columnspan=3, padx=5, pady=5)

    def __erro(self, mensagem):
        erro = tk.Toplevel()
        erro.title("\tERRO!!\t")
        erro.geometry("400x250")
        erro.wm_iconbitmap("images/logo_pySEP.ico")
        erro["bg"] = "red"

        label_erro = tk.Label(
            master=erro,
            anchor=tk.CENTER,
            bg="red",
            justify=tk.CENTER,
            padx=2,
            pady=2,
            text=mensagem,
            font=("Helvetica", 20)
        )
        label_erro.pack(fill='both', expand=True)

    def __config_bar(self):
        config_bar = tk.Toplevel()
        config_bar.title("Configurações da barra " + str(self.__info_basic['nums'].get('barras')))
        config_bar.geometry("800x250")
        config_bar.wm_iconbitmap("images/logo_pySEP.ico")
        config_bar["bg"] = "light goldenrod"

        frame_config = tk.Frame(
            master=config_bar,
            bg="light goldenrod"
        )
        frame_config.pack(fill='both', expand=True)

        # TÍTULO DA JANELA
        label_titulo = tk.Label(
            master=frame_config,
            anchor=tk.CENTER,
            bg="light goldenrod",
            justify=tk.CENTER,
            padx=2,
            pady=2,
            text="Configurações da barra " + str(self.__info_basic['nums'].get('barras')),
            font=("Helvetica", 20)
        )
        label_titulo.grid(row=0, columnspan=6, padx=5, pady=5)

        # NÚMERO DA BARRA
        label_num_barra = tk.Label(
            master=frame_config,
            text="Número da barra: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_num_barra.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        entry_num_barra = tk.Entry(
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_num_barra.focus_set()
        entry_num_barra.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ##############################################################################

        label_div_1 = tk.Label(
            master=frame_config,
            text="    |||    ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bg="light goldenrod",
        )
        label_div_1.grid(row=1, column=2, padx=5, pady=5)

        ##############################################################################

        # TIPO DA BARRA
        __tipo_bar = tk.StringVar()

        _tipo1_barra = tk.Radiobutton(
            master=frame_config,
            text="REF",
            variable=__tipo_bar,
            value="1",
            bg="light goldenrod",
            command=__tipo_bar.set("1")
        )
        _tipo1_barra.grid(row=1, column=3, sticky=tk.W)

        _tipo2_barra = tk.Radiobutton(
            master=frame_config,
            text="PQ",
            variable=__tipo_bar,
            value="2",
            bg="light goldenrod",
            command=__tipo_bar.set("2")
        )
        _tipo2_barra.grid(row=1, column=4, sticky=tk.W)

        _tipo3_barra = tk.Radiobutton(
            master=frame_config,
            text="PV",
            variable=__tipo_bar,
            value="3",
            bg="light goldenrod",
            command=__tipo_bar.set("3")
        )
        _tipo3_barra.grid(row=1, column=5, sticky=tk.W)

        ##############################################################################

        label_div_2 = tk.Label(
            master=frame_config,
            text="    |||    ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bg="light goldenrod",
        )
        label_div_2.grid(row=2, column=2, padx=5, pady=5)

        ##############################################################################

        # TENSÃO DA BARRA
        label_tensao_barra = tk.Label(
            master=frame_config,
            text="Tensão da barra [pu]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_tensao_barra.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        entry_tensao_barra = tk.Entry(
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_tensao_barra.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        # ÂNGULO DA BARRA
        label_ang_barra = tk.Label(
            master=frame_config,
            text="Ângulo da tensão \ndesta barra [graus]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_ang_barra.grid(row=2, column=3, padx=5, pady=5, sticky=tk.W)

        entry_ang_barra = tk.Entry(
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_ang_barra.grid(row=2, column=4, padx=5, pady=5, sticky=tk.W)

        # CARGA DA BARRA
        label_carga_barra = tk.Label(
            master=frame_config,
            text="Carga desta barra (P+Qj)\nex.:100e6+50e6 [VA]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_carga_barra.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

        entry_carga_barra = tk.Entry(
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_carga_barra.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        ##############################################################################

        label_div_3 = tk.Label(
            master=frame_config,
            text="    |||    ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bg="light goldenrod",
        )
        label_div_3.grid(row=3, column=2, padx=5, pady=5)

        ##############################################################################

        # GERAÇÃO DA BARRA
        label_geracao_barra = tk.Label(
            master=frame_config,
            text="Geração desta barra (P+Qj)\nex.:100e6+50e6 [VA]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_geracao_barra.grid(row=3, column=3, padx=5, pady=5, sticky=tk.W)

        entry_geracao_barra = tk.Entry(
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_geracao_barra.grid(row=3, column=4, padx=5, pady=5, sticky=tk.W)

        # BOTÃO ADICIONAR
        def __add_butt():

            num_bar = int(entry_num_barra.get())
            print('\n\nnum bar = ', num_bar)

            tp_bar = int(__tipo_bar.get())
            print('tipo barra = ', tp_bar)

            tensao_bar = float(entry_tensao_barra.get())
            print('tensao bar = ', tensao_bar)

            ang_bar = float(entry_ang_barra.get())
            print('ang bar = ', ang_bar)

            carga_bar = str(entry_carga_barra.get())
            print('carga bar = ', carga_bar)

            geracao_bar = str(entry_geracao_barra.get())
            print('geracao bar = ', geracao_bar)

            if not carga_bar.__contains__("+") and not carga_bar.__contains__("-"):
                self.__erro(mensagem="INSERIR A CARGA NO FORMATO: \n P + Q OU P - Q !")
            elif not geracao_bar.__contains__("+") and not geracao_bar.__contains__("-"):
                self.__erro(mensagem="INSERIR A CARGA NO FORMATO: \n P + Q OU P - Q !")
            else:
                carga = list()
                geracao = list()
                if carga_bar.__contains__("+"):
                    carga = carga_bar.split("+")
                    carga = list(map(float, carga))
                    carga[1] *= 1j
                    carga = carga[0] + carga[1]
                elif carga_bar.__contains__("-"):
                    carga = carga_bar.split("-")
                    carga = list(map(float, carga))
                    carga[1] *= 1j
                    carga = carga[0] + carga[1]

                if geracao_bar.__contains__("+"):
                    geracao = geracao_bar.split("+")
                    geracao = list(map(float, geracao))
                    geracao[1] *= 1j
                    geracao = geracao[0] + geracao[1]

                elif geracao_bar.__contains__("-"):
                    geracao = geracao_bar.split("-")
                    geracao = list(map(float, geracao))
                    geracao[1] *= 1j
                    geracao = geracao[0] + geracao[1]

                self.__circuito.addBarra(
                    barra=num_bar,
                    code=tp_bar,
                    tensao=tensao_bar,
                    ang=ang_bar,
                    carga=carga,
                    geracao=geracao)
                print("\n\nBarra ", self.__info_basic['nums'].get('barras'), " adicionada! ")
                self.__circuito.showBarras()

                self.__info_basic['nums']['barras'] += 1
                self.__show_grafo()
                config_bar.destroy()

        butt_add = tk.Button(
            master=frame_config,
            text="Adicionar", font=("Helvetica", 12), height=2, width=30,
            bg="goldenrod",
            bd=3,
            command=__add_butt,
            anchor=tk.CENTER,
            justify=tk.CENTER,
            compound=tk.CENTER,
            padx=2,
            pady=2,
            relief=tk.GROOVE,
        )
        butt_add.grid(row=4, columnspan=5, padx=5, pady=5)

    def __config_lin(self):
        config_lin = tk.Toplevel()
        config_lin.title("Configurações de linha ")
        config_lin.geometry("620x250")
        config_lin.wm_iconbitmap("images/logo_pySEP.ico")
        config_lin["bg"] = "light goldenrod"

        frame_config = tk.LabelFrame(
            master=config_lin,
            bg="light goldenrod"
        )
        frame_config.pack(fill='both', expand=True)

        # TÍTULO DA JANELA
        label_titulo = tk.Label(
            master=frame_config,
            anchor=tk.CENTER,
            bg="light goldenrod",
            justify=tk.CENTER,
            padx=2,
            pady=2,
            text="Configurações da " + str(self.__info_basic['nums'].get('linhas')) + " ª linha.",
            font=("Helvetica", 20)
        )
        label_titulo.grid(row=0, columnspan=5, padx=5, pady=5)

        # NÚMERO DA BARRA 1
        label_num_barra1 = tk.Label(
            master=frame_config,
            text="Número da barra \nde origem: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_num_barra1.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        entry_num_barra1 = tk.Entry(
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_num_barra1.focus_set()
        entry_num_barra1.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        ##############################################################################

        label_div_1 = tk.Label(
            master=frame_config,
            text="    |||    ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bg="light goldenrod",
        )
        label_div_1.grid(row=1, column=2, padx=5, pady=5)

        ##############################################################################

        # NÚMERO DA BARRA 2
        label_num_barra2 = tk.Label(
            master=frame_config,
            text="Número da barra \nde destino: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_num_barra2.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)

        entry_num_barra2 = tk.Entry(
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_num_barra2.focus_set()
        entry_num_barra2.grid(row=1, column=4, padx=5, pady=5, sticky=tk.W)

        # IMPEDÂNCIA DA LINHA
        label_imp_linha = tk.Label(
            master=frame_config,
            text="Impedância da linha [pu]: \nExemplo: 0.1 + 0.2 ",
            font=("Helvetica", 14),
            justify=tk.CENTER,
            anchor=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_imp_linha.grid(row=2, columnspan=5, padx=5, pady=5)

        entry_imp_linha = tk.Entry(
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE,
            width=40,
        )
        entry_imp_linha.grid(row=3, columnspan=5, padx=5, pady=5)

        # BOTÃO ADICIONAR
        def __add_butt():

            num_bar1 = int(entry_num_barra1.get())
            print('\n\nnum bar1 = ', num_bar1)

            num_bar2 = int(entry_num_barra2.get())
            print('num bar2 = ', num_bar2)

            z_linha = str(entry_imp_linha.get())
            print('impedância = ', z_linha)

            if not z_linha.__contains__("+") and not z_linha.__contains__("-"):
                self.__erro(mensagem="INSERIR A IMPEDÂNCIA NO FORMATO: \n r + x OU r - x !")
            else:
                z = list()
                if z_linha.__contains__("+"):
                    z = z_linha.split("+")
                    z = list(map(float, z))
                    z[1] *= 1j
                    z = z[0] + z[1]
                elif z_linha.__contains__("-"):
                    z = z_linha.split("-")
                    z = list(map(float, z))
                    z[1] *= 1j
                    z = z[0] + z[1]

                self.__circuito.addLinha(
                    b1=num_bar1,
                    b2=num_bar2,
                    z_ij=z)
                print("\n\n", self.__info_basic['nums'].get('linhas'), "ª linha adicionada! ")
                self.__circuito.showLinhas()

                self.__info_basic['nums']['linhas'] += 1
                self.__grafo_add_edge(list_linhas=self.__circuito.getLinhas())
                # print('\n\nself.__circuito.getLinhas() = ', self.__circuito.getLinhas())
                config_lin.destroy()

        butt_add = tk.Button(
            master=frame_config,
            text="Adicionar", font=("Helvetica", 12), height=2, width=30,
            bg="goldenrod",
            bd=3,
            command=__add_butt,
            anchor=tk.CENTER,
            justify=tk.CENTER,
            compound=tk.CENTER,
            padx=2,
            pady=2,
            relief=tk.GROOVE,
        )
        butt_add.grid(row=5, columnspan=5, padx=5, pady=5)

    def __add_lin(self, event):
        self.__config_lin()
        self.__text_status.set("Adicionando uma nova linha! ")

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

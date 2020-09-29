import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
<<<<<<< HEAD
=======
import networkx as nx
<<<<<<< HEAD
from PIL import Image, ImageTk
>>>>>>> 61cee31 (logo adicionada)
=======
>>>>>>> c68287f (cálculo fluxo de potência)

# from .circuito import Circuito
from circuito import Circuito
from malha import Malha


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

        # self.__circuito = ckt.Circuito(sBase=100e6)
        self.__circuito = Circuito(sBase=100e6)

        self.__teste = Figure(figsize=(5, 5), dpi=100)

        self.__show_logo()
        self.__s_base()

        ## Malha de terra
        self.__malha = Malha()

        self.__janela.mainloop()

    def __show_logo(self):

        logo = tk.PhotoImage(file="images/pySEP_logo.png")

        self.__label_logo = tk.Label(
            master=self.__janela,
            bg="light goldenrod",
            image=logo,
        )
        self.__label_logo.photo = logo
        self.__label_logo.pack(expand=True)

    def set_menu(self, janela_main):
        def __fechar_tudo():
            self.__janela.destroy()
            self.__janela.quit()

        def func_teste():
            print('\nmenu menu menu menu')

        menu = tk.Menu(janela_main, tearoff=False, bg="dark goldenrod")
        janela_main.config(menu=menu)

<<<<<<< HEAD
<<<<<<< HEAD
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
=======
=======
        ## FILE
>>>>>>> da86f7d (opção menu projeto malha de terra ok)
        menu_file = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Arquivo", menu=menu_file)
        menu_file.add_command(label="Novo Projeto", command=func_teste)
        menu_file.add_command(label="Salvar Projeto", command=func_teste)
        menu_file.add_command(label="Importar Projeto", command=func_teste)
        menu_file.add_command(label="Sair", command=__fechar_tudo)
        menu_file.add_separator()

        ## EDIT
        menu_edit = tk.Menu(menu, tearoff=False)
        menu.add_cascade(label="Editar", menu=menu_edit)
        menu_edit.add_command(label="Desfazer", command=func_teste)
        menu_edit.add_separator()

        ## FLUXO DE POTÊNCIA
        menu_calc_fluxo = tk.Menu(master=menu, tearoff=False)
        menu.add_cascade(label="Fluxo de Potência", menu=menu_calc_fluxo)
        menu_calc_fluxo.add_command(label="Calcular!", command=self.__calc_fluxo)
        menu_calc_fluxo.add_cascade(label="Relatório Final", command=self.__calc_fluxo_relatorio)
        menu_calc_fluxo.add_cascade(label="Mostrar Perdas", command=self.__calc_fluxo_perdas)
        menu_calc_fluxo.add_cascade(label="Plotar Convergência da(s) Tensão(ões)",
                                    command=self.__calc_fluxo_plot_tensao)
        menu_calc_fluxo.add_cascade(label="Plotar Convergência do(s) Ângulo(os)", command=self.__calc_fluxo_plot_angulo)
        menu_calc_fluxo.add_separator()

        ## PROJETO MALHA DE TERRA
        menu_malha_terra = tk.Menu(master=menu, tearoff=False)
        menu.add_cascade(label="Projeto Malha de Terra", menu=menu_malha_terra)
        menu_malha_terra.add_command(label="Adicionar informações de projeto", command=self.__malha_terra_add_info)
        menu_malha_terra.add_cascade(label="Realizar teste de projeto", command=self.__malha_terra_testar)
        # menu_malha_terra.add_cascade(label="Mostrar Perdas", command=self.__calc_fluxo_perdas)
        # menu_malha_terra.add_cascade(label="Plotar Convergência da(s) Tensão(ões)",
        #                             command=self.__calc_fluxo_plot_tensao)
        # menu_malha_terra.add_cascade(label="Plotar Convergência do(s) Ângulo(os)", command=self.__calc_fluxo_plot_angulo)
        menu_malha_terra.add_separator()

        # Sistemas de Proteção
        menu_protecao = tk.Menu(master=menu, tearoff=False)
        menu.add_cascade(label="Sistemas de Proteção", menu=menu_protecao)
        menu_protecao.add_command(label="Desenhar Circuito do Sistema", command=self.__embreve)
        # menu_protecao.add_cascade(label="Realizar teste de projeto", command=self.__malha_terra_testar)
        # menu_malha_terra.add_cascade(label="Mostrar Perdas", command=self.__calc_fluxo_perdas)
        # menu_malha_terra.add_cascade(label="Plotar Convergência da(s) Tensão(ões)",
        #                             command=self.__calc_fluxo_plot_tensao)
        # menu_malha_terra.add_cascade(label="Plotar Convergência do(s) Ângulo(os)", command=self.__calc_fluxo_plot_angulo)
        menu_protecao.add_separator()

    def __embreve(self):
        print("Ferramenta em análise para desenvolvimento")
        config_draw_prot = tk.Toplevel()
        config_draw_prot.title("Ferramenta em análise para desenvolvimento")
        config_draw_prot.geometry("1100x700")
        config_draw_prot.wm_iconbitmap("images/logo_pySEP.ico")
        config_draw_prot["bg"] = "light goldenrod"
        frame_info_draw_prot = tk.LabelFrame(
            master=config_draw_prot,
            bg="light goldenrod",
            text="Ferramenta em análise para desenvolvimento",
            font=("Helvetica", 20)
        )
        frame_info_draw_prot.pack(fill='both', expand=True)

    def __malha_terra_testar(self):
        config_testar_malha = tk.Toplevel()
        config_testar_malha.title("Testar projeto de malha de terra")
        config_testar_malha.geometry("660x215")
        config_testar_malha.wm_iconbitmap("images/logo_pySEP.ico")
        config_testar_malha["bg"] = "light goldenrod"

        frame_teste_malha = tk.LabelFrame(
            master=config_testar_malha,
            bg="light goldenrod",
            text="Testar Projeto de Malha de Terra",
            font=("Helvetica", 20)
        )
        # frame_teste_malha.pack(fill='both', expand=True)
        frame_teste_malha.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # LABEL Profundidade das Hastes
        label_profundidade_hastes = tk.Label(
            master=frame_teste_malha,
            text="Profundidade das hastes [m]: ",
            font=("Helvetica", 15),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_profundidade_hastes.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        entry_profundidade_hastes = tk.Entry(
            font=("Helvetica", 15),
            master=frame_teste_malha,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_profundidade_hastes.focus_set()
        entry_profundidade_hastes.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # LABEL Profundidade das Hastes
        label_iteracoes = tk.Label(
            master=frame_teste_malha,
            text="Número de iterações: \nQuanto maior, mais preciso o cálculo simples. ",
            font=("Helvetica", 14),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_iteracoes.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        entry_iteracoes = tk.Entry(
            font=("Helvetica", 15),
            master=frame_teste_malha,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_iteracoes.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # BOTÃO ADICIONAR
        def __add_butt_salvar():
            profundidade = float(entry_profundidade_hastes.get())
            print('\n\nProfundidade das hastes = ', profundidade)

            iteracoes = int(entry_iteracoes.get())
            print('\n\nProfundidade das hastes = ', iteracoes)

            print('\n\n\n=========================== TESTE SIMPLES DO PROJETO DA MALHA DE TERRA ======================')
            self.__malha.testar_ri_v(profundidade_haste=profundidade, iteracoes=iteracoes, show=True)
            if self.__malha.get_teste() is False:
                print('\n\n\n======================= TESTE COMPLETO DO PROJETO DA MALHA DE TERRA =====================')
                self.__malha.testar_vmalha_vtoq(show=True)
                self.__malha.testar_vpsm_vpasso(show=True)

            config_testar_malha.destroy()

        butt_add_salvar = tk.Button(
            master=config_testar_malha,
            text="Testar!", font=("Helvetica", 12), height=2,  # width=30,
            bg="goldenrod",
            bd=3,
            command=__add_butt_salvar,
            anchor=tk.CENTER,
            justify=tk.CENTER,
            compound=tk.CENTER,
            padx=2,
            pady=2,
            relief=tk.GROOVE,
        )
        butt_add_salvar.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

    def __malha_terra_add_info(self):
        config_info_malha = tk.Toplevel()
        config_info_malha.title("Informações de Projeto da Malha de Terra")
        config_info_malha.geometry("1100x700")
        config_info_malha.wm_iconbitmap("images/logo_pySEP.ico")
        config_info_malha["bg"] = "light goldenrod"

        frame_info_malha = tk.LabelFrame(
            master=config_info_malha,
            bg="light goldenrod",
            text="Informações de Projeto da Malha de Terra",
            font=("Helvetica", 20)
        )
        frame_info_malha.pack(fill='both', expand=True)

        # LABEL ADD Icc
        label_add_icc = tk.Label(
            master=frame_info_malha,
            text="Corrente de curto-circuito [A]: ",
            font=("Helvetica", 15),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_add_icc.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        entry_add_icc = tk.Entry(
            font=("Helvetica", 15),
            master=frame_info_malha,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_add_icc.focus_set()
        entry_add_icc.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # LABEL ADD Imalha
        label_add_imalha = tk.Label(
            master=frame_info_malha,
            text="Corrente de malha [A]: ",
            font=("Helvetica", 15),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_add_imalha.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        entry_add_imalha = tk.Entry(
            font=("Helvetica", 15),
            master=frame_info_malha,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_add_imalha.grid(row=0, column=4, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # LABEL ADD tempo protecao
        label_add_t_protecao = tk.Label(
            master=frame_info_malha,
            text="Tempo da proteção [s]: ",
            font=("Helvetica", 15),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_add_t_protecao.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        entry_add_t_protecao = tk.Entry(
            font=("Helvetica", 15),
            master=frame_info_malha,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_add_t_protecao.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # LABEL ADD tempo defeito
        label_add_t_defeito = tk.Label(
            master=frame_info_malha,
            text="Tempo do defeito [s]: ",
            font=("Helvetica", 15),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_add_t_defeito.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        entry_add_t_defeito = tk.Entry(
            font=("Helvetica", 15),
            master=frame_info_malha,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_add_t_defeito.grid(row=1, column=4, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # LABEL ADD temperatura ambiente
        label_add_temp_ambiente = tk.Label(
            master=frame_info_malha,
            text="Temperatura ambiente [C°]: ",
            font=("Helvetica", 15),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_add_temp_ambiente.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        entry_add_temp_ambiente = tk.Entry(
            font=("Helvetica", 15),
            master=frame_info_malha,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_add_temp_ambiente.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # LABEL ADD temperatura máxima permissível
        label_add_temp_max_permissivel = tk.Label(
            master=frame_info_malha,
            text="Temperatura máxima permissível [C°]: ",
            font=("Helvetica", 15),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_add_temp_max_permissivel.grid(row=2, column=3, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        entry_add_temp_max_permissivel = tk.Entry(
            font=("Helvetica", 15),
            master=frame_info_malha,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_add_temp_max_permissivel.grid(row=2, column=4, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # BOTÃO ADICIONAR
        def __add_butt_salvar():
            icc = float(entry_add_icc.get())
            print('\n\nIcc = ', icc)

            imalha = float(entry_add_imalha.get())
            print('Imalha = ', imalha)

            t_prot = float(entry_add_t_protecao.get())
            print('tempo protecao = ', t_prot)

            t_def = float(entry_add_t_defeito.get())
            print('tempo defeito = ', t_def)

            temp_amb = int(entry_add_temp_ambiente.get())
            print('temperatura ambiente = ', temp_amb)

            temp_max = int(entry_add_temp_max_permissivel.get())
            print('temperatura maxima = ', temp_max)

            self.__malha.add_icc(i_cc=icc)
            self.__malha.add_i_malha(i_malha=imalha)
            self.__malha.add_t_protecao(t_protecao=t_prot)
            self.__malha.add_t_defeito(t_defeito=t_def)
            self.__malha.add_temp_ambiente(temp_ambiente=temp_amb)
            self.__malha.add_temp_max_permissivel(temp_max_permissivel=temp_max)

            config_info_malha.destroy()

        butt_add_salvar = tk.Button(
            master=frame_info_malha,
            text="Salvar!", font=("Helvetica", 12), height=2,  # width=30,
            bg="goldenrod",
            bd=3,
            command=__add_butt_salvar,
            anchor=tk.CENTER,
            justify=tk.CENTER,
            compound=tk.CENTER,
            padx=2,
            pady=2,
            relief=tk.GROOVE,
        )
        butt_add_salvar.grid(row=3, columnspan=5, padx=5, pady=5)

    def __calc_fluxo_plot_tensao(self):
        self.__circuito.plot_conv(tensao=True, ang=False)

    def __calc_fluxo_plot_angulo(self):
        self.__circuito.plot_conv(tensao=False, ang=True)

    def __calc_fluxo_perdas(self):
        self.__circuito.relatorio(show_tensoes=False, show_correntes=False, show_fluxo=False)
        self.__circuito.perdas(show=True)
        self.__text_status.set("Perdas do circuito!")

    def __calc_fluxo_relatorio(self):
        self.__relatorio_fluxo()
        self.__text_status.set("Relatório Final!")

    def __relatorio_fluxo(self):  # Talvez depois colocar os resultados em um toplevel ou algo assim

        config_relatorio = tk.Toplevel()
        config_relatorio.title("Relatório Final do Fluxo de Potência")
        config_relatorio.geometry("460x250")
        config_relatorio.wm_iconbitmap("images/logo_pySEP.ico")
        config_relatorio["bg"] = "light goldenrod"

        frame_relatorio = tk.LabelFrame(
            master=config_relatorio,
            bg="light goldenrod"
        )
        frame_relatorio.pack(fill='both', expand=True)
>>>>>>> 7de809c (relatório e perdas)

        # TÍTULO DA JANELA
        label_titulo = tk.Label(
            master=frame_relatorio,
            anchor=tk.CENTER,
            bg="light goldenrod",
            justify=tk.CENTER,
            padx=2,
            pady=2,
            text="Relatório Final do Fluxo de Potência",
            font=("Helvetica", 20)
        )
        label_titulo.grid(row=0, columnspan=6, padx=5, pady=5)

        # MOSTRAR TENSÕES: True ou False
        __relatorio_tensoes = tk.BooleanVar()

        _tensoes_true = tk.Radiobutton(
            master=frame_relatorio,
            text="Mostrar Tensões: ",
            font=("Helvetica", 13),
            variable=__relatorio_tensoes,
            value=True,
            bg="light goldenrod",
            command=__relatorio_tensoes.set(True)
        )
        _tensoes_true.grid(row=2, column=0, sticky=tk.W)

<<<<<<< HEAD
        self.__grafo_pos = nx.spring_layout(self.__grafo)
>>>>>>> 29cc7eb (.)

        a = self.__teste.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7], [1, 2, -1, -2, 0, 3, 4])

<<<<<<< HEAD
        canvas = FigureCanvasTkAgg(self.__teste, self.__janela)
=======
    def __show_grafo(self, a):
        self.__frame_grafo.destroy()
        self.__frame_grafo = tk.Frame(
            master=self.__janela,
            bg="light goldenrod"
=======
        _tensoes_false = tk.Radiobutton(
            master=frame_relatorio,
            text=" Não Mostrar Tensões: ",
            font=("Helvetica", 13),
            variable=__relatorio_tensoes,
            value=False,
            bg="light goldenrod",
            command=__relatorio_tensoes.set(True)
        )
        _tensoes_false.grid(row=2, column=3, sticky=tk.W)

        # MOSTRAR ÂNGULOS: True ou False
        __relatorio_corr = tk.BooleanVar()

        _correntes_true = tk.Radiobutton(
            master=frame_relatorio,
            text="Mostrar Correntes",
            font=("Helvetica", 13),
            variable=__relatorio_corr,
            value=True,
            bg="light goldenrod",
            command=__relatorio_corr.set(False)
        )
        _correntes_true.grid(row=4, column=0, sticky=tk.W)

        _correntes_false = tk.Radiobutton(
            master=frame_relatorio,
            text="Não Mostrar Correntes",
            font=("Helvetica", 13),
            variable=__relatorio_corr,
            value=False,
            bg="light goldenrod",
            command=__relatorio_corr.set(False)
>>>>>>> 7de809c (relatório e perdas)
        )
        _correntes_false.grid(row=4, column=3, sticky=tk.W)

        # MOSTRAR FLUXO: True ou False
        __relatorio_fluxo = tk.BooleanVar()

        _fluxo_true = tk.Radiobutton(
            master=frame_relatorio,
            text="Mostrar Fluxo",
            font=("Helvetica", 13),
            variable=__relatorio_fluxo,
            value=True,
            bg="light goldenrod",
            command=__relatorio_fluxo.set(False)
        )
        _fluxo_true.grid(row=6, column=0, sticky=tk.W)

<<<<<<< HEAD
        canvas = FigureCanvasTkAgg(self.__f, master=self.__frame_grafo)
>>>>>>> fbd7d23 (.)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar_grafo = NavigationToolbar2Tk(canvas, self.__janela)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



    def set_toolbar(self, janela_main):
        toolbar = tk.Frame(janela_main, bg="goldenrod")
=======
        _fluxo_false = tk.Radiobutton(
            master=frame_relatorio,
            text="Não Mostrar Fluxo",
            font=("Helvetica", 13),
            variable=__relatorio_fluxo,
            value=False,
            bg="light goldenrod",
            command=__relatorio_fluxo.set(False)
        )
        _fluxo_false.grid(row=6, column=3, sticky=tk.W)

        # BOTÃO ADICIONAR
        def __add_butt():
            info_tensoes = __relatorio_tensoes.get()
            print('Mostrar tensões = ', info_tensoes)

            info_corr = __relatorio_corr.get()
            print('Mostrar correntes = ', info_corr)
>>>>>>> 7de809c (relatório e perdas)

            info_fluxo = __relatorio_fluxo.get()
            print('Mostrar Fluxo = ', info_fluxo)

            self.__circuito.relatorio(
                show_tensoes=info_tensoes,
                show_correntes=info_corr,
                show_fluxo=info_fluxo
            )
            print("\n\nRelatório Mostrado! ")

            self.__label_logo.destroy()
            config_relatorio.destroy()

        butt_add = tk.Button(
            master=frame_relatorio,
            text="Mostrar!", font=("Helvetica", 12), height=2, width=30,
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
        butt_add.grid(row=8, columnspan=6, padx=5, pady=5)

    def __calc_fluxo(self):
        self.__config_fluxo()
        self.__text_status.set("Fluxo de potência calculado!")

    def __config_fluxo(self):
        config_fluxo = tk.Toplevel()
        config_fluxo.title("Calcular Fluxo de Potência")
        config_fluxo.geometry("460x250")
        config_fluxo.wm_iconbitmap("images/logo_pySEP.ico")
        config_fluxo["bg"] = "light goldenrod"

        frame_config = tk.LabelFrame(
            master=config_fluxo,
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
            text="Calcular Fluxo de Potência",
            font=("Helvetica", 20)
        )
        label_titulo.grid(row=0, columnspan=6, padx=5, pady=5)

        # NÚMERO DA BARRA
        label_erro_fluxo = tk.Label(
            master=frame_config,
            text="Erro de convergência: \nExemplo: 1e-2 ou 0.01",
            font=("Helvetica", 15),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_erro_fluxo.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        entry_erro_fluxo = tk.Entry(
            font=("Helvetica", 15),
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_erro_fluxo.focus_set()
        entry_erro_fluxo.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W)

        # MOSTRAR ITERAÇÕES: True ou False
        __show_iter = tk.BooleanVar()

        _iter_true = tk.Radiobutton(
            master=frame_config,
            text="Mostrar Iterações",
            font=("Helvetica", 13),
            variable=__show_iter,
            value=True,
            bg="light goldenrod",
            command=__show_iter.set(True)
        )
        _iter_true.grid(row=2, column=0, sticky=tk.W)

        _iter_false = tk.Radiobutton(
            master=frame_config,
            text="Não Mostrar Iterações",
            font=("Helvetica", 13),
            variable=__show_iter,
            value=False,
            bg="light goldenrod",
            command=__show_iter.set(False)
        )
        _iter_false.grid(row=2, column=3, sticky=tk.W)

        # BOTÃO ADICIONAR
        def __add_butt():
            err_flux = float(entry_erro_fluxo.get())
            print('\n\nErro iterações = ', err_flux)

            show_inter = int(__show_iter.get())
            print('Mostrar iterações = ', show_inter)

            self.__circuito.calcular_fluxo_pot_nr(
                erro=err_flux,
                show=show_inter
            )
            print("\n\nFluxo de Potência calculado! ")
            self.__circuito.showBarras()

            self.__label_logo.destroy()
            config_fluxo.destroy()

        butt_add = tk.Button(
            master=frame_config,
            text="Calcular!", font=("Helvetica", 12), height=2, width=30,
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

        a = self.__f.add_subplot()

        self.__show_grafo(a=a)

    def __show_grafo(self, a):
        self.__frame_grafo.destroy()
        self.__frame_grafo = tk.Frame(
            master=self.__janela,
            bg="light goldenrod"
        )
        self.__frame_grafo.pack(fill='both', expand=True)

        pesos = nx.get_edge_attributes(self.__grafo, 'z')

        nx.draw_networkx(self.__grafo, self.__grafo_pos, ax=a, font_color='w', font_size=15,
                         node_size=700, node_color='saddlebrown', node_shape='s',
                         width=5, edge_color='black')

        nx.draw_networkx_edge_labels(self.__grafo, self.__grafo_pos, ax=a, font_size=20,
                                     node_size=700, node_color='saddlebrown', node_shape='s',
                                     width=5, edge_color='black', edge_labels=pesos, font_color='black')

        canvas = FigureCanvasTkAgg(self.__f, master=self.__frame_grafo)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar_grafo = NavigationToolbar2Tk(canvas, self.__frame_grafo)
        toolbar_grafo.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def set_toolbar(self, janela_main):
        toolbar = tk.Frame(janela_main, bg="goldenrod")

        # Adicionar Barra
        add_barra = tk.Button(
            master=toolbar,
            text="Adicionar Novo Nó",
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

        # Adicionar Solos
        add_solo = tk.Button(
            master=toolbar,
            text="Informações do solo",
            font=("Helvetica", 11),
            relief=tk.FLAT,
            bg="light goldenrod",
            bd=2,
            justify=tk.CENTER,
        )
        add_solo.bind("<Button-1>", self.__add_solo)
        add_solo.pack(side=tk.LEFT, padx=2, pady=2)

        # Adicionar Malha
        add_malha = tk.Button(
            master=toolbar,
            text="Informações da malha de terra",
            font=("Helvetica", 11),
            relief=tk.FLAT,
            bg="light goldenrod",
            bd=2,
            justify=tk.CENTER,
        )
        add_malha.bind("<Button-1>", self.__add_malha)
        add_malha.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)

    def __add_malha(self, event):
        self.__config_malha()
        self.__text_status.set("Adicionando informações da malha de terra! ")

    def __config_malha(self):
        config_malha = tk.Toplevel()
        config_malha.title("Configurações da malha")
        config_malha.geometry("1060x900")
        config_malha.wm_iconbitmap("images/logo_pySEP.ico")
        config_malha["bg"] = "light goldenrod"

        frame_config = tk.Frame(
            master=config_malha,
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
            text="Configurações da malha",
            font=("Helvetica", 20)
        )
        label_titulo.grid(row=0, columnspan=10, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> LABEL Largura da malha
        label_malha_largura = tk.Label(
            master=frame_config,
            text="Largura da malha [m]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_malha_largura.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> ENTRY Largura da malha

        entry_malha_largura = tk.Entry(
            font=("Helvetica", 12),
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_malha_largura.focus_set()
        entry_malha_largura.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> LABEL Comprimento da malha
        label_malha_comprimento = tk.Label(
            master=frame_config,
            text="Comprimento da malha [m]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_malha_comprimento.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> ENTRY Comprimento da malha

        entry_malha_comprimento = tk.Entry(
            font=("Helvetica", 12),

            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_malha_comprimento.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> LABEL Espaçamento da largura da malha
        label_malha_esp_larg = tk.Label(
            master=frame_config,
            text="Espaçamento de cada haste\nno eixo X [0.05 a 0.1]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_malha_esp_larg.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> ENTRY Espaçamento da largura da malha

        entry_malha_esp_larg = tk.Entry(
            font=("Helvetica", 12),
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_malha_esp_larg.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> LABEL Espaçamento do comprimento da malha
        label_malha_esp_compr = tk.Label(
            master=frame_config,
            text="Espaçamento de cada haste\nno eixo Y [0.05 a 0.1]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_malha_esp_compr.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> ENTRY Espaçamento do comprimento da malha

        entry_malha_esp_compr = tk.Entry(
            font=("Helvetica", 12),
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_malha_esp_compr.grid(row=2, column=3, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        ########################################################################################################################

        _frame_profundidade = tk.Frame(
            master=frame_config,
            bg="light goldenrod",
            padx=2,
            pady=2,
        )
        _frame_profundidade.grid(row=3, columnspan=10, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> LABEL profundidade da malha
        label_malha_profundidade = tk.Label(
            master=_frame_profundidade,
            text="Profundidade da malha [m]:",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_malha_profundidade.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # Informações --> ENTRY profundidade da malha

        entry_malha_profundidade = tk.Entry(
            font=("Helvetica", 12),
            master=_frame_profundidade,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_malha_profundidade.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        ########################################################################################################################

        _labelframe_periferia = tk.LabelFrame(
            master=frame_config,
            text="Hastes na periferia? ", font=("Helvetica", 14),
            bg="light goldenrod",
            padx=2,
            pady=2,
        )
        _labelframe_periferia.grid(row=4, columnspan=10, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # HASTES NA PERIFERIA?
        __hastes_periferia = tk.BooleanVar()

        _periferia_true = tk.Radiobutton(
            master=_labelframe_periferia,
            text="Sim: ",
            font=("Helvetica", 13),
            variable=__hastes_periferia,
            value=True,
            bg="light goldenrod",
            command=__hastes_periferia.set(True)
        )
        _periferia_true.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        _periferia_false = tk.Radiobutton(
            master=_labelframe_periferia,
            text="Não: ",
            font=("Helvetica", 13),
            variable=__hastes_periferia,
            value=False,
            bg="light goldenrod",
            command=__hastes_periferia.set(True)
        )
        _periferia_false.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        _frame_dimensoes = tk.Frame(
            master=frame_config,
            bg="light goldenrod",
            padx=2,
            pady=2,
        )
        _frame_dimensoes.grid(row=5, columnspan=10, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        _frame_grafo_malha = tk.Frame(
            master=frame_config,
            bg="light goldenrod",
            padx=2,
            pady=2,
        )
        _frame_grafo_malha.grid(row=6, columnspan=10, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        def __show_grafo(a, grafo, pos, f):
            _frame_grafo_malha = tk.Frame(
                master=frame_config,
                bg="light goldenrod",
                padx=2,
                pady=2,
            )
            _frame_grafo_malha.grid(row=6, columnspan=10, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

            nx.draw(grafo, pos, node_color='black', ax=a)

            canvas = FigureCanvasTkAgg(f, master=_frame_grafo_malha)
            canvas.draw()
            canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

            toolbar_grafo = NavigationToolbar2Tk(canvas, _frame_grafo_malha)
            toolbar_grafo.update()
            canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # BOTÃO ADICIONAR Adicionar dimensões
        def __add_butt_dimensoes():
            largura = float(entry_malha_largura.get())
            print('\n\nlargura malha = ', largura)

            comprimento = float(entry_malha_comprimento.get())
            print('\n\ncomprimento malha = ', comprimento)

            esp_larg = float(entry_malha_esp_larg.get())
            print('\n\nEspaçamento malha largura = ', esp_larg)

            esp_compr = float(entry_malha_esp_compr.get())
            print('\n\nEspaçamento malha comprimento = ', esp_compr)

            profundidade = float(entry_malha_profundidade.get())
            print('\n\nprofundidade malha = ', profundidade)

            periferia = bool(__hastes_periferia.get())
            print('\n\nHastes na periferia? ', periferia)

            if periferia is True:
                periferia_true = True
                periferia_false = False
            else:
                periferia_true = False
                periferia_false = True

            self.__malha.add_dimensoes(
                largura=largura,
                comprimento=comprimento,
                esp_larg=esp_larg,
                esp_compr=esp_compr,
                profundidade_malha=profundidade,
                malha_com_hastes_na_periferia=periferia_true,
                malha_sem_hastes_na_periferia=periferia_false
            )

            __grafo_malha = nx.Graph()

            f = Figure(figsize=(5, 4), dpi=100)
            a = f.add_subplot()

            na = int(largura * esp_larg)
            nb = int(comprimento * esp_compr)

            nodes = []
            for i in range(na * nb):
                nodes.append(str(i + 1))
            pos = dict()
            cont = 0
            for i in range(nb):
                for j in range(na):
                    pos[nodes[cont]] = (j + 1, i + 1)
                    cont += 1
            __grafo_malha.add_nodes_from(nodes)

            edges = []
            for i in range(na):
                edges.append(
                    (nodes[i], nodes[(na * nb) - na + i])
                )
            for i in range(nb):
                edges.append(
                    (nodes[i * na], nodes[na + (i * na) - 1])
                )
            __grafo_malha.add_edges_from(edges)

            _frame_grafo_malha.destroy()
            __show_grafo(a=a, grafo=__grafo_malha, pos=pos, f=f)

        butt_add_dimensoes = tk.Button(
            master=_frame_dimensoes,
            text="Adicionar informações  e mostrar malha de terra!", font=("Helvetica", 12), height=1,  # width=10,
            bg="goldenrod",
            bd=3,
            command=__add_butt_dimensoes,
            anchor=tk.CENTER,
            justify=tk.CENTER,
            compound=tk.CENTER,
            padx=2,
            pady=2,
            relief=tk.GROOVE,
        )
        butt_add_dimensoes.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # BOTÃO Salvar informações
        def __add_butt_salvar_malha():
            config_malha.destroy()

        butt_add_dimensoes = tk.Button(
            master=frame_config,
            text="Salvar informações da malha e sair!", font=("Helvetica", 12), height=1,  # width=10,
            bg="goldenrod",
            bd=3,
            command=__add_butt_salvar_malha,
            anchor=tk.CENTER,
            justify=tk.CENTER,
            compound=tk.CENTER,
            padx=2,
            pady=2,
            relief=tk.GROOVE,
        )
        butt_add_dimensoes.grid(row=7, columnspan=10, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

    ########################################################################################################################

    #######################################################################################################

    def __add_solo(self, event):
        self.__config_solo()
        self.__text_status.set("Adicionando informações do solo! ")

    def __config_solo(self):
        config_solo = tk.Toplevel()
        config_solo.title("Configurações do solo")
        config_solo.geometry("1060x900")
        config_solo.wm_iconbitmap("images/logo_pySEP.ico")
        config_solo["bg"] = "light goldenrod"

        frame_config = tk.Frame(
            master=config_solo,
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
            text="Configurações do solo",
            font=("Helvetica", 20)
        )
        label_titulo.grid(row=0, columnspan=8, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # BOTÃO SALVAR INFORMAÇÕES SOLOS
        def __add_butt():
            config_solo.destroy()

        butt_salvar_solos = tk.Button(
            master=frame_config,
            text="Salvar informações! ", font=("Helvetica", 11), height=2, width=10,
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
        butt_salvar_solos.grid(row=0, column=8, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> LABEL Brita
        label_brita = tk.Label(
            master=frame_config,
            text="Adicionar Informações da camada de Brita ",
            font=("Helvetica", 20),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_brita.grid(row=1, columnspan=10, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> LABEL Brita PROFUNDIDADE
        label_brita_profundidade = tk.Label(
            master=frame_config,
            text="Profundidade [m]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_brita_profundidade.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> ENTRY Brita PROFUNDIDADE

        entry_brita_profundidade = tk.Entry(
            font=("Helvetica", 12),

            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_brita_profundidade.focus_set()
        entry_brita_profundidade.grid(row=2, column=2, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> LABEL Brita RESISTIVIDADE
        label_brita_resistividade = tk.Label(
            master=frame_config,
            text="Resistividade [Ohm.m]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_brita_resistividade.grid(row=2, column=4, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> ENTRY Brita RESISTIVIDADE

        entry_brita_resistividade = tk.Entry(
            font=("Helvetica", 12),

            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )

        entry_brita_resistividade.grid(row=2, column=6, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # BOTÃO ADICIONAR BRITA
        def __add_butt():
            profundidade = float(entry_brita_profundidade.get())
            print('\n\nprofundidade = ', profundidade)

            resistividade = float(entry_brita_resistividade.get())
            print('\n\nresistividade = ', resistividade)

            self.__malha.add_info_brita(profundidade=profundidade,
                                        resistividade=resistividade)

            self.__malha.show_solo()

            set_color_solo(profundidade=profundidade, num_camada=0, resistividade=resistividade, nome="Brita")

        butt_add_brita = tk.Button(
            master=frame_config,
            text="Adicionar informações da camada de Brita!", font=("Helvetica", 12), height=1,  # width=10,
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
        butt_add_brita.grid(row=2, column=8, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> LABEL Solo n
        label_solo = tk.Label(
            master=frame_config,
            text="Adicionar nova camada de solo: ",
            font=("Helvetica", 20),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_solo.grid(row=3, columnspan=10, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> LABEL Solo PROFUNDIDADE
        label_solo_profundidade = tk.Label(
            master=frame_config,
            text="Profundidade [m]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_solo_profundidade.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> ENTRY Solo PROFUNDIDADE

        entry_solo_profundidade = tk.Entry(
            font=("Helvetica", 12),
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_solo_profundidade.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> LABEL Solo RESISTIVIDADE
        label_solo_resistividade = tk.Label(
            master=frame_config,
            text="Resistividade [Ohm.m]: ",
            font=("Helvetica", 12),
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
        )
        label_solo_resistividade.grid(row=4, column=4, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # Informações --> ENTRY Solo RESISTIVIDADE

        entry_solo_resistividade = tk.Entry(
            font=("Helvetica", 12),
            master=frame_config,
            justify=tk.CENTER,
            bd=2,
            bg="light goldenrod",
            relief=tk.GROOVE
        )
        entry_solo_resistividade.grid(row=4, column=6, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        # BOTÃO ADICIONAR BRITA
        def __add_butt():
            self.__malha.set_num_solo()
            num_camada = self.__malha.get_num_solo()

            profundidade = float(entry_solo_profundidade.get())
            print('\n\nprofundidade = ', profundidade)

            resistividade = float(entry_solo_resistividade.get())
            print('\n\nresistividade = ', resistividade)

            self.__malha.add_info_solo(num_camada=num_camada,
                                       profundidade=profundidade,
                                       resistividade=resistividade)

            self.__malha.show_solo()
            set_color_solo(profundidade=profundidade, num_camada=num_camada, resistividade=resistividade,
                           nome="H" + str(num_camada))

        frame_solos = tk.Frame(
            master=frame_config,
            bg="light goldenrod",

        )
        frame_solos.grid(row=5, columnspan=10, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

        def set_color_solo(profundidade, resistividade, num_camada, nome):
            cores = ["white", "brown", "red", "yellow", "blue", "black", "green"]
            frame = tk.LabelFrame(
                master=frame_solos,
                width=1050,
                height=profundidade * 150,
                bg=cores[num_camada],
                text="\t\tNome: " + str(nome) + "\t\tProfundidade: " + str(
                    profundidade) + " [m]\t\tResistividade: " + str(resistividade) + " [Ohm.m]",
                font=("Helvetica", 12),
            )
            frame.pack(fill=tk.BOTH, expand=True)

        butt_add_solo = tk.Button(
            master=frame_config,
            text="Adicionar informações da camada de Solo!", font=("Helvetica", 12), height=1,  # width=10,
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
        butt_add_solo.grid(row=4, column=8, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

    def __add_bar(self, event):
        self.__config_bar()
        self.__text_status.set("Adicionando uma nova barra! ")

    def __s_base(self):
        s_base = tk.Toplevel(master=self.__janela)
        s_base.title("\tBem-vindo ao pySEP!!\t")
        s_base.geometry("500x175+500+500")
        s_base.wm_iconbitmap("images/logo_pySEP.ico")
        s_base["bg"] = "light goldenrod"

        label_s_base = tk.Label(
            master=s_base,
            anchor=tk.CENTER,
            bg="light goldenrod",
            justify=tk.CENTER,
            padx=2,
            pady=2,
            text="Defina um valor base para o sistema em [VA]!\nInserir conforme exemplo: 100e6",
            font=("Helvetica", 18)
        )
        label_s_base.grid(row=0, columnspan=3, padx=5, pady=5)

        frame_s_base = tk.Entry(
            font=("Helvetica", 15),

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
        config_bar.geometry("1000x275")
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
            font=("Helvetica", 15),

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
            font=("Helvetica", 15),

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
            font=("Helvetica", 15),

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
            font=("Helvetica", 15),

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
            font=("Helvetica", 15),

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
<<<<<<< HEAD
                self.__show_grafo()
=======
                self.__grafo_add_node(list_numBar=self.__circuito.getBarras())
                self.__label_logo.destroy()
>>>>>>> 61cee31 (logo adicionada)
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
        config_lin.geometry("815x275")
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
            font=("Helvetica", 15),

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
            font=("Helvetica", 15),

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
            font=("Helvetica", 15),

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
                self.__label_logo.destroy()
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

    ############################## PROTEÇÃO ########################################

    # ## DESENHAR CIRCUITO DO SISTEMA :
    # def __protecao_draw_ckt(self):
    #     config_draw_prot = tk.Toplevel()
    #     config_draw_prot.title("Modelagem do Circuito Considerado")
    #     config_draw_prot.geometry("1100x700")
    #     config_draw_prot.wm_iconbitmap("images/logo_pySEP.ico")
    #     config_draw_prot["bg"] = "light goldenrod"
    #
    #     frame_info_draw_prot = tk.LabelFrame(
    #         master=config_draw_prot,
    #         bg="light goldenrod",
    #         text="Informações Preliminares",
    #         font=("Helvetica", 20)
    #     )
    #     frame_info_draw_prot.pack(fill='both', expand=True)
    #
    #     # LABEL ADD Número de nós do sistema
    #     label_add_num_nos = tk.Label(
    #         master=frame_info_draw_prot,
    #         text="Número de Nós do Sisema: ",
    #         font=("Helvetica", 15),
    #         justify=tk.CENTER,
    #         bd=2,
    #         bg="light goldenrod",
    #     )
    #     label_add_num_nos.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
    #
    #     entry_add_num_nos = tk.Entry(
    #         font=("Helvetica", 15),
    #         master=frame_info_draw_prot,
    #         justify=tk.CENTER,
    #         bd=2,
    #         bg="light goldenrod",
    #         relief=tk.GROOVE
    #     )
    #     entry_add_num_nos.focus_set()
    #     entry_add_num_nos.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
    #
    #     # LABEL ADD Imalha
    #     label_add_imalha = tk.Label(
    #         master=frame_info_draw_prot,
    #         text="Corrente de malha [A]: ",
    #         font=("Helvetica", 15),
    #         justify=tk.CENTER,
    #         bd=2,
    #         bg="light goldenrod",
    #     )
    #     label_add_imalha.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
    #
    #     entry_add_imalha = tk.Entry(
    #         font=("Helvetica", 15),
    #         master=frame_info_malha,
    #         justify=tk.CENTER,
    #         bd=2,
    #         bg="light goldenrod",
    #         relief=tk.GROOVE
    #     )
    #     entry_add_imalha.grid(row=0, column=4, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)

    # # LABEL ADD tempo protecao
    # label_add_t_protecao = tk.Label(
    #     master=frame_info_malha,
    #     text="Tempo da proteção [s]: ",
    #     font=("Helvetica", 15),
    #     justify=tk.CENTER,
    #     bd=2,
    #     bg="light goldenrod",
    # )
    # label_add_t_protecao.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
    #
    # entry_add_t_protecao = tk.Entry(
    #     font=("Helvetica", 15),
    #     master=frame_info_malha,
    #     justify=tk.CENTER,
    #     bd=2,
    #     bg="light goldenrod",
    #     relief=tk.GROOVE
    # )
    # entry_add_t_protecao.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
    #
    # # LABEL ADD tempo defeito
    # label_add_t_defeito = tk.Label(
    #     master=frame_info_malha,
    #     text="Tempo do defeito [s]: ",
    #     font=("Helvetica", 15),
    #     justify=tk.CENTER,
    #     bd=2,
    #     bg="light goldenrod",
    # )
    # label_add_t_defeito.grid(row=1, column=3, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
    #
    # entry_add_t_defeito = tk.Entry(
    #     font=("Helvetica", 15),
    #     master=frame_info_malha,
    #     justify=tk.CENTER,
    #     bd=2,
    #     bg="light goldenrod",
    #     relief=tk.GROOVE
    # )
    # entry_add_t_defeito.grid(row=1, column=4, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
    #
    # # LABEL ADD temperatura ambiente
    # label_add_temp_ambiente = tk.Label(
    #     master=frame_info_malha,
    #     text="Temperatura ambiente [C°]: ",
    #     font=("Helvetica", 15),
    #     justify=tk.CENTER,
    #     bd=2,
    #     bg="light goldenrod",
    # )
    # label_add_temp_ambiente.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
    #
    # entry_add_temp_ambiente = tk.Entry(
    #     font=("Helvetica", 15),
    #     master=frame_info_malha,
    #     justify=tk.CENTER,
    #     bd=2,
    #     bg="light goldenrod",
    #     relief=tk.GROOVE
    # )
    # entry_add_temp_ambiente.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
    #
    # # LABEL ADD temperatura máxima permissível
    # label_add_temp_max_permissivel = tk.Label(
    #     master=frame_info_malha,
    #     text="Temperatura máxima permissível [C°]: ",
    #     font=("Helvetica", 15),
    #     justify=tk.CENTER,
    #     bd=2,
    #     bg="light goldenrod",
    # )
    # label_add_temp_max_permissivel.grid(row=2, column=3, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
    #
    # entry_add_temp_max_permissivel = tk.Entry(
    #     font=("Helvetica", 15),
    #     master=frame_info_malha,
    #     justify=tk.CENTER,
    #     bd=2,
    #     bg="light goldenrod",
    #     relief=tk.GROOVE
    # )
    # entry_add_temp_max_permissivel.grid(row=2, column=4, padx=5, pady=5, sticky=tk.W + tk.E + tk.N + tk.S)
    #
    # # BOTÃO ADICIONAR
    # def __add_butt_salvar():
    #     icc = float(entry_add_icc.get())
    #     print('\n\nIcc = ', icc)
    #
    #     imalha = float(entry_add_imalha.get())
    #     print('Imalha = ', imalha)
    #
    #     t_prot = float(entry_add_t_protecao.get())
    #     print('tempo protecao = ', t_prot)
    #
    #     t_def = float(entry_add_t_defeito.get())
    #     print('tempo defeito = ', t_def)
    #
    #     temp_amb = int(entry_add_temp_ambiente.get())
    #     print('temperatura ambiente = ', temp_amb)
    #
    #     temp_max = int(entry_add_temp_max_permissivel.get())
    #     print('temperatura maxima = ', temp_max)
    #
    #     self.__malha.add_icc(i_cc=icc)
    #     self.__malha.add_i_malha(i_malha=imalha)
    #     self.__malha.add_t_protecao(t_protecao=t_prot)
    #     self.__malha.add_t_defeito(t_defeito=t_def)
    #     self.__malha.add_temp_ambiente(temp_ambiente=temp_amb)
    #     self.__malha.add_temp_max_permissivel(temp_max_permissivel=temp_max)
    #
    #     config_info_malha.destroy()
    #
    # butt_add_salvar = tk.Button(
    #     master=frame_info_malha,
    #     text="Salvar!", font=("Helvetica", 12), height=2,  # width=30,
    #     bg="goldenrod",
    #     bd=3,
    #     command=__add_butt_salvar,
    #     anchor=tk.CENTER,
    #     justify=tk.CENTER,
    #     compound=tk.CENTER,
    #     padx=2,
    #     pady=2,
    #     relief=tk.GROOVE,
    # )
    # butt_add_salvar.grid(row=3, columnspan=5, padx=5, pady=5)

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

    @staticmethod
    def set_janela(janela_main):
        janela_main.title("pySEP    -    Python em Sistemas Elétricos de Potência!")
        janela_main.geometry("1280x720+100+100")
        janela_main.wm_iconbitmap("images/logo_pySEP.ico")
        janela_main["bg"] = "light goldenrod"
        janela_main["bd"] = 5

    def bemvindo(self, event):
        self.__text_status.set("Bem-vindo ao pySEP!")

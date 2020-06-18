from .buses import *
from .fluxo import *
from .lines import *
from .jcb import jcb_setJacob
from .plotagem import plt_plotData


class Circuito:
    def __init__(self, sBase):
        self.sBase = sBase
        self.__count = 0
        self.__dic = {
            'data': dict(),
            'lines': dict(),
            'fluxo': {'Sbase': self.sBase,
                      'Sesp': dict(),
                      'deltaPQ': list(),
                      'resP': list(),
                      'resQ': list(),
                      },
            'nPQV': {'nPQ': int(),
                     'nPV': int(),
                     'listAngTens': {'ang': list(),
                                     'tensao': list()},
                     },
            'plot': {'tensao': dict(),
                     'ang': dict()},
            'ybus': list(),
            'jacobiana': dict(),
        }
        self.__tensoes = dict(),
        self.__correntes = dict(),
        self.__fluxo = dict(),
        self.__perdas = float()

    def set_s_base(self, sBase):
        self.sBase = sBase

    def addBarra(self, barra, code, tensao, ang, carga, geracao):
        bs_addBarra(dicBarras=self.__dic['data'], dicFlow=self.__dic['fluxo'],
                    barra=barra, code=code,
                    tensao=tensao, ang=ang,
                    carga=carga, geracao=geracao)

    def showBarras(self):
        bs_showBuses(self.__dic['data'], self.__dic['fluxo'])

    def getBarras(self):
        """
        :return: list
        """
        lista_barras = [i for i in self.__dic['data']]
        return lista_barras

    def addLinha(self, b1, b2, z_ij):
        ln_addLine(dic=self.__dic['lines'], b1=b1, b2=b2, z_ij=z_ij)

    def showLinhas(self):
        ln_showLines(self.__dic['lines'])

    def getLinhas(self):
        """
        :return: list
        """
        lista_linhas = []
        for i in self.__dic['lines']:
            b12 = tuple([i[0], i[1]])
            lista_linhas.append(tuple([i[0], i[1], {'z': self.__dic['lines'][b12].get('z')}]))
        return lista_linhas

    def ybus(self, show):
        bs_setSesp(dicBarras=self.__dic['data'], dicFlow=self.__dic['fluxo'])
        bs_add_plot(dicBarras=self.__dic['data'], dicPlot=self.__dic['plot'])
        bs_add_nPQV(dicBarras=self.__dic['data'], dicNPQV=self.__dic['nPQV'])
        self.__dic['ybus'] = ln_ybus(self.__dic, showYbus=show)

    def pot_inj(self, show):
        fl_pot_injetada(self.__dic['data'], self.__dic['fluxo'], self.__dic['ybus'], count=self.__count, show=show)

    def jacobiana(self, show):
        self.__dic['jacobiana'] = jcb_setJacob(dicBarras=self.__dic['data'],
                                               yBus=self.__dic['ybus'],
                                               dicNpqv=self.__dic['nPQV'],
                                               showSubs=show)

    def sis_linear(self):
        fl_sist_linear(dicBarras=self.__dic['data'],
                       dicFlow=self.__dic['fluxo'],
                       dic_nPQV=self.__dic['nPQV'],
                       plot=self.__dic['plot'],
                       jacob=self.__dic['jacobiana'])

    def n_pot_inj(self):
        fl_nova_inj(dicBarras=self.__dic['data'],
                    yBus=self.__dic['ybus'])

    def calcular_fluxo_pot_nr(self, show, erro):
        self.ybus(True)
        self.pot_inj(show=show)
        self.jacobiana(show=show)
        self.sis_linear()
        self.__count += 1

        self.showBarras()

        pq = list(map(abs, self.__dic['fluxo'].get('deltaPQ')))
        test = list(map(lambda m: True if (m < erro) else False, pq))
        stop = test.count(False)

        if stop > 0:
            while True:
                self.pot_inj(show=show)
                self.jacobiana(show=show)
                self.sis_linear()

                pq = list(map(abs, self.__dic['fluxo'].get('deltaPQ')))
                test = list(map(lambda m: True if (m < erro) else False, pq))
                stop = test.count(False)

                if stop == 0:
                    self.__count += 1
                    break
                if self.__count == 30:
                    self.__count += 1
                    break
                self.__count += 1
                self.showBarras()

        self.n_pot_inj()

        print('\n\nlistTensao: ', self.__dic['nPQV']['listAngTens'].get('tensao'))
        print('listAng: ', self.__dic['nPQV']['listAngTens'].get('ang'))
        print('\n\nnPQ: ', self.__dic['nPQV'].get('nPQ'))
        print('nPV: ', self.__dic['nPQV'].get('nPV'))

        print('CONVERGIU PARA UM ERRO DE ', erro, ' .')
        print('CONVERGIU EM ', self.__count, ' ITERAÇÕES. ')

    def relatorio(self, show_tensoes=False, show_correntes=False, show_fluxo=False):
        self.__tensoes = bs_tensoes(dicBarras=self.__dic['data'], show=show_tensoes)
        self.__correntes = ln_correntes(dicBarras=self.__dic['data'], dic_tensoes=self.__tensoes,
                                        ybus=self.__dic['ybus'],
                                        show=show_correntes)
        self.__fluxo = fl_fluxo(dic_barras=self.__dic['data'], dic_corr=self.__correntes, dic_v=self.__tensoes,
                                show=show_fluxo)

    def perdas(self, show):
        self.relatorio()
        self.__perdas = fl_perdas(dic_fluxo=self.__fluxo, show=show)

    def plot_conv(self, tensao, ang):
        plt_plotData(cont=self.__count, dic_barras=self.__dic['data'],
                     dic_tens_plot=self.__dic['plot'].get('tensao'),
                     dic_ang_plot=self.__dic['plot'].get('ang'),
                     tensao=tensao,
                     ang=ang)

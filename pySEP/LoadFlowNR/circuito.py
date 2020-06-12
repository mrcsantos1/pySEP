import buses as bs
import fluxo as fl
import lines as ln
import jcb as jcb


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

    def addBarra(self, barra, code, tensao, ang, carga, geracao):
        bs.addBarra(dicBarras=self.__dic['data'], dicFlow=self.__dic['fluxo'],
                    barra=barra, code=code,
                    tensao=tensao, ang=ang,
                    carga=carga, geracao=geracao)

    def showBarras(self):
        bs.showBuses(self.__dic['data'], self.__dic['fluxo'])

    def addLinha(self, b1, b2, z_ij):
        ln.addLine(dic=self.__dic['lines'], b1=b1, b2=b2, z_ij=z_ij)

    def showLinhas(self):
        ln.showLines(self.__dic['lines'])

    def ybus(self, show):
        bs.setSesp(dicBarras=self.__dic['data'], dicFlow=self.__dic['fluxo'])
        bs.add_plot(dicBarras=self.__dic['data'], dicPlot=self.__dic['plot'])
        bs.add_nPQV(dicBarras=self.__dic['data'], dicNPQV=self.__dic['nPQV'])
        self.__dic['ybus'] = ln.ybus(self.__dic, showYbus=show)

    def pot_inj(self, show):
        fl.pot_injetada(self.__dic['data'], self.__dic['fluxo'], self.__dic['ybus'], count=self.__count, show=show)

        print('\ndelta pq = ', self.__dic['fluxo'].get('deltaPQ'))

    def jacobiana(self, show):
        self.__dic['jacobiana'] = jcb.setJacob(dicBarras=self.__dic['data'],
                                               resP=self.__dic['fluxo'].get('resP'),
                                               resQ=self.__dic['fluxo'].get('resQ'),
                                               yBus=self.__dic['ybus'],
                                               dicNpqv=self.__dic['nPQV'],
                                               showSubs=show)

    def sis_linear(self):
        fl.sist_linear(dicBarras=self.__dic['data'],
                       dicFlow=self.__dic['fluxo'],
                       dic_nPQV=self.__dic['nPQV'],
                       plot=self.__dic['plot'],
                       jacob=self.__dic['jacobiana'])

    def n_pot_inj(self):
        fl.nova_inj(dicBarras=self.__dic['data'],
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
<<<<<<< HEAD
<<<<<<< HEAD
                if self.__count == 2:
=======
                if self.__count == 100:
>>>>>>> ef123a1 (8barras ok GLÓRIA A DEUSSSS)
=======
                if self.__count == 10:
>>>>>>> 13fa90e (Terminar próximos passos e começar GUI)
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
        self.__tensoes = bs.tensoes(dicBarras=self.__dic['data'], show=show_tensoes)
        self.__correntes = ln.correntes(dicBarras=self.__dic['data'], dic_tensoes=self.__tensoes,
                                        ybus=self.__dic['ybus'],
                                        show=show_correntes)
        self.__fluxo = fl.fluxo(dic_barras=self.__dic['data'], dic_corr=self.__correntes, dic_v=self.__tensoes,
                                show=show_fluxo)

<<<<<<< HEAD
#
=======

a = Circuito(sBase=100e6)

a.addBarra(barra=1, code=1, tensao=1.00, ang=0.00, carga=0.0j, geracao=0 + 0j)
a.addBarra(barra=2, code=2, tensao=1.00, ang=0.00, carga=100e6 + 20e6 * 1j, geracao=0 + 0j)
a.addBarra(barra=3, code=2, tensao=1.00, ang=0.00, carga=150e6 + 20e6 * 1j, geracao=0 + 0j)
a.addBarra(barra=4, code=3, tensao=1.05, ang=0.00, carga=0.0j, geracao=300e6 + 0j)
a.addBarra(barra=5, code=2, tensao=1.00, ang=0.00, carga=50e6 + 0 * 1j, geracao=0 + 0j)
a.addBarra(barra=6, code=2, tensao=1.00, ang=0.00, carga=100e6 + 0 * 1j, geracao=0 + 0j)
a.addBarra(barra=7, code=3, tensao=1.05, ang=0.00, carga=0 + 0 * 1j, geracao=300e6 + 0j)
a.addBarra(barra=8, code=2, tensao=1.00, ang=0.00, carga=100e6 + 20e6 * 1j, geracao=0 + 0j)
a.addBarra(barra=9, code=2, tensao=1.00, ang=0.00, carga=50e6 + 0 * 1j, geracao=0 + 0j)

a.addLinha(b1=1, b2=2, z_ij=0.01 + 0.005j)
a.addLinha(b1=1, b2=3, z_ij=0.01 + 0.015j)
a.addLinha(b1=1, b2=4, z_ij=0.005 + 0.025j)
a.addLinha(b1=1, b2=5, z_ij=0.01 + 0.02j)
a.addLinha(b1=4, b2=6, z_ij=0.01 + 0.015j)
a.addLinha(b1=3, b2=7, z_ij=0.01 + 0.005j)
a.addLinha(b1=7, b2=8, z_ij=0.01 + 0.025j)
a.addLinha(b1=2, b2=9, z_ij=0.01 + 0.005j)

a.calcular_fluxo_pot_nr(show=True, erro=0.01)

a.showBarras()

<<<<<<< HEAD
>>>>>>> ef123a1 (8barras ok GLÓRIA A DEUSSSS)
=======
a.relatorio()

>>>>>>> 12c412b (relatorios)
# c = Circuito(sBase=100e6)
#
# c.addBarra(1, 1, 1.05, 0, 0 + 0 * 1j, 0 + 0 * 1j)
# c.addBarra(2, 2, 1.00, 0, 256.6e6 + 110.2e6 * 1j, 0 + 0 * 1j)
# c.addBarra(3, 2, 1.00, 0, 138.6e6 + 45.2e6 * 1j, 0 + 0 * 1j)
#
# # c.setSesp()
#
# c.addLinha(1, 2, 0.02 + 0.04j)
# c.addLinha(1, 3, 0.01 + 0.03j)
# c.addLinha(2, 3, 0.0125 + 0.025j)

# c.ybus(True)

# c.pot_inj(True)
#
# c.jacobiana(True)
#
# c.sis_linear()
#
# c.n_pot_inj()
#
# c.showBarras()
#
# c.calcular_fluxo_pot_nr(show=True, erro=0.001)
#
# c.showBarras()
#
# a = Circuito(sBase=100e6)
# a.addBarra(barra=1, code=1, tensao=1.000, ang=0, carga=0 + 0 * 1j, geracao=0 + 0 * 1j)
# a.addBarra(barra=2, code=2, tensao=1.000, ang=0, carga=100e6 + 50e6 * 1j, geracao=0 + 0 * 1j)
#
# # a.setSesp()
#
# a.addLinha(1, 2, 0.1 + 0.2j)
#
# a.calcular_fluxo_pot_nr(show=True, erro=0.00001)
# a.showBarras()
#
# b = Circuito(sBase=100e6)
# b.addBarra(barra=1, code=1, tensao=1.000, ang=0, carga=0 + 0 * 1j, geracao=0 + 0 * 1j)
# b.addBarra(barra=2, code=2, tensao=1.000, ang=0, carga=100e6 + 50e6 * 1j, geracao=0 + 0 * 1j)
# b.addBarra(barra=3, code=2, tensao=1.000, ang=0, carga=100e6 + 50e6 * 1j, geracao=0 + 0 * 1j)
# b.addBarra(barra=4, code=3, tensao=1.050, ang=0, carga=0 + 0 * 1j, geracao=200e6 + 0 * 1j)
#
#
# b.addLinha(1, 2, 0.1 + 0.15j)
# b.addLinha(1, 3, 0.1 + 0.15j)
# b.addLinha(2, 4, 0.1 + 0.15j)
# b.addLinha(3, 4, 0.1 + 0.15j)
#
# b.calcular_fluxo_pot_nr(show=True, erro=0.00000001)
# b.showBarras()

<<<<<<< HEAD
_3barras = Circuito(sBase=100e6)

_3barras.addBarra(barra=1, code=1, tensao=1.025, ang=0, carga=0 + 0 * 1j, geracao=0 + 0 * 1j)
_3barras.addBarra(barra=2, code=2, tensao=1.00, ang=0, carga=400e6 + 200e6 * 1j, geracao=0 + 0 * 1j)
_3barras.addBarra(barra=3, code=3, tensao=1.03, ang=0, carga=0 + 0 * 1j, geracao=300e6 + 0 * 1j)

<<<<<<< HEAD
=======
=======
# _3barras = Circuito(sBase=100e6)
#
# _3barras.addBarra(barra=1, code=1, tensao=1.025, ang=0, carga=0 + 0 * 1j, geracao=0 + 0 * 1j)
# _3barras.addBarra(barra=2, code=2, tensao=1.00, ang=0, carga=400e6 + 200e6 * 1j, geracao=0 + 0 * 1j)
# _3barras.addBarra(barra=3, code=3, tensao=1.03, ang=0, carga=0 + 0 * 1j, geracao=300e6 + 0 * 1j)
#
#
# _3barras.addLinha(1, 2, 0.1j)
# _3barras.addLinha(1, 3, 0.05j)
# _3barras.addLinha(2, 3, 0.01j)
#
#
# _3barras.calcular_fluxo_pot_nr(show=True, erro=0.00000001)
# _3barras.showBarras()
>>>>>>> 9c7f9d8 (5 barras divergiu!)


# DIVERGIU! TESTAR A IMPLEMENTAÇÃO DE UM COMPARADOR PARA V(k+1) NÃO SER MUITO DIFERENTE DE V(k), por exemplo
# b = Circuito(sBase=100e6)
#
# b.addBarra(barra=2, code=1, tensao=1.000, ang=0, carga=0 + 0 * 1j, geracao=0 + 0 * 1j)
#
# b.addBarra(barra=1, code=2, tensao=1.000, ang=0, carga=100e6 + 50e6 * 1j, geracao=0 + 0 * 1j)
# b.addBarra(barra=3, code=2, tensao=1.000, ang=0, carga=200e6 + 50e6 * 1j, geracao=0 + 0 * 1j)
# b.addBarra(barra=5, code=2, tensao=1.000, ang=0, carga=200e6 + 50e6 * 1j, geracao=0 + 0 * 1j)
#
# b.addBarra(barra=4, code=3, tensao=1.050, ang=0, carga=0 + 0 * 1j, geracao=100e6 + 0 * 1j)
#
# b.addLinha(1, 2, 0.02 + 0.05j)
# b.addLinha(1, 5, 0.05 + 0.22j)
# b.addLinha(2, 5, 0.06 + 0.17j)
# b.addLinha(2, 4, 0.06 + 0.18j)
# b.addLinha(2, 3, 0.05 + 0.20j)
# b.addLinha(3, 4, 0.07 + 0.17j)
# b.addLinha(4, 5, 0.02 + 0.05j)
#
# b.calcular_fluxo_pot_nr(show=True, erro=0.1)
# b.showBarras()

<<<<<<< HEAD
<<<<<<< HEAD
_3barras.calcular_fluxo_pot_nr(show=True, erro=0.00000001)
_3barras.showBarras()
>>>>>>> 6014b20 (!)
=======
>>>>>>> 9c7f9d8 (5 barras divergiu!)
=======
#
# b = Circuito(sBase=100e6)
#
# b.addBarra(barra=1, code=1, tensao=1.050, ang=0, carga=0 + 0 * 1j, geracao=0 + 0 * 1j)
#
# b.addBarra(barra=3, code=3, tensao=1.050, ang=0, carga=0 + 0 * 1j, geracao=300e6 + 0 * 1j)
# b.addBarra(barra=6, code=3, tensao=1.050, ang=0, carga=0 + 0 * 1j, geracao=200e6 + 0 * 1j)
#
# b.addBarra(barra=2, code=2, tensao=1.000, ang=0, carga=150e6 + 25e6 * 1j, geracao=0 + 0 * 1j)
# b.addBarra(barra=4, code=2, tensao=1.000, ang=0, carga=200e6 + 50e6 * 1j, geracao=0 + 0 * 1j)
# b.addBarra(barra=5, code=2, tensao=1.000, ang=0, carga=100e6 + 50e6 * 1j, geracao=0 + 0 * 1j)
# b.addBarra(barra=7, code=2, tensao=1.000, ang=0, carga=200e6 + 50e6 * 1j, geracao=0 + 0 * 1j)
# b.addBarra(barra=8, code=2, tensao=1.000, ang=0, carga=200e6 + 50e6 * 1j, geracao=0 + 0 * 1j)
# b.addBarra(barra=9, code=2, tensao=1.000, ang=0, carga=100e6 + 25e6 * 1j, geracao=0 + 0 * 1j)
#
# b.addLinha(1, 7, 0.1 + 0.15j)
# b.addLinha(1, 8, 0.1 + 0.15j)
# b.addLinha(1, 6, 0.1 + 0.15j)
#
# b.addLinha(2, 3, 0.1 + 0.15j)
# b.addLinha(2, 4, 0.1 + 0.15j)
#
# b.addLinha(4, 5, 0.1 + 0.15j)
# b.addLinha(4, 9, 0.1 + 0.15j)
#
# b.addLinha(5, 6, 0.1 + 0.15j)
#
# b.addLinha(7, 8, 0.1 + 0.15j)
#
# b.addLinha(8, 9, 0.1 + 0.15j)
#
# b.calcular_fluxo_pot_nr(show=True, erro=0.1)
# b.showBarras()
>>>>>>> ef123a1 (8barras ok GLÓRIA A DEUSSSS)

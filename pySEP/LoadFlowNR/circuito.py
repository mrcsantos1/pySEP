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
                if self.__count == 20:
                    self.__count += 1
                    break
                self.__count += 1
                self.showBarras()

        self.n_pot_inj()

        print('CONVERGIU PARA UM ERRO DE ', erro, ' .')
        print('CONVERGIU EM ', self.__count, ' ITERAÇÕES. ')

    def get_npqv(self):
        print(self.__dic.get('nPQV'))


c = Circuito(sBase=100e6)

c.addBarra(1, 1, 1.05, 0, 0 + 0 * 1j, 0 + 0 * 1j)
c.addBarra(2, 2, 1.00, 0, 256.6e6 + 110.2e6 * 1j, 0 + 0 * 1j)
c.addBarra(3, 2, 1.00, 0, 138.6e6 + 45.2e6 * 1j, 0 + 0 * 1j)

# c.setSesp()

c.addLinha(1, 2, 0.02 + 0.04j)
c.addLinha(1, 3, 0.01 + 0.03j)
c.addLinha(2, 3, 0.0125 + 0.025j)

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

c.calcular_fluxo_pot_nr(show=True, erro=0.1)

c.showBarras()

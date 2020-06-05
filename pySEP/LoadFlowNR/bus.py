import numpy as np
import math as mt


class Bus:
    def __init__(self):
        self._data = dict()
        self._Sesp = dict()
        self._tensaoPlot = dict()
        self._angPlot = dict()

        self.__Sbase = 100e6

        self._nPQ = int()
        self._nPV = int()

    def addBus(self, barra, code, tensao, ang, carga, geracao):
        self._data[barra] = {'code': code, 'tensao': tensao, 'ang': mt.radians(ang),
                             'carga': (carga / self.__Sbase), 'geracao': (geracao / self.__Sbase)}
        self._tensaoPlot[barra] = [tensao]
        self._angPlot[barra] = [ang]

        if code == 2:
            self._nPQ += 1
        elif code == 3:
            self._nPV += 1

    def relatorioBarras(self):
        """
            Método utilizado para printar todos os valores em cada barra.
        """
        print('\n\n=============================== DADOS: =================================')
        print('Sbase = ', self.__Sbase, ' VA')
        for i in self._data:
            self._data[i]['ang'] = mt.degrees(self._data.get(i)['ang'])
            print(self._data[i])
        print('========================================================================')

    def showBuses(self):
        print('\n\n=============================== DADOS: =================================')
        print('Sbase = ', self.__Sbase, ' VA')
        for i in self._data:
            print('Barra: ', i, '\t', end='')
            print(self._data[i])
        print('========================================================================')

    def setSesp(self, showSesp=False):
        """
        Método utilizado para calcular a potência especificada em cada barra.
        """
        for i in self._data:
            if self._data[i]['code'] == 2:
                self._Sesp[i] = {'Pesp': np.real(self._data.get(i)['geracao'] - self._data.get(i)['carga']),
                                 'Qesp': float(
                                     np.imag(self._data.get(i)['geracao']) - np.imag(self._data.get(i)['carga']))
                                 }
            elif self._data[i]['code'] == 3:
                self._Sesp[i] = {'Pesp': np.real(self._data.get(i)['geracao'] - self._data.get(i)['carga']),
                                 'Qesp': float(
                                     np.imag(self._data.get(i)['geracao']) - np.imag(self._data.get(i)['carga']))
                                 }
        if showSesp:
            print('\n\n=============================== Sesp: =================================')
            print(self._Sesp, ' pu')
            print('========================================================================')

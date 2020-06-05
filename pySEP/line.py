import numpy as np


class Line:
    def __init__(self, numBus):
        self.__Lines = dict()
        self._ybus = object()
        self.__numBus = numBus

    def addLine(self, b1, b2, z_ij):
        z_ij = z_ij
        y_ij = 1 / z_ij
        self.__Lines[(b1, b2)] = {'z': z_ij, 'y': y_ij}

    def showLines(self):
        print('\n\n====================================== Ligações: =============================================')
        for i in self.__Lines:
            print('Ligação = \t', i, '\t', self.__Lines[i])
        print('==============================================================================================')

    def ybus(self, showYbus=False):
        self._ybus = np.ones((self.__numBus, self.__numBus), dtype=complex)

        for i in range(len(self._ybus)):
            lin = []
            for j in range(len(self._ybus)):
                if i == j:
                    lin.append(0)
                else:
                    if self.__Lines.__contains__(tuple([i + 1, j + 1])):
                        lin.append(-self.__Lines.get(tuple([i + 1, j + 1]))['y'])
                    elif self.__Lines.__contains__(tuple([j + 1, i + 1])):
                        lin.append(-self.__Lines.get(tuple([j + 1, i + 1]))['y'])
                    else:
                        lin.append(0)
            for j in range(len(self._ybus)):
                if i == j:
                    lin[j] = -1 * sum(lin)
            lin = np.around(lin, decimals=3)
            self._ybus[i] = lin

        self._ybus = np.around(self._ybus,  decimals=5)
        
        if showYbus:
            print('\n\n============================= YBUS: ====================================')
            for i in self._ybus: print(i)
            print('========================================================================')

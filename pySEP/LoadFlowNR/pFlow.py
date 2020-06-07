import numpy as np
import cmath as cmt


class Jacob:
    def __init__(self):
        self.__Jacob = list()
        self.__data = dict()
        self.__ybus = list()
        self.__nPQ = int()
        self.__nPV = int()

    def _setInfo(self, data, ybus, nPQ, nPV):
        self.__data = data
        self.__ybus = ybus
        self.__nPQ = nPQ
        self.__nPV = nPV

    def setJ1(self, listAng, nPQ, nPV):
        self.__J1 = np.ones((nPQ + nPV, nPQ + nPV))

        mainDiagonal = []
        outDiagonal = []
        for i in listAng:
            soma = []
            for j in range(1, len(self.__data) + 1, 1):
                if i != j:
                    soma.append(
                        abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__data.get(i)['tensao']) *
                        abs(self.__data.get(j)['tensao']) *
                        cmt.sin(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__data.get(i)['ang'] +
                                self.__data.get(j)['ang'])
                    )
            mainDiagonal.append(sum(soma))

        for i in listAng:
            for j in listAng:
                if i != j:
                    outDiagonal.append(
                        -abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__data.get(i)['tensao']) *
                        abs(self.__data.get(j)['tensao']) *
                        cmt.sin(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__data.get(i)['ang'] +
                                self.__data.get(j)['ang'])
                    )
        m = 0
        for i in range(len(listAng)):
            # m = 0
            for j in range(len(listAng)):
                if i == j:
                    self.__J1[i][j] = np.real(mainDiagonal[j])
                else:
                    self.__J1[i][j] = np.real(outDiagonal[m])
                    m += 1
        self.__J1 = np.around(self.__J1, decimals=5)
        return self.__J1


nPQ = 10
nPV = 3
#
# a = list()
# b = list()
# c = list()
# d = list()
#
# for i in range(nPQ + nPV):
#     lin = []
#     for j in range(nPQ + nPV):
#         lin.append(10)
#     a.append(lin)
#
# for i in range(nPQ + nPV):
#     lin = []
#     for j in range(nPQ):
#         lin.append(20)
#     b.append(lin)
#
# for i in range(nPQ):
#     lin = []
#     for j in range(nPQ + nPV):
#         lin.append(30)
#     c.append(lin)
#
# for i in range(nPQ):
#     lin = []
#     for j in range(nPQ):
#         lin.append(40)
#     d.append(lin)

a = np.ones([nPQ + nPV, nPQ + nPV])*10
b = np.ones([nPQ + nPV, nPQ])*20
c = np.ones([nPQ, nPQ + nPV])*30
d = np.ones([nPQ, nPQ])*40


print('a=\n', a)
print('b=\n', b)
print('c=\n', c)
print('d=\n', d)

j = np.ones([2 * nPQ + nPV, 2 * nPQ + nPV])

for i in range(2 * nPQ + nPV):
    for k in range(2 * nPQ + nPV):
        if i < len(a):
            if k < len(a):
                j[i][k] = a[i][k]
            else:
                j[i][k] = b[i-len(a)][k-len(a)]
        else:
            if k < len(c[0]):
                j[i][k] = c[i-len(a)][k]
            else:
                j[i][k] = d[i-len(a)][k-len(a)]
print('\n')
print(j)

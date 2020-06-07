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

    def __setJ1(self, listAng, nPQ, nPV):
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
                    # soma.append(
                    #     self.__ybus[i - 1][j - 1] *
                    #     self.__data.get(i)['tensao'] *
                    #     self.__data.get(j)['tensao'] *
                    #     cmt.sin(cmt.phase(self.__ybus[i - 1][j - 1]) -
                    #             self.__data.get(i)['ang'] +
                    #             self.__data.get(j)['ang'])
                    # )
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

    def __setJ2(self, listTensao, listAng, nPQ, nPV):
        self.__J2 = np.ones((nPQ + nPV, nPQ))

        mainDiagonal = []
        outDiagonal = []

        for i in listAng:
            soma = []
            a = 0
            for j in range(1, len(self.__data) + 1, 1):

                if i != j:
                    soma.append(
                        abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__data.get(j)['tensao']) *
                        cmt.cos(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__data.get(i)['ang'] +
                                self.__data.get(j)['ang'])
                    )
            a = (2 * abs(self.__data.get(i)['tensao']) * abs(self.__ybus[i - 1][i - 1]) *
                 cmt.cos(cmt.phase(self.__ybus[i - 1][i - 1]))
                 )
            mainDiagonal.append(a + sum(soma))

        for i in listAng:
            for j in listTensao:
                if i != j:
                    outDiagonal.append(
                        abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__data.get(i)['tensao']) *
                        cmt.cos(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__data.get(i)['ang'] +
                                self.__data.get(j)['ang'])
                    )
        m = 0
        for i in range(nPQ + nPV):
            for j in range(nPQ):
                if i < nPV:
                    self.__J2[i][j] = np.real(outDiagonal[m])
                    m += 1
                elif i >= nPV:
                    if i - nPV == j:
                        self.__J2[i][j] = np.real(mainDiagonal[j + nPV])
                    else:
                        self.__J2[i][j] = np.real(outDiagonal[m])
                        m += 1

        self.__J2 = np.around(self.__J2, decimals=5)
        return self.__J2

    def __setJ3(self, listTensao, listAng, nPQ, nPV):
        self.__J3 = np.ones((nPQ, nPQ + nPV))

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
                        cmt.cos(cmt.phase(self.__ybus[i - 1][j - 1]) -
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
                        cmt.cos(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__data.get(i)['ang'] +
                                self.__data.get(j)['ang'])
                    )
        m = 0

        for i in range(nPQ):
            for j in range(nPQ + nPV):
                if j < nPV:
                    self.__J3[i][j] = np.real(outDiagonal[m])
                    m += 1
                elif j >= nPV:
                    if j - nPV == i:
                        self.__J3[i][j] = np.real(mainDiagonal[i + nPV])
                    else:
                        self.__J3[i][j] = np.real(outDiagonal[m])
                        m += 1
        self.__J3 = np.around(self.__J3, decimals=5)
        return self.__J3

    def __setJ4(self, listTensao, listAng, nPQ, nPV):
        self.__J4 = np.ones((nPQ, nPQ))

        mainDiagonal = []
        outDiagonal = []
        for i in listAng:
            soma = []
            a = 0
            for j in range(1, len(self.__data) + 1, 1):
                if i != j:
                    soma.append(
                        abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__data.get(j)['tensao']) *
                        cmt.sin(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__data.get(i)['ang'] +
                                self.__data.get(j)['ang'])
                    )
            a = (2 * abs(self.__data.get(i)['tensao']) * abs(self.__ybus[i - 1][i - 1]) *
                 cmt.sin(cmt.phase(self.__ybus[i - 1][i - 1]))
                 )
            mainDiagonal.append(-a - sum(soma))
        for i in listAng:
            for j in listTensao:
                if i != j:
                    outDiagonal.append(
                        -abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__data.get(i)['tensao']) *
                        cmt.sin(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__data.get(i)['ang'] +
                                self.__data.get(j)['ang'])
                    )
        m = 0

        for i in range(nPQ):
            for j in range(nPQ):
                if i == j:
                    self.__J4[i][j] = np.real(mainDiagonal[j + nPV])
                else:
                    self.__J4[i][j] = np.real(outDiagonal[m])
                    m += 1

        self.__J4 = np.around(self.__J4, decimals=5)
        return self.__J4

    def _setJacob(self, listTensao, listAng, showSubs=False):

        nXn = (2 * self.__nPQ) + self.__nPV

        j1 = self.__setJ1(listAng=listAng, nPQ=self.__nPQ, nPV=self.__nPV)  # (nPQ  + nPV) X (nPQ + nPV)
        j2 = self.__setJ2(listTensao=listTensao, listAng=listAng, nPQ=self.__nPQ, nPV=self.__nPV)  # (nPQ + nPV) X (nPQ)
        j3 = self.__setJ3(listTensao=listTensao, listAng=listAng, nPQ=self.__nPQ, nPV=self.__nPV)  # (nPQ) X (nPQ + nPV)
        j4 = self.__setJ4(listTensao=listTensao, listAng=listAng, nPQ=self.__nPQ, nPV=self.__nPV)  # (nPQ) X (nPQ)

        self.__Jacob = np.zeros((nXn, nXn))

        # for i in range(nXn):
        #     h = []
        #     k = []
        #     if i < len(j1):
        #         for j in range(len(j1[i])): h.append(j1[i][j])
        #         for j in range(len(j2[i])): h.append(j2[i][j])
        #         self.__Jacob[i] = np.hstack(h)
        #     elif i >= len(j1):
        #         m = i - len(j1)
        #         for j in range(len(j3[m])): k.append(j3[m][j])
        #         for j in range(len(j4[m])): k.append(j4[m][j])
        #         self.__Jacob[i] = np.hstack(k)

        # j = np.ones([2 * nPQ + nPV, 2 * nPQ + nPV])

        for i in range(2 * self.__nPQ + self.__nPV):
            for k in range(2 * self.__nPQ + self.__nPV):
                if i < len(j1):
                    if k < len(j1):
                        self.__Jacob[i][k] = j1[i][k]
                    else:
                        self.__Jacob[i][k] = j2[i - len(j1)][k - len(j1)]
                else:
                    if k < len(j3[0]):
                        self.__Jacob[i][k] = j3[i - len(j1)][k]
                    else:
                        self.__Jacob[i][k] = j4[i - len(j1)][k - len(j1)]
        if showSubs:
            print('\n\n==================== MATRIZ JACOBIANA: ===========================')
            # print("iteração [", self.count, "]")
            print('\nJ1 = ')
            for i in j1: print(i)
            print('\nJ2 = ')
            for i in j2: print(i)
            print('\nJ3 = ')
            for i in j3: print(i)
            print('\nJ4 = ')
            for i in j4: print(i)
            print('\nJACOB = ')
            for i in self.__Jacob: print(i)
            print('========================================================================')

    def getJacob(self):
        return self.__Jacob

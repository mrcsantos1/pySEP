import numpy as np
import math as mt
import cmath as cmt


def jcb_setJacob(dicBarras, yBus, dicNpqv, showSubs=False):
    npq = dicNpqv.get('nPQ')
    npv = dicNpqv.get('nPV')

    list_ang = dicNpqv['listAngTens'].get('ang')

    n_x_n = (2 * npq) + npv

    j1 = __setJ1(dicBarras=dicBarras, yBus=yBus, listAng=list_ang, nPQ=npq,
                 nPV=npv)  # (nPQ  + nPV) X (nPQ + nPV)
    j2 = __setJ2(dicBarras=dicBarras, yBus=yBus, listAng=list_ang, nPQ=npq,
                 nPV=npv)  # (nPQ + nPV) X (nPQ)
    j3 = __setJ3(dicBarras=dicBarras, yBus=yBus, listAng=list_ang, nPQ=npq,
                 nPV=npv)  # (nPQ) X (nPQ + nPV)
    j4 = __setJ4(dicBarras=dicBarras, yBus=yBus, listAng=list_ang, nPQ=npq)  # (nPQ) X (nPQ)

    dic_jacob = np.zeros((n_x_n, n_x_n))

    for i in range(2 * npq + npv):
        for k in range(2 * npq + npv):
            if i < len(j1):
                if k < len(j1):
                    dic_jacob[i][k] = j1[i][k]
                else:
                    dic_jacob[i][k] = j2[i - len(j1)][k - len(j1)]
            else:
                if k < len(j3[0]):
                    dic_jacob[i][k] = j3[i - len(j1)][k]
                else:
                    dic_jacob[i][k] = j4[i - len(j1)][k - len(j1)]

    if showSubs:
        print('\n\n==================== MATRIZ JACOBIANA: ===========================')
        print('\nJ1 = ')
        for i in j1:
            print(i)
        print('\nJ2 = ')
        for i in j2:
            print(i)
        print('\nJ3 = ')
        for i in j3:
            print(i)
        print('\nJ4 = ')
        for i in j4:
            print(i)
        print('\nJACOB = ')
        for i in dic_jacob:
            print(i)
        print('========================================================================')

    return dic_jacob


def __setJ1(dicBarras, yBus, listAng, nPQ, nPV):
    j1 = np.ones((nPQ + nPV, nPQ + nPV))

    main_diag = []
    out_diag = []
    for i in listAng:
        soma = []
        for j in range(1, len(dicBarras) + 1, 1):
            if i != j:
                soma.append(
                    abs(dicBarras[i].get('tensao')) *
                    abs(dicBarras[j].get('tensao')) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.sin(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )
        main_diag.append(sum(soma))
    for i in listAng:
        for j in listAng:
            if i != j:
                out_diag.append(
                    -abs(dicBarras[i].get('tensao')) *
                    abs(dicBarras[j].get('tensao')) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.sin(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )
    m = 0
    for i in range(nPQ + nPV):
        for j in range(nPQ + nPV):
            if i == j:
                j1[i][j] = main_diag[j]
            else:
                j1[i][j] = out_diag[m]
                m += 1
    j1 = np.around(j1, decimals=5)
    return j1


def __setJ2(dicBarras, yBus, listAng, nPQ, nPV):
    j2 = np.ones((nPQ + nPV, nPQ))

    main_diag = []
    out_diag = []
    for i in listAng:
        soma = []
        for j in range(1, len(dicBarras) + 1, 1):
            if i != j:
                soma.append(
                    abs(dicBarras[j].get('tensao')) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.cos(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )
        soma = sum(soma) + (2 * abs(dicBarras[i].get('tensao')) *
                            abs(yBus[i - 1][i - 1]) *
                            mt.cos(cmt.phase(yBus[i - 1][i - 1])))
        main_diag.append(soma)

    for i in listAng:
        for j in listAng:
            if i != j:
                out_diag.append(
                    abs(dicBarras[i].get('tensao')) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.cos(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )
    m = 0
    for i in range(nPQ + nPV):
        for j in range(nPQ):
            if i == j:
                j2[i][j] = main_diag[j]
            else:
                j2[i][j] = out_diag[m]
                m += 1

    j2 = np.around(j2, decimals=5)
    return j2


def __setJ3(dicBarras, yBus, listAng, nPQ, nPV):
    j3 = np.ones((nPQ, nPQ + nPV))

    main_diag = []
    out_diag = []
    for i in listAng:
        soma = []
        for j in range(1, len(dicBarras) + 1, 1):
            if i != j:
                soma.append(
                    abs(dicBarras[i].get('tensao')) *
                    abs(dicBarras[j].get('tensao')) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.cos(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )
        main_diag.append(sum(soma))
    for i in listAng:
        for j in listAng:
            if i != j:
                out_diag.append(
                    -abs(dicBarras[i].get('tensao')) *
                    abs(dicBarras[j].get('tensao')) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.cos(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )
    m = 0
    for i in range(nPQ):
        for j in range(nPQ + nPV):
            if i == j:
                j3[i][j] = main_diag[j]
            else:
                j3[i][j] = out_diag[m]
                m += 1

    j3 = np.around(j3, decimals=5)
    return j3


def __setJ4(dicBarras, yBus, listAng, nPQ):
    j4 = np.ones((nPQ, nPQ))

    main_diag = []
    out_diag = []
    for i in listAng:
        soma = []
        for j in range(1, len(dicBarras) + 1, 1):
            if i != j:
                soma.append(
                    abs(dicBarras[j].get('tensao')) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.sin(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )
        soma = -sum(soma) - (2 * abs(dicBarras[i].get('tensao')) *
                             abs(yBus[i - 1][i - 1]) *
                             mt.sin(cmt.phase(yBus[i - 1][i - 1])))
        main_diag.append(soma)

    for i in listAng:
        for j in listAng:
            if i != j:
                out_diag.append(
                    -abs(dicBarras[i].get('tensao')) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.sin(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )
    m = 0

    for i in range(nPQ):
        for j in range(nPQ):
            if i == j:
                j4[i][j] = main_diag[j]
            else:
                j4[i][j] = out_diag[m]
                m += 1

    j4 = np.around(j4, decimals=5)
    return j4

import numpy as np
import math as mt
import cmath as cmt


def getSbase(dicFlow):
    return dicFlow.get('Sbase')


def pot_injetada(dicBarras, dicFluxo, yBus, count, show=False):
    dicFluxo['deltaPQ'] = []
    dicFluxo['resP'] = []
    dicFluxo['resQ'] = []

    for i in dicBarras:
        soma1 = []
        soma2 = []
        if dicBarras[i]['code'] != 1:
            for j in dicBarras:
                soma1.append(  # Apenas Potência ATIVA
                    abs(dicBarras.get(i)['tensao']) *
                    abs(dicBarras.get(j)['tensao']) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.cos(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )

                soma2.append(  # Apenas Potência REATIVA
                    abs(dicBarras.get(i)['tensao']) *
                    abs(dicBarras.get(j)['tensao']) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.sin(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )
            soma1 = sum(soma1)
            soma2 = -sum(soma2)

            dicFluxo['resP'].append(dicFluxo['Sesp'].get(i)['Pesp'] - soma1)
            if dicBarras[i]['code'] == 2:
                dicFluxo['resQ'].append(dicFluxo['Sesp'].get(i)['Qesp'] - soma2)

    for i in range(len(dicFluxo['resP'])):
        dicFluxo['deltaPQ'].append(dicFluxo['resP'][i])
    for i in range(len(dicFluxo['resQ'])):
        dicFluxo['deltaPQ'].append(dicFluxo['resQ'][i])  # SEM O j

    dicFluxo['deltaPQ'] = np.around(dicFluxo['deltaPQ'], decimals=5)

    if show:
        for i in dicFluxo['deltaPQ']:
            print("delta P e Q da iteração [", count, "] \t=", i)
    print('resP = \t', dicFluxo['resP'], '\tresQ = \t', dicFluxo['resQ'])


def __inv_jacob(jacobiana):
    return np.linalg.inv(jacobiana)


def sist_linear(dicBarras, dicFlow, dic_nPQV, plot, jacob):
    # inv_jac = __inv_jacob(jacob)
    vet_x = np.linalg.solve(jacob, dicFlow.get('deltaPQ'))
    # vet_x = np.dot(inv_jac, dicFlow.get('deltaPQ'))
    # print('\n\nJ-1: \n', inv_jac)
    print('\n\nx = ', vet_x)
    ang = []
    tens = []
    for i in range(len(vet_x)):
        if i < (dic_nPQV.get('nPQ') + dic_nPQV.get('nPV')):
            ang.append(vet_x[i])
        else:
            tens.append(vet_x[i])
    m = 0
    for i in range(len(dicBarras)):
        if dicBarras[i + 1]['code'] != 1:
            dicBarras[i + 1]['ang'] += float(np.real(ang[m]))
            plot['ang'][i + 1].append(dicBarras[i + 1]['ang'])
            m += 1
    m = 0
    for i in range(len(dicBarras)):
        if dicBarras[i + 1]['code'] == 2:
            dicBarras[i + 1]['tensao'] += float(np.real(tens[m]))
            plot['tensao'][i + 1].append(dicBarras[i + 1]['tensao'])
            m += 1


def nova_inj(dicBarras, yBus):
    __sBarras = dict()
    for i in dicBarras:
        soma1 = []
        soma2 = []
        if dicBarras[i]['code'] != 2:
            for j in dicBarras:
                soma1.append(  # Apenas Potência ATIVA
                    abs(dicBarras.get(i)['tensao']) *
                    abs(dicBarras.get(j)['tensao']) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.cos(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )
                soma2.append(  # Apenas Potência REATIVA
                    abs(dicBarras.get(i)['tensao']) *
                    abs(dicBarras.get(j)['tensao']) *
                    abs(yBus[i - 1][j - 1]) *
                    mt.sin(
                        cmt.phase(yBus[i - 1][j - 1]) -
                        dicBarras.get(i)['ang'] +
                        dicBarras.get(j)['ang']
                    )
                )
            soma1 = sum(soma1)
            soma2 = -sum(soma2)

            if dicBarras[i]['code'] == 1:
                __sBarras[i] = {'P': soma1, 'Q': soma2}
            elif dicBarras[i]['code'] == 3:
                __sBarras[i] = {'P': 0, 'Q': soma2}

    for i in dicBarras:
        if dicBarras[i]['code'] == 1:
            dicBarras[i]['geracao'] = __sBarras[i].get('P') + __sBarras[i].get('Q') * 1j
        elif dicBarras[i]['code'] == 3:
            dicBarras[i]['geracao'] = np.real(dicBarras[i].get('geracao')) + __sBarras[i].get('Q') * 1j

    print('\n\nsBarras = ', __sBarras)

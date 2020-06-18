import numpy as np

import math as mt
import cmath as cmt
import pySEP.fluxo as fl


def bs_addBarra(dicBarras, dicFlow, barra, code, tensao, ang, carga, geracao):
    dicBarras[barra] = {'code': code, 'tensao': tensao, 'ang': mt.radians(ang),
                        'carga': (carga / fl.getSbase(dicFlow=dicFlow)),
                        'geracao': (geracao / fl.getSbase(dicFlow=dicFlow))}


def bs_add_nPQV(dicBarras, dicNPQV):
    dicNPQV['nPQ'] = 0
    dicNPQV['nPV'] = 0
    dicNPQV['listAngTens']['ang'] = []
    dicNPQV['listAngTens']['tensao'] = []

    for i in dicBarras:
        if dicBarras[i]['code'] == 2:
            dicNPQV['nPQ'] += 1
            dicNPQV['listAngTens']['ang'].append(i)
            dicNPQV['listAngTens']['tensao'].append(i)
        elif dicBarras[i]['code'] == 3:
            dicNPQV['nPV'] += 1
            dicNPQV['listAngTens']['ang'].append(i)


def bs_add_plot(dicBarras, dicPlot):
    for i in dicBarras:
        dicPlot['tensao'][i] = [dicBarras[i].get('tensao')]
        dicPlot['ang'][i] = [dicBarras[i].get('ang')]


def bs_relatorioBarras(dicBarras, dicFlow):
    bs_setSesp(dicBarras=dicBarras, dicFlow=dicFlow)
    print('\n\n=============================== DADOS: =================================')
    print('Sbase = ', dicFlow.get('Sbase'), ' VA')
    for i in dicBarras:
        dicBarras[i]['ang'] = mt.degrees(dicBarras.get(i)['ang'])
        print(dicBarras[i])
    print('========================================================================')


def bs_showBuses(dicBarras, dicFlow):
    print('\n\n=============================== DADOS: =================================')
    print('Sbase = ', dicFlow.get('Sbase'), ' VA')
    for i in dicBarras:
        print('Barra: ', i, '\t', end='')
        print(dicBarras[i])
    print('========================================================================')


def bs_setSesp(dicBarras, dicFlow):
    for i in dicBarras:
        if dicBarras[i]['code'] != 1:
            dicFlow['Sesp'][i] = {'Pesp': np.real(dicBarras[i].get('geracao')) - np.real(dicBarras[i].get('carga')),
                                  'Qesp': np.imag(dicBarras[i].get('geracao')) - np.imag(dicBarras[i].get('carga'))
                                  }
    print('\n\n=============================== Sesp: =================================')
    print(dicFlow['Sesp'], ' pu')
    print('========================================================================')


def bs__showTensao(dicTensoes):
    print('============================ TENSÕES: =======================================')
    for i in dicTensoes:
        print('Barra: \t', i, '\tTENSÃO = \t', dicTensoes.get(i), '\t[pu]')
    print('===============================================================================')


def bs_tensoes(dicBarras, show):
    v = dict()
    for i in dicBarras:
        v[i] = cmt.rect(dicBarras.get(i)['tensao'], dicBarras.get(i)['ang'])
    if show:
        print("")
        bs__showTensao(v)
    return v

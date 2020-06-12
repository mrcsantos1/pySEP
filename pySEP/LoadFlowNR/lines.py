import numpy as np


def addLine(dic, b1, b2, z_ij):
    z_ij = z_ij
    y_ij = 1 / z_ij
    dic[(b1, b2)] = {'z': z_ij, 'y': y_ij}


def showLines(dic):
    print('\n\n====================================== Ligações: =============================================')
    for i in dic:
        print('Ligação = \t', i, '\t', dic[i])
    print('==============================================================================================')


def ybus(dic, showYbus=False):
    _ybus = np.ones((len(dic.get('data')), len(dic.get('data'))), dtype=complex)

    for i in range(len(_ybus)):
        lin = []
        for j in range(len(_ybus)):
            if i == j:
                lin.append(0)
            else:
                if dic['lines'].__contains__(tuple([i + 1, j + 1])):
                    lin.append(-dic['lines'].get(tuple([i + 1, j + 1]))['y'])
                elif dic['lines'].__contains__(tuple([j + 1, i + 1])):
                    lin.append(-dic['lines'].get(tuple([j + 1, i + 1]))['y'])
                else:
                    lin.append(0)
        for j in range(len(_ybus)):
            if i == j:
                lin[j] = -1 * sum(lin)
        lin = np.around(lin, decimals=3)
        _ybus[i] = lin

    _ybus = np.around(_ybus, decimals=5)

    if showYbus:
        print('\n\n============================= YBUS: ====================================')
        for i in _ybus:
            print(i)
        print('========================================================================')

    return _ybus

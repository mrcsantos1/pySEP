import matplotlib.pyplot as plt


def __plotTensao(contador, dic_barras, dic_tensoes_plot):
    # x = contador - 1
    x = contador
    barras = []
    y = []
    for i in dic_barras:
        if dic_barras.get(i)['code'] == 2:
            barras.append(i)
    for i in barras:
        y.append(dic_tensoes_plot.get(i))
    for i in range(len(barras)):
        plt.subplot(len(barras), 1, i + 1)
        plt.plot(range(x + 1), y[i], linewidth=3, color="r")
        plt.title('Variação da tensão na barra ' + str(barras[i]) + ' X Número de iterações')
        plt.xlabel('Número de iterações ')
        plt.ylabel('Tensão na barra ' + str(barras[i]) + ' pu')
        # plt.grid(True)
    plt.tight_layout()
    plt.show()


def __plotAng(contador, dic_barras, dic_ang_plot):
    # x = contador - 1
    x = contador
    barras = []
    y = []
    for i in dic_barras:
        if dic_barras.get(i)['code'] != 1:
            barras.append(i)
    for i in barras:
        y.append(dic_ang_plot.get(i))
    for i in range(len(barras)):
        plt.subplot(len(barras), 1, i + 1)
        plt.plot(range(x + 1), y[i], linewidth=3, color="r")
        plt.title('Variação do ângulo na barra ' + str(barras[i]) + ' X Número de iterações')
        plt.xlabel('Número de iterações ')
        plt.ylabel('Ângulo na barra ' + str(barras[i]) + ' [rad]')
        # plt.grid(True)
    plt.tight_layout()
    plt.show()


def plotData(cont, dic_barras, dic_tens_plot, dic_ang_plot, tensao, ang):
    if tensao:
        __plotTensao(contador=cont, dic_barras=dic_barras, dic_tensoes_plot=dic_tens_plot)
    if ang:
        __plotAng(contador=cont, dic_barras=dic_barras, dic_ang_plot=dic_ang_plot)

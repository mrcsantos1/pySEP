import numpy as np
import matplotlib.pyplot as plt
import math as mt
import cmath as cmt

from line import Line
from bus import Bus
from jacob import Jacob


class Circuit(Line, Bus, Jacob):
    def __init__(self, nBus):
        self.__numBus = nBus
        Bus.__init__(self)
        Line.__init__(self, self.__numBus)
        Jacob.__init__(self)

        self.__deltaPeQ = list()
        self.__ResiduoP = list()
        self.__ResiduoQ = list()
        self.__x = list()
        self.__Sbarras = dict()
        self.__V = dict()
        self.__I = dict()
        self.__powerFlow = dict()

        self._count = 1
        self.__perdas = 0

    @staticmethod
    def help():
        print(
            """
            Este método é utilizado para obter informações sobre o funcionamento deste código. Ou seja, antes de usar algum
            método, recomenda-se executar este método para ter certeza do que está sendo feito.

            A execução correta deste cálculo requer que alguns passos lógicos sejam seguidos. A seguir estes passos são
            comentados:

                ## 1:
                *Após instanciar um objeto com esta classe, o primeiro passo para montar o circuito é acrescentar uma barra.
                Para isso, utiliza-se o método "addBus(args)", com seus respectivos parâmetros. Este método é utilizado para
                se adicionar todas as barras do circuito, uma de cada vez.

                ## 2:
                *Após adicionar a/as barras, caso queira visualizar suas respectivas informações, basta utilizar o método
                "showBuses()", sem parâmetros sendo passados.

                ## 3:
                *Após adicionar as barras, deve-se executar o método "setSesp()", sem parâmetros, o qual é responsável por
                calcular as potências especificadas em cada barra uma das anteriormente adicionadas ao circuito.

                ## 4:
                *Após adicionar todas as barras (ou ao menos as barras que estão ligadas entre si), e executar o cálculo da
                potência especificada em cada barra,  adiciona-se as ligações entre essas barras com o método
                "addLine(args)", sendo passados seus respectivos parâmetros.

                ## 5:
                *Após adicionar as linhas, caso queira visualizar suas respectivas ligações, basta utilizar o método
                "showLines()", sem parâmetros sendo passados. Após adicionar as linhas, já é possível executar o método
                "solveCircuito(args)" -passo 11- , para calcular, de forma iterativa, o fluxo de potência pelo método de
                newton-raphson. Caso queira executar mais passos, então pode-se seguir para o passo 6, senão, vá direto para
                o passo 11.

                ## 6:
                *Após adicionar as linhas, é possível calcular a matriz de admitâncias Ybus através do método "ybus()", sem
                parâmetros. Porém, recomenda-se que este passo só seja executado em caso de testes. Para abreviar o número
                de métodos e resolver o circuito, recomenda-se que este passo 6 seja pulado para o passo 10. Se caso queira
                executar o passo 6, então deve-se seguir a sequências dos passos 6, 7, 8, 9 e 10, obrigatoriamente.

                ## 7:
                *Após o passo 6 (ybus()), deve-se executar o passo 7 responsável por calcular a potência injetada no sistema
                através do método "Sinjetada(args)", com seu respectivo parâmetro.

                ## 8:
                *Após o passo 7 (Sinjetada()), deve-se executar o passo 8 responsável por calcular a matriz Jacobiana,
                através do método "setJacob(args), com seus parâmetros".

                ## 9:
                *Após o passo 8 (setJacob()), deve-se executar o passo 9 responsável por resolver a equação matricial
                [delta P delta Q] = [Jacobiana] . [Resultado], através do método "linearSystem()", sem parâmetros.

                ## 10:
                *Após o passo 9 (linearSystem()), deve-se executar o passo 10 responsável por encontrar a nova injeção de
                potência no sistema, através do método "NovaInjecao()", sem parâmetros.

                ## 11:
                *Após adicionar as linhas no passo 5, já é possível executar o método "solveCircuito(args)", com seus
                parâmetros, para calcular de forma iterativa, o fluxo de potência pelo método de newton-raphson.

                ## 12:
                *Após o circuito resolvido, seja pelo passo 11 ou pela sequência dos passos 6, 7, 8, 9 e 10, deve-se
                calcular as tensões em cada barra através do método "Tensoes(args)", com seu respectivo parâmetro.

                ## 13:
                *Após o passo 12 (Tensoes()), deve-se calcular as correntes nas linhas do circuito. Para isso, utiliza-se o
                método "Correntes(args)", com seu respectivo parâmetro.

                ## 14:
                *Após o passo 13 (Correntes()), deve-se executar o método "powerFlow(args)", com seus parâmetros, para
                calcular o fluxo de potência em todas as ligações do sistema.

                ## 15:
                *Após o passo 14 (powerFlow()), pode-se obter o valor das perdas no sistema através do método "losses()",
                sem parâmetros.

                ## 16:
                *Por fim, após todos os passos acima e com os valores do fluxo de potência no sistema, é possível plotar
                o comportamento das curvas de convergência das tensões e dos ângulos em cada barra, através do método
                "plotData(args)", com seus parâmetros.


            :param addBus: Este método é utilizado apenas para setar (adicionar/atualizar) os valores iniciais de cada barra do
            sistema. Parâmetros deste método:
                :param barra: Representa o número de cada barra.
                :param code: Representa o tipo de cada barra (1 : Tensão e Ângulo; 2 : P e Q; 3 : P e V).
                :param tensao: Módulo da tensão na barra.
                :param ang: Valor do ângulo de fase cada barra. Colocá-lo em GRAUS.
                :param carga: P e Q de carga em cada barra.
                :param geracao: P e Q de geração em cada barra.

            :param showBuses: Método utilizado para printar todos os valores em cada barra. Sem parâmetros.

            :param setSesp: Método utilizado para calcular a potência especificada em cada barra. Os valores
            são printados automaticamente. Sem parâmetros.

            :param addLine: Método utilizado para setar as ligações entre cada barra. Seus parâmetros:
                :param barra1: Barra de origem.
                :param barra2: Barra destino.
                :param impedancia: Valor em PU da impedância.
                :param admitancia: Valor em PU da admitância.

                É necessário informar um valor de admitância ou de impedância.

            :param showLines: Método utilizado para printar as ligações do circuito. Sem parâmetros.

            :param ybus: Método utilizado para calcular a matriz ybus. Sem parâmetros.

            :param Sinjetada: Método utilizado para calcular as potências injetadas no circuito. E seta os valores de delta
            P e de delta Q. Sem parâmetros.

            :param setJacob: Método utilizado para calcular a matriz Jacobiana. Seus parâmetros:
                :param listTensao: Lista de tensões a serem calculadas no circuito. (Barras PQ)
                :param listAng: Lista de ângulos a serem calculados no circuito. (Barras PQ e PV)
                :param mostrarSubs: Deseja mostrar os valores das submatrizes J1, J2, J3 e J4 durante
                as iterações? Se sim, passar True como parâmetro.

                Printa a matriz Jacobiana.

            :param linearSystem: Método utilizado para calcular os resultados do sistema linear do passo 6 da aula 13. O
            sistema é do tipo: [delta P delta Q] = [Jacobiana] . [Resultado] - Sem parâmetros.

            :param NovaInjecao: Método utilizado para calcular o novo valor de Injeção de potência aparente nas barras de
            folga e PV. (P e Q nas de folga e Q nas PV). Sem parâmetros.

            :param solveCircuito: Método genérico utilizado para 'resolver' o circuito. Seus parâmetros:
                :param showSubMat: Parâmetro utilizado caso dejese-se mostrar os valores das variações
                de potências ativa e reativa, bem como as variações nas submatrizes em cada iteração.
                :param erro: Valor do erro utilizado para parar as iterações.
                :param iteracoes: Número de iterações que se deseja repetir o cálculo.
                    Obs.: Deve-se passar ou um número de iterações ou um número para o erro.
                :param listTensao: Lista de tensões a serem calculadas no circuito. (Barras PQ)
                :param listAng: Lista de ângulos a serem calculados no circuito. (Barras PQ e PV)

            :param Tensoes: Método utilizado para calcular as tensões em cada barra. O cálculo é feito a partir dos valores
            em pu e dos ângulos das tensões, os quais são oriundos das iterações do método "solveCircuito()". Seu parâmetro:
                :param show: Caso dejese-se mostrar os valores das tensões em cada barra, deve-se passar True para o
                parâmetro "show".

            :param Correntes: Método utilizado para calcular os valores das correntes em cada linha. O cálculo é feito para
            todas as barras. Portanto, nas barras que não há ligação, o resultado deve ser 0. As correntes que representam
            ligações com as mesmas barras, seus valores são calculados como o somatório de todas as correntes da barra sob
            análise. Seu parâmetro:

                :param show: Caso dejese-se mostrar os valores das correntes, deve-se passar
                True para o parâmetro "show".

            :param powerFlow: Método responsável por calcular o fluxo de potência em todas as ligações do sistema. Seus
            parâmetros:

                :param printTensao: Caso dejese-se mostrar os valores das tensões em cada barra, deve-se passar True para o
                parâmetro "print".
                :param printCorrentes: Caso dejese-se mostrar os valores das correntes, deve-se passar True para o parâmetro
                "print".

            :param losses: Método utilizado para calcular as perdas do circuito. O cálculo é realizado pela soma de todas
            as potências. Sem parâmetros.

            :param plotData: Método utilizado para plotar a convergência das tensões e dos ângulos calculados pelo
            algoritmo. Seus parâmetros:

                :param tensao: Para plotar a tensão, deve-se passar "True" para este parâmetro.
                :param ang: Para plotar o ângulo, deve-se passar "True" para este parâmetro.


            Segue-se um exemplo prático:

                import pySEP as psp

                c = psp.CreateCircuit(100e6)

                c.addBus(1, 1, 1.05, 0, 0 + 0 * 1j, 0 + 0 * 1j)
                c.addBus(2, 2, 1.00, 0, 256.6e6 + 110.2e6 * 1j, 0 + 0 * 1j)
                c.addBus(3, 2, 1.00, 0, 138.6e6 + 45.2e6 * 1j, 0 + 0 * 1j)

                c.setSesp()

                c.addLine(1, 2, impedancia=0.02 + 0.04j)
                c.addLine(1, 3, impedancia=0.01 + 0.03j)
                c.addLine(2, 3, impedancia=0.0125 + 0.025j)

                c.solveCircuito(iteracoes=20, listTensao=[2, 3], listAng=[2, 3], erro=None, showSubMat=False)

                c.powerFlow(printTensao=True, printCorrentes=True)

                c.losses()

                c.plotData(tensao=True, ang=True)

            Qualquer dúvida, entrar em contato. Endereços disponíveis em README.md
            """
        )

    def _potInj(self, show=False):
        self.__deltaPeQ = []
        self.__ResiduoP = []
        self.__ResiduoQ = []

        for i in self._data:
            soma1 = []
            soma2 = []
            if self._data[i]['code'] != 1:
                for j in self._data:
                    soma1.append(  # Apenas Potência ATIVA
                        abs(self._ybus[i - 1][j - 1]) *
                        abs(self._data.get(i)['tensao']) *
                        abs(self._data.get(j)['tensao']) *
                        mt.cos(np.angle(self._ybus[i - 1][j - 1]) - self._data.get(i)['ang'] + self._data.get(j)[
                            'ang'])
                    )
                    soma2.append(  # Apenas Potência REATIVA
                        -abs(self._ybus[i - 1][j - 1]) *
                        abs(self._data.get(i)['tensao']) *
                        abs(self._data.get(j)['tensao']) *
                        mt.sin(np.angle(self._ybus[i - 1][j - 1]) - self._data.get(i)['ang'] + self._data.get(j)[
                            'ang']) * 1j
                    )
                self.__ResiduoP.append(np.real(
                    self._Sesp.get(i)['Pesp'] - sum(soma1)))  # Lista com os valores de cada barra != da barra |V| phi
                if self._data[i]['code'] == 2:
                    self.__ResiduoQ.append(np.imag((self._Sesp.get(i)['Qesp']) * 1j - sum(soma2)))

        for i in range(len(self.__ResiduoP)):
            self.__deltaPeQ.append(self.__ResiduoP[i])
        for i in range(len(self.__ResiduoQ)):
            self.__deltaPeQ.append(self.__ResiduoQ[i])  # SEM O j

        self.__deltaPeQ = np.around(self.__deltaPeQ, decimals=5)

        if show:
            for i in self.__deltaPeQ:
                print("delta P e Q da iteração [", self._count, "] \t=", i)

    def _setJb(self, listTensao, listAng, showSubs=False):
        self._setInfo(data=self._data, ybus=self._ybus, nPQ=self._nPQ, nPV=self._nPV)
        self._setJacob(listTensao=listTensao, listAng=listAng, showSubs=showSubs)

    def _linearSystem(self):
        self.__x = []
        self.__x = np.linalg.solve(self.getJacob(), self.__deltaPeQ)

        ang = []
        tens = []
        for i in range(len(self.__x)):
            if i < (self._nPQ + self._nPV):
                ang.append(self.__x[i])
            else:
                tens.append(self.__x[i])
        m = 0
        for i in range(len(self._data)):
            if self._data.get(i + 1)['code'] != 1:
                self._data[i + 1]['ang'] += float(np.real(ang[m]))
                self._angPlot[i + 1].append(self._data[i + 1]['ang'])
                m += 1
        m = 0
        for i in range(len(self._data)):
            if self._data.get(i + 1)['code'] == 2:
                self._data[i + 1]['tensao'] += float(np.real(tens[m]))
                self._tensaoPlot[i + 1].append(self._data[i + 1]['tensao'])
                m += 1

    def _newInj(self):
        self.__Sbarras = dict()
        for i in self._data:
            soma1 = []
            soma2 = []
            if self._data[i]['code'] != 2:
                for j in self._data:
                    soma1.append(  # Apenas Potência ATIVA
                        abs(self._ybus[i - 1][j - 1]) *
                        abs(self._data.get(i)['tensao']) *
                        abs(self._data.get(j)['tensao']) *
                        mt.cos(np.angle(self._ybus[i - 1][j - 1]) - self._data.get(i)['ang'] + self._data.get(j)[
                            'ang'])
                    )
                    soma2.append(  # Apenas Potência REATIVA
                        -abs(self._ybus[i - 1][j - 1]) *
                        abs(self._data.get(i)['tensao']) *
                        abs(self._data.get(j)['tensao']) *
                        mt.sin(np.angle(self._ybus[i - 1][j - 1]) - self._data.get(i)['ang'] + self._data.get(j)[
                            'ang']) * 1j
                    )
            if self._data[i]['code'] == 1:
                self.__Sbarras[i] = {'P': np.real(sum(soma1)), 'Q': np.imag(sum(soma2))}
            elif self._data[i]['code'] == 3:
                self.__Sbarras[i] = {'P': 0, 'Q': np.imag(sum(soma2))}

        for i in self._data:
            if self._data[i]['code'] == 1:
                self._data[i]['geracao'] = self.__Sbarras.get(i)['P'] + self.__Sbarras.get(i)['Q'] * 1j
            elif self._data[i]['code'] == 3:
                self._data[i]['geracao'] = np.real(self._data.get(i)['geracao']) + self.__Sbarras.get(i)['Q'] * 1j

    def solve(self, erro, listTensao, listAng, showPotInj=False, showSubs=False):

        self._potInj(show=showPotInj)
        self._setJb(listTensao=listTensao, listAng=listAng, showSubs=showSubs)
        self._count += 1
        self._linearSystem()

        pq = list(map(abs, self.__deltaPeQ))
        test = list(map(lambda m: True if (m < erro) else False, pq))
        stop = test.count(False)
        if stop > 0:
            while True:
                self._potInj(show=showPotInj)
                self._setJb(listTensao=listTensao, listAng=listAng, showSubs=showSubs)
                self._linearSystem()
                self._count += 1
                pq = list(map(abs, self.__deltaPeQ))
                test = list(map(lambda m: True if (m < erro) else False, pq))
                stop = test.count(False)
                if stop == 0:
                    break

        self._newInj()

        print('CONVERGIU PARA UM ERRO DE ', erro, ' .')
        print('CONVERGIU EM ', self._count, ' ITERAÇÕES. ')

    def __showTensao(self):
        print('============================ TENSÕES: =======================================')
        for i in self.__V:
            print('Barra: \t', i, '\tTENSÃO = \t', self.__V.get(i), '\t[pu]')
        print('===============================================================================')

    def _tensoes(self, show=None):
        for i in self._data:
            self.__V[i] = cmt.rect(self._data.get(i)['tensao'],
                                   self._data.get(i)['ang'])
        if show:
            print("")
            self.__showTensao()

    def __showCorr(self):
        print('============================ CORRENTES: =======================================')
        for i in self.__I:
            print('Ligação: \t', i, '\tCorrente = \t', self.__I.get(i), '\t[pu]')
        print('===============================================================================')

    def _correntes(self, show=None):  # Correntes calculadas considerando os ângulos das tensões.
        self._tensoes(show=None)
        for i in self._data:
            soma = []
            for j in self._data:
                if i == j:
                    continue
                else:
                    self.__I[(i, j)] = ((self.__V.get(i) - self.__V.get(j)) * self._ybus[i - 1][j - 1])
                soma.append(((self.__V.get(i) - self.__V.get(j)) * self._ybus[i - 1][j - 1]))
            self.__I[(i, i)] = sum(soma)
        if show:
            self.__showCorr()

    def pFlow(self, showTensoes=False, showCorrentes=False, showPflow=False):
        self._tensoes(show=showTensoes)
        self._correntes(show=showCorrentes)
        for i in self.__I:
            a = i[0]
            self.__powerFlow[i] = -self.__V.get(a) * np.conjugate(self.__I.get(i))
        if showPflow:
            print('======================== Fluxo de Potência: ===================================')
            for i in self.__powerFlow:
                print('Ligação: \t', i, '\tFluxo = \t', self.__powerFlow.get(i), '\t[pu]')
            print('===============================================================================')
            for i in self._data:
                if self._data.get(i)['code'] != 2:
                    self._data[i]['geracao'] = self.__powerFlow.get((i, i))

    def losses(self):
        perdas = []
        for i in self.__powerFlow:
            perdas.append(self.__powerFlow.get(i))
        self.__perdas = sum(perdas)
        print('\n\nPerdas = \t', self.__perdas, '\t[pu]')

    def __plotTensao(self):
        x = self._count - 1
        barras = []
        y = []
        # plt.rcParams.update({'font.size': 20})
        for i in self._data:
            if self._data.get(i)['code'] == 2:
                barras.append(i)
        for i in barras:
            y.append(self._tensaoPlot.get(i))
        for i in range(len(barras)):
            plt.subplot(len(barras), 1, i + 1)
            plt.plot(range(x + 1), y[i], linewidth=3, color="r")
            plt.title('Variação da tensão na barra ' + str(barras[i]) + ' X Número de iterações')
            plt.xlabel('Número de iterações ')
            plt.ylabel('Tensão na barra ' + str(barras[i]) + ' pu')
            # plt.grid(True)
        plt.tight_layout()
        plt.show()

    def __plotAng(self):
        x = self._count - 1
        barras = []
        y = []
        for i in self._data:
            if self._data.get(i)['code'] != 1:
                barras.append(i)
        for i in barras:
            y.append(self._angPlot.get(i))
        for i in range(len(barras)):
            plt.subplot(len(barras), 1, i + 1)
            plt.plot(range(x + 1), y[i], linewidth=3, color="r")
            plt.title('Variação do ângulo na barra ' + str(barras[i]) + ' X Número de iterações')
            plt.xlabel('Número de iterações ')
            plt.ylabel('Ângulo na barra ' + str(barras[i]) + ' [rad]')
            # plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plotData(self, tensao=None, ang=None):
        if tensao:
            self.__plotTensao()
        if ang:
            self.__plotAng()

#
# _2bus = Circuit(nBus=10)
# _2bus.addBus(barra=1, code=1, tensao=1.00, ang=0.00, geracao=0 + 0 * 1j, carga=0 + 0 * 1j)
# _2bus.addBus(barra=2, code=2, tensao=1.00, ang=0.00, geracao=0 + 0 * 1j, carga=10e6 + 2e6 * 1j)
# _2bus.addBus(barra=3, code=2, tensao=1.00, ang=0.00, geracao=0 + 0 * 1j, carga=10e6 + 2e6 * 1j)
# _2bus.addBus(barra=4, code=2, tensao=1.00, ang=0.00, geracao=0 + 0 * 1j, carga=10e6 + 2e6 * 1j)
# _2bus.addBus(barra=5, code=2, tensao=1.00, ang=0.00, geracao=0 + 0 * 1j, carga=10e6 + 2e6 * 1j)
# _2bus.addBus(barra=6, code=2, tensao=1.00, ang=0.00, geracao=0 + 0 * 1j, carga=10e6 + 2e6 * 1j)
# _2bus.addBus(barra=7, code=2, tensao=1.00, ang=0.00, geracao=0 + 0 * 1j, carga=10e6 + 2e6 * 1j)
# _2bus.addBus(barra=8, code=2, tensao=1.00, ang=0.00, geracao=0 + 0 * 1j, carga=10e6 + 2e6 * 1j)
# _2bus.addBus(barra=9, code=2, tensao=1.00, ang=0.00, geracao=0 + 0 * 1j, carga=10e6 + 2e6 * 1j)
# _2bus.addBus(barra=10, code=2, tensao=1.00, ang=0.00, geracao=0 + 0 * 1j, carga=10e6 + 2e6 * 1j)
#
# _2bus.showBuses()
#
# _2bus.setSesp(showSesp=True)
#
# _2bus.addLine(1, 2, z_ij=0.5j)
# _2bus.addLine(1, 3, z_ij=0.5j)
# _2bus.addLine(1, 4, z_ij=0.5j)
# _2bus.addLine(1, 5, z_ij=0.5j)
# _2bus.addLine(2, 6, z_ij=0.5j)
# _2bus.addLine(3, 7, z_ij=0.5j)
# _2bus.addLine(4, 8, z_ij=0.5j)
# _2bus.addLine(5, 9, z_ij=0.5j)
# _2bus.addLine(6, 10, z_ij=0.5j)
#
# _2bus.showLines()
#
# _2bus.ybus(showYbus=True)
#
# _2bus.solve(erro=1e-9, listTensao=[2, 3, 4, 5, 6, 7, 8, 9, 10], listAng=[2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# _2bus.pFlow(showCorrentes=False, showTensoes=False, showPflow=False)
#
# _2bus.losses()
#
# _2bus.plotData(tensao=False, ang=False)

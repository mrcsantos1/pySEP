import cmath as cmt
import math as mt
import matplotlib.pyplot as plt
import numpy as np


class CreateCircuit:
    def __init__(self, PotBase=None):
        """
        :param PotBase: Pode passar um valor para a potência aparente base do circuito.
        Se for passada, deve estar em VA, isto é, para uma potência de 100 MVA, deve-se
        passar o número 100e6.

        Obs.1: Este é o módulo da potência aparente. Portanto é um número real.
        Obs.2: Caso nenhum número for passado como parâmetro, o algoritmo realizará
        os cálculos utilizando a comum, e geralmente usada, base de 100 MVA.
        """
        if PotBase is float and PotBase != 0:
            self.Sbase = PotBase
        else:
            self.Sbase = 100e6
        self.__dados = dict()
        self.__Sesp = dict()
        self.__Ligacoes = dict()
        self.__ybus = []
        self.__J1 = []
        self.__J2 = []
        self.__J3 = []
        self.__J4 = []
        self.__Jacob = []
        self.__listTensao = []
        self.__listAng = []
        self.__powerFlow = dict()
        self.count = 1
        self.__tensaoPlot = dict()
        self.__angPlot = dict()
        self.__x = []
        self.__I = dict()
        self.__V = dict()
        self.__S = dict()
        self.__nPQ = int()
        self.__nPV = int()
        self.__Sbarras = dict()
        self.__ResiduoP = []
        self.__ResiduoQ = []
        self.__deltaPeQ = []
        self.__Perdas = 0

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

    def addBus(self, barra, code, tensao, ang, carga, geracao):
        """
        Este método é utilizado apenas para setar (adicionar/atualizar) os valores iniciais de cada barra do
        sistema.
        :param barra: Representa o número de cada barra.
        :param code: Representa o tipo de cada barra (1 : Tensão e Ângulo; 2 : P e Q; 3 : P e V).
        :param tensao: Módulo da tensão na barra.
        :param ang: Valor do ângulo de fase cada barra. Colocá-lo em GRAUS.
        :param carga: P e Q de carga em cada barra.
        :param geracao: P e Q de geração em cada barra.

        :return: Este método não retorna nada. Apenas modifica/seta os valores para o algoritmo.
        """
        self.__dados[barra] = {'code': code, 'tensao': tensao, 'ang': mt.radians(ang),
                               'carga': (carga / self.Sbase), 'geracao': (geracao / self.Sbase)}
        self.__tensaoPlot[barra] = [tensao]
        self.__angPlot[barra] = [ang]

    def showBuses(self):
        """
        Método utilizado para printar todos os valores em cada barra.
        """
        print('\n\n=============================== DADOS: =================================')
        print('Sbase = ', self.Sbase, ' VA')
        for i in self.__dados:
            print(self.__dados[i])
        print('========================================================================')

    def relatorioBarras(self):
        """
            Método utilizado para printar todos os valores em cada barra.
        """
        print('\n\n=============================== DADOS: =================================')
        print('Sbase = ', self.Sbase, ' VA')
        for i in self.__dados:
            self.__dados[i]['ang'] = mt.degrees(self.__dados.get(i)['ang'])
            print(self.__dados[i])
        print('========================================================================')


    def setSesp(self):
        """
        Método utilizado para calcular a potência especificada em cada barra. Os valores
        são printados automaticamente.
        """
        for i in self.__dados:
            if self.__dados[i]['code'] == 2:
                self.__Sesp[i] = {'Pesp': np.real(self.__dados.get(i)['geracao'] - self.__dados.get(i)['carga']),
                                  'Qesp': float(
                                      np.imag(self.__dados.get(i)['geracao']) - np.imag(self.__dados.get(i)['carga']))
                                  }
            elif self.__dados[i]['code'] == 3:
                self.__Sesp[i] = {'Pesp': np.real(self.__dados.get(i)['geracao'] - self.__dados.get(i)['carga']),
                                  'Qesp': float(
                                      np.imag(self.__dados.get(i)['geracao']) - np.imag(self.__dados.get(i)['carga']))
                                  }
        print('\n\n=============================== Sesp: =================================')
        print(self.__Sesp, ' pu')
        print('========================================================================')

    def addLine(self, barra1, barra2, impedancia=None, admitancia=None):
        """
        Método utilizado para setar as ligações entre cada barra.

        :param barra1: Barra de origem.
        :param barra2: Barra destino.
        :param impedancia: Valor em PU da impedância.
        :param admitancia: Valor em PU da admitância.

        É necessário informar um valor de admitância ou de impedância.
        """
        if impedancia is None:
            impedancia = 1 / admitancia
        elif admitancia is None:
            admitancia = 1 / impedancia
        else:
            return 'ERRO! É NECESSÁRIO INFORMAR O VALOR DE IMPEDÂNCIA OU DE ADMITÂNCIA DA LINHA! '

        self.__Ligacoes[(barra1, barra2)] = {'Impedância': impedancia,
                                             'Admitância': admitancia}

    def showLines(self):
        """
        Método utilizado para printar as ligações do circuito.
        """
        print('\n\n====================================== Ligações: =============================================')
        for i in self.__Ligacoes:
            print('Ligação = \t', i, '\t', self.__Ligacoes[i])
        print('==============================================================================================')

    def __printYbus(self):
        """
        Método privado utilizado apenas para printar os valores da matriz ybus.
        """
        print('\n\n============================= YBUS: ====================================')
        for i in self.__ybus: print(i)
        print('========================================================================')

    def ybus(self):
        """
        Método utilizado para calcular a matriz ybus.
        """
        self.__ybus = np.ones((len(self.__dados), len(self.__dados)), dtype=complex)

        for i in range(len(self.__ybus)):
            lin = []
            for j in range(len(self.__ybus)):
                if i == j:
                    lin.append(0)
                else:
                    if self.__Ligacoes.__contains__(tuple([i + 1, j + 1])):
                        lin.append(-self.__Ligacoes.get(tuple([i + 1, j + 1]))['Admitância'])
                    elif self.__Ligacoes.__contains__(tuple([j + 1, i + 1])):
                        lin.append(-self.__Ligacoes.get(tuple([j + 1, i + 1]))['Admitância'])
                    else:
                        lin.append(0)
            for j in range(len(self.__ybus)):
                if i == j:
                    lin[j] = -1 * sum(lin)
            self.__ybus[i] = lin

        self.__printYbus()

        for i in self.__dados:
            if self.__dados.get(i)['code'] == 2:
                self.__nPQ += 1
            elif self.__dados.get(i)['code'] == 3:
                self.__nPV += 1

    def Sinjetada(self, mostrar):
        """
        Método utilizado para calcular as potências injetadas no circuito.
        E seta os valores de delta P e de delta Q.
        """
        self.__deltaPeQ = []
        self.__ResiduoP = []
        self.__ResiduoQ = []

        for i in self.__dados:
            soma1 = []
            soma2 = []
            if self.__dados[i]['code'] != 1:
                for j in self.__dados:
                    soma1.append(  # Apenas Potência ATIVA
                        abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(i)['tensao']) *
                        abs(self.__dados.get(j)['tensao']) *
                        mt.cos(np.angle(self.__ybus[i - 1][j - 1]) - self.__dados.get(i)['ang'] + self.__dados.get(j)[
                            'ang'])
                    )
                    soma2.append(  # Apenas Potência REATIVA
                        -abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(i)['tensao']) *
                        abs(self.__dados.get(j)['tensao']) *
                        mt.sin(np.angle(self.__ybus[i - 1][j - 1]) - self.__dados.get(i)['ang'] + self.__dados.get(j)[
                            'ang']) * 1j
                    )

                self.__ResiduoP.append(np.real(
                    self.__Sesp.get(i)['Pesp'] - sum(soma1)))  # Lista com os valores de cada barra != da barra |V| phi
                if self.__dados[i]['code'] == 2:
                    self.__ResiduoQ.append(np.imag((self.__Sesp.get(i)['Qesp']) * 1j - sum(soma2)))

        for i in range(len(self.__ResiduoP)):
            self.__deltaPeQ.append(self.__ResiduoP[i])
        for i in range(len(self.__ResiduoQ)):
            self.__deltaPeQ.append(self.__ResiduoQ[i])  # SEM O j

        if mostrar:
            for i in self.__deltaPeQ: print("delta P e Q da iteração [", self.count, "] \t=", i)

    def __setJ1(self, listAng, nPQ, nPV):
        """
        Método privado utilizado para calcular a submatriz J1 da matriz Jacobiana.

        :param listAng: Lista de ângulos a serem calculados no circuito. (Barras PQ e PV)
        :param nPQ: Número de barras PQ.
        :param nPV: Número de barras PV.
        :return: Retorna a submatriz J1.
        """
        self.__J1 = np.ones((nPQ + nPV, nPQ + nPV))

        mainDiagonal = []
        outDiagonal = []
        for i in listAng:
            soma = []
            for j in range(1, len(self.__dados) + 1, 1):
                if i != j:
                    soma.append(
                        abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(i)['tensao']) *
                        abs(self.__dados.get(j)['tensao']) *
                        cmt.sin(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__dados.get(i)['ang'] +
                                self.__dados.get(j)['ang'])
                    )
            mainDiagonal.append(sum(soma))

        for i in listAng:
            for j in listAng:
                if i != j:
                    outDiagonal.append(
                        -abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(i)['tensao']) *
                        abs(self.__dados.get(j)['tensao']) *
                        cmt.sin(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__dados.get(i)['ang'] +
                                self.__dados.get(j)['ang'])
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

        return self.__J1

    def __setJ2(self, listTensao, listAng, nPQ, nPV):
        """
        Método privado utilizado para calcular a submatriz J2 da matriz Jacobiana.

        :param listTensao: Lista de tensões a serem calculadas no circuito. (Barras PQ)
        :param listAng: Lista de ângulos a serem calculados no circuito. (Barras PQ e PV)
        :param nPQ: Número de barras PQ.
        :param nPV: Número de barras PV.
        :return: Retorna a submatriz J2.
        """
        self.__J2 = np.ones((nPQ + nPV, nPQ))

        mainDiagonal = []
        outDiagonal = []

        for i in listAng:
            soma = []
            a = 0
            for j in range(1, len(self.__dados) + 1, 1):

                if i != j:
                    soma.append(
                        abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(j)['tensao']) *
                        cmt.cos(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__dados.get(i)['ang'] +
                                self.__dados.get(j)['ang'])
                    )
            a = (2 * abs(self.__dados.get(i)['tensao']) * abs(self.__ybus[i - 1][i - 1]) *
                 cmt.cos(cmt.phase(self.__ybus[i - 1][i - 1]))
                 )
            mainDiagonal.append(a + sum(soma))

        for i in listAng:
            for j in listTensao:
                if i != j:
                    outDiagonal.append(
                        abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(i)['tensao']) *
                        cmt.cos(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__dados.get(i)['ang'] +
                                self.__dados.get(j)['ang'])
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

        return self.__J2

    def __setJ3(self, listTensao, listAng, nPQ, nPV):
        """
        Método privado utilizado para calcular a submatriz J3 da matriz Jacobiana.

        :param listTensao: Lista de tensões a serem calculadas no circuito. (Barras PQ)
        :param listAng: Lista de ângulos a serem calculados no circuito. (Barras PQ e PV)
        :param nPQ: Número de barras PQ.
        :param nPV: Número de barras PV.
        :return: Retorna a submatriz J3.
        """
        self.__J3 = np.ones((nPQ, nPQ + nPV))

        mainDiagonal = []
        outDiagonal = []
        for i in listAng:
            soma = []
            for j in range(1, len(self.__dados) + 1, 1):
                if i != j:
                    soma.append(
                        abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(i)['tensao']) *
                        abs(self.__dados.get(j)['tensao']) *
                        cmt.cos(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__dados.get(i)['ang'] +
                                self.__dados.get(j)['ang'])
                    )
            mainDiagonal.append(sum(soma))
        for i in listAng:
            for j in listAng:
                if i != j:
                    outDiagonal.append(
                        -abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(i)['tensao']) *
                        abs(self.__dados.get(j)['tensao']) *
                        cmt.cos(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__dados.get(i)['ang'] +
                                self.__dados.get(j)['ang'])
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

        return self.__J3

    def __setJ4(self, listTensao, listAng, nPQ, nPV):
        """
        Método privado utilizado para calcular a submatriz J4 da matriz Jacobiana.

        :param listTensao: Lista de tensões a serem calculadas no circuito. (Barras PQ)
        :param listAng: Lista de ângulos a serem calculados no circuito. (Barras PQ e PV)
        :param nPQ: Número de barras PQ.
        :param nPV: Número de barras PV.
        :return: Retorna a submatriz J4.
        """
        self.__J4 = np.ones((nPQ, nPQ))

        mainDiagonal = []
        outDiagonal = []
        for i in listAng:
            soma = []
            a = 0
            for j in range(1, len(self.__dados) + 1, 1):
                if i != j:
                    soma.append(
                        abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(j)['tensao']) *
                        cmt.sin(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__dados.get(i)['ang'] +
                                self.__dados.get(j)['ang'])
                    )
            a = (2 * abs(self.__dados.get(i)['tensao']) * abs(self.__ybus[i - 1][i - 1]) *
                 cmt.sin(cmt.phase(self.__ybus[i - 1][i - 1]))
                 )
            mainDiagonal.append(-a - sum(soma))
        for i in listAng:
            for j in listTensao:
                if i != j:
                    outDiagonal.append(
                        -abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(i)['tensao']) *
                        cmt.sin(cmt.phase(self.__ybus[i - 1][j - 1]) -
                                self.__dados.get(i)['ang'] +
                                self.__dados.get(j)['ang'])
                    )
        m = 0

        for i in range(nPQ):
            for j in range(nPQ):
                if i == j:
                    self.__J4[i][j] = np.real(mainDiagonal[j + nPV])
                else:
                    self.__J4[i][j] = np.real(outDiagonal[m])
                    m += 1

        return self.__J4

    def setJacob(self, listTensao, listAng, mostrarSubs):
        """
        Método utilizado para calcular a matriz Jacobiana.

        :param listTensao: Lista de tensões a serem calculadas no circuito. (Barras PQ)
        :param listAng: Lista de ângulos a serem calculados no circuito. (Barras PQ e PV)
        :param mostrarSubs: Deseja mostrar os valores das submatrizes J1, J2, J3 e J4 durante
        as iterações? Se sim, passar True como parâmetro.

        Printa a matriz Jacobiana.
        """

        self.__Jacob = []
        self.__listTensao = listTensao
        self.__listAng = listAng
        nXn = len(listTensao) + len(listAng)

        J1 = self.__setJ1(listAng, self.__nPQ, self.__nPV)  # (nPQ  + nPV) X (nPQ + nPV)
        J2 = self.__setJ2(listTensao, listAng, self.__nPQ, self.__nPV)  # (nPQ  + nPV) X (nPQ)
        J3 = self.__setJ3(listTensao, listAng, self.__nPQ, self.__nPV)  # (nPQ) X (nPQ + nPV)
        J4 = self.__setJ4(listTensao, listAng, self.__nPQ, self.__nPV)  # (nPQ) X (nPQ)

        self.__Jacob = np.zeros((nXn, nXn))

        for i in range(nXn):
            h = []
            k = []
            if i < len(J1):
                for j in range(len(J1[i])): h.append(J1[i][j])
                for j in range(len(J2[i])): h.append(J2[i][j])
                # geral[i] = np.hstack(h)
                self.__Jacob[i] = np.hstack(h)
            elif i >= len(J1):
                m = i - len(J1)
                for j in range(len(J3[m])): k.append(J3[m][j])
                for j in range(len(J4[m])): k.append(J4[m][j])
                # geral[i] = np.hstack(k)
                self.__Jacob[i] = np.hstack(k)
        if mostrarSubs:
            print('\n\n==================== MATRIZ JACOBIANA: ===========================')
            print("iteração [", self.count, "]")
            print('\nJ1 = ')
            for i in J1: print(i)
            print('\nJ2 = ')
            for i in J2: print(i)
            print('\nJ3 = ')
            for i in J3: print(i)
            print('\nJ4 = ')
            for i in J4: print(i)
            print('\nJACOB = ')
            for i in self.__Jacob: print(i)
            print('========================================================================')

    def linearSystem(self):
        """
        Método utilizado para calcular os resultados do sistema linear do passo 6 da aula 13.
        O sistema é do tipo:
            [delta P delta Q] = [Jacobiana] . [Resultado]
        """
        self.__x = []
        self.__x = np.linalg.solve(self.__Jacob, self.__deltaPeQ)
        deucerto = np.allclose(np.dot(self.__Jacob, self.__x), self.__deltaPeQ)
        # print('\n\t\tDEU CERTO? ', deucerto)

        ang = []
        tens = []
        for i in range(len(self.__x)):
            if i < (self.__nPQ + self.__nPV):
                ang.append(self.__x[i])
            else:
                tens.append(self.__x[i])
        m = 0
        for i in range(len(self.__dados)):
            if self.__dados.get(i + 1)['code'] != 1:
                # print('float(np.real(ang[m])) = ', float(np.real(ang[m])))
                self.__dados[i + 1]['ang'] += float(np.real(ang[m]))
                self.__angPlot[i + 1].append(self.__dados[i + 1]['ang'])
                m += 1
        m = 0
        for i in range(len(self.__dados)):
            if self.__dados.get(i + 1)['code'] == 2:
                # print('float(np.real(tens[m])) = ', float(np.real(tens[m])))
                self.__dados[i + 1]['tensao'] += float(np.real(tens[m]))
                self.__tensaoPlot[i + 1].append(self.__dados[i + 1]['tensao'])
                m += 1

    def NovaInjecao(self):
        """
        Método utilizado para calcular o novo valor de Injeção de potência aparente nas
        barras de folga e PV. (P e Q nas de folga e Q nas PV).
        """
        self.__Sbarras = dict()
        for i in self.__dados:
            soma1 = []
            soma2 = []
            if self.__dados[i]['code'] != 2:
                for j in self.__dados:
                    soma1.append(  # Apenas Potência ATIVA
                        abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(i)['tensao']) *
                        abs(self.__dados.get(j)['tensao']) *
                        mt.cos(np.angle(self.__ybus[i - 1][j - 1]) - self.__dados.get(i)['ang'] + self.__dados.get(j)[
                            'ang'])
                    )
                    soma2.append(  # Apenas Potência REATIVA
                        -abs(self.__ybus[i - 1][j - 1]) *
                        abs(self.__dados.get(i)['tensao']) *
                        abs(self.__dados.get(j)['tensao']) *
                        mt.sin(np.angle(self.__ybus[i - 1][j - 1]) - self.__dados.get(i)['ang'] + self.__dados.get(j)[
                            'ang']) * 1j
                    )
            if self.__dados[i]['code'] == 1:
                self.__Sbarras[i] = {'P': np.real(sum(soma1)), 'Q': np.imag(sum(soma2))}
            elif self.__dados[i]['code'] == 3:
                self.__Sbarras[i] = {'P': 0, 'Q': np.imag(sum(soma2))}

        for i in self.__dados:
            if self.__dados[i]['code'] == 1:
                self.__dados[i]['geracao'] = self.__Sbarras.get(i)['P'] + self.__Sbarras.get(i)['Q'] * 1j
            elif self.__dados[i]['code'] == 3:
                self.__dados[i]['geracao'] = np.real(self.__dados.get(i)['geracao']) + self.__Sbarras.get(i)['Q'] * 1j

    def solveCircuito(self, showSubMat=False, erro=None, iteracoes=None, listTensao=None, listAng=None):
        """
        Método genérico utilizado para 'resolver' o circuito.

        :param showSubMat: Parâmetro utilizado caso dejese-se mostrar os valores das variações
        de potências ativa e reativa, bem como as variações nas submatrizes em cada iteração.
        :param erro: Valor do erro utilizado para parar as iterações.
        :param iteracoes: Número de iterações que se deseja repetir o cálculo.
            Obs.: Deve-se passar ou um número de iterações ou um número para o erro.
        :param listTensao: Lista de tensões a serem calculadas no circuito. (Barras PQ)
        :param listAng: Lista de ângulos a serem calculados no circuito. (Barras PQ e PV)
        """
        self.__listTensao = listTensao
        self.__listAng = listAng
        self.count = 1
        self.ybus()
        self.Sinjetada(mostrar=showSubMat)
        self.setJacob(listTensao=self.__listTensao, listAng=self.__listAng, mostrarSubs=showSubMat)
        self.count += 1
        self.linearSystem()

        if iteracoes is None and erro is not None:
            pEq = list(map(abs, self.__deltaPeQ))
            teste = list(map(lambda m: True if (m < erro) else False, pEq))
            stop = teste.count(False)
            while True:
                self.Sinjetada(mostrar=showSubMat)
                self.setJacob(listTensao=self.__listTensao, listAng=self.__listAng, mostrarSubs=showSubMat)
                self.linearSystem()
                self.count += 1
                pEq = list(map(abs, self.__deltaPeQ))
                teste = list(map(lambda m: True if (m < erro) else False, pEq))
                stop = teste.count(False)
                # print('\n\nstop = ', stop, '\n\n')
                if stop == 0:
                    break
        elif iteracoes is not None and erro is None:
            while self.count < iteracoes:
                self.Sinjetada(mostrar=showSubMat)
                self.setJacob(listTensao=self.__listTensao, listAng=self.__listAng, mostrarSubs=showSubMat)
                self.linearSystem()
                self.count += 1

        self.NovaInjecao()
        # self.printBarras()
        if iteracoes is not None:
            print('\n======================= N° DE ITERAÇÕES = ', self.count)
        elif erro is not None:
            print('CONVERGIU PARA UM ERRO DE ', erro, ' .')
            print('CONVERGIU EM ', self.count, ' ITERAÇÕES. ')

    def __printTensao(self):
        """
        Método utilizado para printar os valores das tensões em cada barra. Em pu.
        """
        print('============================ TENSÕES: =======================================')
        for i in self.__V:
            print('Barra: \t', i, '\tTENSÃO = \t', self.__V.get(i), '\t[pu]')
        print('===============================================================================')

    def Tensoes(self, show=None):
        """
        Método utilizado para calcular as tensões em cada barra.
        O cálculo é feito a partir dos valores em pu e dos ângulos das tensões, os quais são
        oriundos das iterações do método "solveCircuito()".

        :param show: Caso dejese-se mostrar os valores das tensões em cada barra, deve-se passar
        True para o parâmetro "print".
        """
        self.__V = dict()
        for i in self.__dados:
            self.__V[i] = cmt.rect(self.__dados.get(i)['tensao'],
                                   self.__dados.get(i)['ang'])
        if show:
            print("")
            self.__printTensao()

    def __printCorrentes(self):
        """
        Método utilizado para printar as correntes em cada ligação.
        """
        print('============================ CORRENTES: =======================================')
        for i in self.__I:
            print('Ligação: \t', i, '\tCorrente = \t', self.__I.get(i), '\t[pu]')
        print('===============================================================================')

    def Correntes(self, show=None):  # Correntes calculadas considerando os ângulos das tensões.
        """
        Método utilizado para calcular os valores das correntes em cada linha.
        O cálculo é feito para todas as barras. Portanto, nas barras que não há ligação,
        o resultado deve ser 0. As correntes que representam ligações com as mesmas barras,
        seus valores são calculados como o somatório de todas as correntes da barra sob análise.

        :param show: Caso dejese-se mostrar os valores das correntes, deve-se passar
        True para o parâmetro "show".
        """
        self.__I = dict()
        self.Tensoes(show=None)
        for i in self.__dados:
            soma = []
            for j in self.__dados:
                if i == j:
                    continue
                else:
                    self.__I[(i, j)] = ((self.__V.get(i) - self.__V.get(j)) * self.__ybus[i - 1][j - 1])
                soma.append(((self.__V.get(i) - self.__V.get(j)) * self.__ybus[i - 1][j - 1]))
            self.__I[(i, i)] = sum(soma)
        if show:
            self.__printCorrentes()

    def powerFlow(self, printTensao=None, printCorrentes=None):
        """
        Método responsável por calcular o fluxo de potência em todas as ligações do sistema.


        :param printTensao: Caso dejese-se mostrar os valores das tensões em cada barra, deve-se passar
        True para o parâmetro "print".
        :param printCorrentes: Caso dejese-se mostrar os valores das correntes, deve-se passar
        True para o parâmetro "print".
        """
        self.__powerFlow = dict()
        self.Tensoes(show=printTensao)
        self.Correntes(show=printCorrentes)
        for i in self.__I:
            a = i[0]
            self.__powerFlow[i] = -self.__V.get(a) * np.conjugate(self.__I.get(i))
        print('======================== Fluxo de Potência: ===================================')
        for i in self.__powerFlow:
            print('Ligação: \t', i, '\tFluxo = \t', self.__powerFlow.get(i), '\t[pu]')
        print('===============================================================================')
        for i in self.__dados:
            if self.__dados.get(i)['code'] != 2:
                self.__dados[i]['geracao'] = self.__powerFlow.get((i, i))

    def losses(self):
        """
        Método utilizado para calcular as perdas do circuito.
        O cálculo é realizado pela soma de todas as potências.
        """
        self.__Perdas = 0
        perdas = []
        for i in self.__powerFlow:
            perdas.append(self.__powerFlow.get(i))
        self.__Perdas = sum(perdas)
        print('\n\nPerdas = \t', self.__Perdas, '\t[pu]')

    def __plotTensao(self):
        """
        Método privado utilizado apenas para plotar a convergência da tensão.
        """
        x = self.count - 1
        barras = []
        y = []
        plt.rcParams.update({'font.size': 20})
        for i in self.__dados:
            if self.__dados.get(i)['code'] == 2:
                barras.append(i)
        for i in barras:
            y.append(self.__tensaoPlot.get(i))
        for i in range(len(barras)):
            plt.subplot(len(barras), 1, i + 1)
            plt.plot(range(x + 1), y[i])
            plt.title('Variação da tensão na barra ' + str(barras[i]) + ' X Número de iterações')
            plt.xlabel('Número de iterações ')
            plt.ylabel('Tensão na barra ' + str(barras[i]) + ' pu')
            # plt.grid(True)
        plt.tight_layout()
        plt.show()

    def __plotAng(self):
        """
        Método privado utilizado apenas para plotar a convergência do ângulo das tensões nas barras.
        """
        x = self.count - 1
        barras = []
        y = []
        for i in self.__dados:
            if self.__dados.get(i)['code'] != 1:
                barras.append(i)
        for i in barras:
            y.append(self.__angPlot.get(i))
        for i in range(len(barras)):
            plt.subplot(len(barras), 1, i + 1)
            plt.plot(range(x + 1), y[i])
            plt.title('Variação do ângulo na barra ' + str(barras[i]) + ' X Número de iterações')
            plt.xlabel('Número de iterações ')
            plt.ylabel('Ângulo na barra ' + str(barras[i]) + ' [rad]')
            # plt.grid(True)
        plt.tight_layout()
        plt.show()

    def plotData(self, tensao=None, ang=None):
        """
        Método utilizado para plotar a convergência das tensões e dos ângulos calculados pelo algoritmo.

        :param tensao: Para plotar a tensão, deve-se passar "True" para este parâmetro.
        :param ang: Para plotar o ângulo, deve-se passar "True" para este parâmetro.
        """
        if tensao:
            self.__plotTensao()
        if ang:
            self.__plotAng()

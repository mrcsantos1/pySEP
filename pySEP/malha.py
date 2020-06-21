import math as mt
import cmath as cmt
import numpy as np


class Malha:
    def __init__(self):
        self.__solo = dict()
        self.__dimensoes = dict()
        self.__num_cond_shunt = dict()
        self.__comp_cond = {'hastes': 0,
                            'cabo': 0}

        self.__pa = float()
        self.__ps = float()
        self.__k = float()
        self.__cs = float()
        self.__t_protecao = float()
        self.__t_defeito = float()
        self.__v_toq_max = float()
        self.__v_passo_max = float()

        self.__i_cc = float()
        self.__i_malha = float()
        self.__temp_ambiente = float()
        self.__temp_max_per = float()
        self.__s_cobre = float()

        self.__res_malha = float()
        self.__N = float()
        self.__kii = float()
        self.__kp = float()
        self.__diametro = float()
        self.__km = float()
        self.__ki = float()
        self.__v_malha = float()
        self.__kpp = float()
        self.__v_psm = float()

        self.__teste = bool()
        self.__lim_seg_toq = bool()
        self.__lim_seg_passo = bool()

    def add_info_solo(self, num_camada, profundidade, resistividade):
        """
        profundidade [m]
        resistividade [ohm.m]
        """

        self.__solo['H' + str(num_camada)] = {
            'profundidade': profundidade,
            'resistividade': resistividade
        }

    def add_info_brita(self, profundidade, resistividade):
        """
        profundidade [m]
        resistividade [ohm.m]
        """
        self.__solo['Brita'] = {
            'profundidade': profundidade,
            'resistividade': resistividade
        }
        self.__ps = resistividade

    def add_t_protecao(self, t_protecao):
        self.__t_protecao = t_protecao

    def add_t_defeito(self, t_defeito):
        self.__t_defeito = t_defeito

    def add_temp_ambiente(self, temp_ambiente):
        self.__temp_ambiente = temp_ambiente

    def add_temp_max_permissivel(self, temp_max_permissivel):
        self.__temp_max_per = temp_max_permissivel

    def add_icc(self, i_cc):
        self.__i_cc = i_cc

    def add_i_malha(self, i_malha):
        self.__i_malha = i_malha

    def add_dimensoes(self, largura, comprimento, esp_larg, esp_compr,
                      profundidade_malha, malha_sem_hastes_na_periferia, malha_com_hastes_na_periferia):
        """
        ea = (0.05 - 0.10) a
        eb = (0.05 - 0.10) a
        e = espaçamento entre os condutores paralelos, e = máximo(ea,eb);
        """
        self.__dimensoes['largura'] = largura
        self.__dimensoes['comprimento'] = comprimento
        self.__dimensoes['ea'] = esp_larg * largura
        self.__dimensoes['eb'] = esp_compr * comprimento
        self.__dimensoes['area'] = largura * comprimento
        self.__dimensoes['profundidade'] = profundidade_malha
        self.__dimensoes['e_max'] = max([self.__dimensoes.get('ea'), self.__dimensoes.get('eb')])
        self.__dimensoes['e_min'] = min([self.__dimensoes.get('ea'), self.__dimensoes.get('eb')])
        if malha_com_hastes_na_periferia:
            self.__dimensoes['hastes_periferia'] = True
        elif malha_sem_hastes_na_periferia:
            self.__dimensoes['hastes_periferia'] = False

    def add_hastes(self, hastes):
        self.__comp_cond['hastes'] += hastes

    def show_solo(self):
        for i in self.__solo:
            print(i, '\t\tprof = ', self.__solo[i].get('profundidade'),
                  '\t\tresist = ', self.__solo[i].get('resistividade'))

    def calc_pa(self, profundidade, show):
        comp = profundidade
        select = []
        for i in self.__solo:
            if i != 'Brita':
                select.append(i)
                if comp >= self.__solo[i].get('profundidade'):
                    comp -= self.__solo[i].get('profundidade')
                    # print('\ncomp = ', comp)
                else:
                    break
        # print(select)
        _a = []
        b = []
        for i in select:
            if i == select[-1]:
                _a.append(comp)
                b.append(comp / self.__solo[i].get('resistividade'))
            else:
                _a.append(self.__solo[i].get('profundidade'))
                b.append(self.__solo[i].get('profundidade') / self.__solo[i].get('resistividade'))
        self.__pa = sum(_a) / sum(b)
        if show:
            self.__show_pa()

    def __show_pa(self):
        print('\npa = ', self.__pa, '\t[ohm.m]')

    def calc_k(self, show):
        self.__k = (self.__pa - self.__ps) / (self.__pa + self.__ps)
        if show:
            self.__show_k()

    def __show_k(self):
        print('\nk = ', self.__k)

    def calc_cs(self, iteracoes, show):
        def div(K, hs, n):
            x = pow(K, n)
            b = pow(((2 * n * hs) / 0.08), 2)
            c = mt.sqrt(1 + b)
            return x / c

        soma = []
        for i in range(1, iteracoes + 1, 1):
            soma.append(div(K=self.__k, hs=self.__solo['Brita'].get('profundidade'), n=i))
        soma = sum(soma)
        self.__cs = (1 + (2 * soma)) / 0.96

        if show:
            self.__show_cs()

    def __show_cs(self):
        print('\ncs = ', self.__cs)

    def calc_v_toq_max(self, show):
        x = 1.5 * self.__cs * self.__solo['Brita'].get('resistividade')
        y = 1000 + x
        z = (0.116 / mt.sqrt(self.__t_protecao))
        self.__v_toq_max = y * z
        if show:
            self.__show_v_toq_max()

    def __show_v_toq_max(self):
        print('\nV_toq_max = ', self.__v_toq_max, '\t[V]')

    def calc_v_passo_max(self, show):
        x = 6 * self.__cs * self.__solo['Brita'].get('resistividade')
        y = 1000 + x
        z = (0.116 / mt.sqrt(self.__t_protecao))
        self.__v_passo_max = y * z
        if show:
            self.__show_v_passo_max()

    def __show_v_passo_max(self):
        print('\nV_toq_max = ', self.__v_passo_max, '\t[V]')

    def calc_diametro(self):
        self.__diametro = mt.sqrt(4 * self.__s_cobre / mt.pi) / 1000

    def calc_s_cobre(self, show):
        menor = False
        om, oa = self.__temp_max_per, self.__temp_ambiente
        t_def = self.__t_defeito
        i = self.__i_cc
        log = mt.log(((om - oa) / (234 + oa)) + 1)
        raiz = mt.sqrt(log / t_def)
        self.__s_cobre = i / (226.53 * raiz)

        antes = 0
        if self.__s_cobre < 50:
            antes = self.__s_cobre
            self.__s_cobre = 50
            menor = True

        if show:
            self.__show_s_cobre(menor=menor, antes=antes)

        self.calc_diametro()

    def __show_s_cobre(self, menor, antes):
        print('\nScobre = ', self.__s_cobre, '\t[mm²]')
        if menor:
            print('Valor corrigido de: ', antes, '\t[mm²]')

    def calc_num_cond_paralelo(self, show):
        self.__num_cond_shunt['Na'] = int((self.__dimensoes.get('largura') / self.__dimensoes.get('ea')) + 1)
        self.__num_cond_shunt['Nb'] = int((self.__dimensoes.get('comprimento') / self.__dimensoes.get('eb')) + 1)
        if show:
            self.__show_num_cond_shunt()

    def __show_num_cond_shunt(self):
        print('\nNa = ', self.__num_cond_shunt.get('Na'), '\t[hastes no eixo X]')
        print('\nNb = ', self.__num_cond_shunt.get('Nb'), '\t[hastes no eixo Y]')

    def calc_comprimento_condutores(self, show, simples):
        """
        :param show: mostrar informações dos cálculos.
        :param simples: Se está no cálculo simples, True. Se está no cálculo detalhado, False.
        """
        if simples:
            self.__comp_cond['cabo'] = (
                    self.__dimensoes.get('largura') *
                    self.__num_cond_shunt.get('Nb') +
                    self.__dimensoes.get('comprimento') *
                    self.__num_cond_shunt.get('Na')
            )

            self.__comp_cond['total'] = self.__comp_cond.get('hastes') + self.__comp_cond.get('cabo')
        else:
            if self.__dimensoes.get('hastes_periferia') is False:
                self.__comp_cond['cabo'] = (
                        self.__dimensoes.get('largura') *
                        self.__num_cond_shunt.get('Nb') +
                        self.__dimensoes.get('comprimento') *
                        self.__num_cond_shunt.get('Na')
                )
                self.__comp_cond['total'] = self.__comp_cond.get('hastes') + self.__comp_cond.get('cabo')
            else:
                self.__comp_cond['cabo'] = (
                        self.__dimensoes.get('largura') *
                        self.__num_cond_shunt.get('Nb') +
                        self.__dimensoes.get('comprimento') *
                        self.__num_cond_shunt.get('Na')
                )
                self.__comp_cond['total'] = self.__comp_cond.get('cabo') + (self.__comp_cond.get('hastes') * 1.5)

        if show:
            self.__show_comp_cond()

    def __show_comp_cond(self):
        print('\nComprimento total dos condutores que formam a malha: ', self.__comp_cond.get('total'), '\t[m]')

    def calc_r_malha(self, show):
        x = 1 / self.__comp_cond.get('total')
        y = 1 / mt.sqrt(20 * self.__dimensoes.get('area'))
        z = self.__dimensoes.get('profundidade') * mt.sqrt((20 / self.__dimensoes.get('area')))
        z = (1 + (1 / (1 + z)))
        self.__res_malha = self.__pa * (x + y * z)

        if show:
            self.__show_r_malha()

    def __show_r_malha(self):
        print('\nR malha = ', self.__res_malha, '\t[ohm]')

    def testar_ri_v(self, profundidade_haste, show):
        self.calc_pa(profundidade=profundidade_haste, show=show)
        self.calc_k(show=show)
        self.calc_cs(iteracoes=3, show=show)
        self.calc_v_toq_max(show=show)
        self.calc_v_passo_max(show=show)
        self.calc_s_cobre(show=show)
        self.calc_num_cond_paralelo(show=show)
        self.calc_comprimento_condutores(show=show, simples=True)
        self.calc_r_malha(show=show)

        if self.__res_malha * self.__i_malha < self.__v_toq_max:
            self.__teste = True
        else:
            self.__teste = False
        if show:
            print('\nTeste = ', self.__teste)
            if self.__teste is False:
                print('Precisa calcular os potenciais de maneira mais precisa! ')
            elif self.__teste is True:
                print('Não precisa calcular os potenciais de maneira mais precisa! ')

    ####################################################################################################################

    def calc_n(self):
        self.__N = mt.sqrt(self.__num_cond_shunt.get('Na') * self.__num_cond_shunt.get('Nb'))

    def calc_kii(self, show=False):
        """
        𝐾𝑖𝑖 = coeficiente relacionado ao número de hastes cravadas:
        """
        self.calc_n()
        if self.__dimensoes.get('hastes_periferia') is False:
            self.__kii = 1 / pow((2 * self.__N), (2 / self.__N))
        elif self.__dimensoes.get('hastes_periferia') is True:
            self.__kii = 1
        if show:
            self.__show_kii()

    def __show_kii(self):
        print('\nKii = ', self.__kii)

    def calc_kp(self, show):
        self.__kp = mt.sqrt(1 + self.__dimensoes.get('profundidade'))
        if show:
            self.__show_kp()

    def __show_kp(self):
        print('\nKp = ', self.__kp)

    def calc_km(self, show):
        e = self.__dimensoes.get('e_max')
        h = self.__dimensoes.get('profundidade')
        d = self.__diametro
        n = self.__N
        x = pow(e, 2) / (16 * h * d)
        y = pow((e + (2 * h)), 2) / (8 * e * d)
        z = h / (4 * d)
        ln1 = mt.log(x + y - z)
        ln2 = mt.log(8 / (mt.pi * (2 * n - 1)))
        self.__km = (0.5 / mt.pi) * (ln1 + (self.__kii * ln2 / self.__kp))
        if show:
            self.__show_km()

    def __show_km(self):
        print('\nKm = ', self.__km)

    def calc_ki(self, show):
        self.__ki = 0.656 + (0.172 * self.__N)
        if show:
            self.__show_ki()

    def __show_ki(self):
        print('\nKi = ', self.__ki)

    def calc_v_malha(self, show):
        self.calc_comprimento_condutores(show=False, simples=False)
        self.__v_malha = (self.__pa * self.__km * self.__ki * self.__i_malha) / self.__comp_cond.get('total')
        if show:
            self.__show_v_malha()

    def __show_v_malha(self):
        print('\nVmalha = ', self.__v_malha, '\t[V]')

    def testar_vmalha_vtoq(self, show):

        self.calc_kii(show=show)
        self.calc_kp(show=show)
        self.calc_km(show=show)
        self.calc_ki(show=show)
        self.calc_v_malha(show=show)

        if self.__v_malha <= self.__v_toq_max:
            self.__lim_seg_toq = True
            print('\nLimite de segurança atendido! \nTensão de toque de malha <= Tensão de toque máxima')
        else:
            self.__lim_seg_toq = False
            print('\nLimite de segurança não atendido! '
                  '\nTensão de toque da malha é maior que a tensão de toque máxima! '
                  '\nÉ NECESSÁRIO MODIFICAR O PROJETO! ')

    def calc_kpp(self, show):
        """
        e = min(ea, eb)
        N = max(Na, Nb)
        :return:
        """
        e = self.__dimensoes.get('e_min')
        h = self.__dimensoes.get('profundidade')
        n = max([self.__num_cond_shunt.get('Na'), self.__num_cond_shunt.get('Nb')])

        x = 1 / (2 * h)
        y = 1 / (e + h)
        z = (1 - pow(0.5, (n - 2))) / e
        self.__kpp = (x + y + z) / mt.pi
        if show:
            self.__show_kpp()

    def __show_kpp(self):
        print('\nKpp = ', self.__kpp)

    def calc_vpsm(self, show):
        self.__v_psm = (self.__pa * self.__kpp * self.__ki * self.__i_malha) / self.__comp_cond.get('total')
        if show:
            self.__show_vpsm()

    def __show_vpsm(self):
        print('\nV_psm = ', self.__v_psm, '\t[V]')

    def testar_vpsm_vpasso(self, show):

        self.calc_kpp(show=show)
        self.calc_vpsm(show=show)

        if self.__v_psm <= self.__v_passo_max:
            self.__lim_seg_passo = True
            print('\nLimite de segurança atendido! \nTensão de passo de malha <= Tensão de passo máxima')
        else:
            self.__lim_seg_passo = False
            print('\nLimite de segurança não atendido! '
                  '\nTensão de passo de malha é maior que a tensão de passo máxima! '
                  '\nÉ NECESSÁRIO MODIFICAR O PROJETO! ')

    def get_info_solo(self):
        return self.__solo

# a = Malha()
# a.add_info_brita(profundidade=0.15, resistividade=3000)
# a.add_info_solo(num_camada=1, profundidade=0.8, resistividade=520)
# a.add_info_solo(num_camada=2, profundidade=1.2, resistividade=440)
# a.add_info_solo(num_camada=3, profundidade=1.8, resistividade=290)
# a.add_info_solo(num_camada=4, profundidade=1e3, resistividade=180)
#
# a.add_icc(i_cc=5e3)
# a.add_i_malha(i_malha=1.9e3)
# a.add_t_protecao(t_protecao=0.3)
# a.add_t_defeito(t_defeito=0.3)
# a.add_temp_ambiente(temp_ambiente=20)
# a.add_temp_max_permissivel(temp_max_permissivel=850)
#
# # a.add_hastes(hastes=2000)
#
# a.add_dimensoes(largura=120, comprimento=120, esp_larg=0.1, esp_compr=0.1, profundidade_malha=1.3,
#                 malha_com_hastes_na_periferia=False,
#                 malha_sem_hastes_na_periferia=True)
#
# a.show_solo()
# # a.calc_pa(1.3, show=True)
# # a.calc_k(show=True)
# # a.calc_cs(iteracoes=3, show=True)
# # a.calc_v_toq_max(show=True)
# # a.calc_v_passo_max(show=True)
# # a.calc_s_cobre(show=True)
# # a.calc_num_cond_paralelo(show=True)
# # a.calc_comprimento_condutores(show=True)
# #
# # a.calc_r_malha(show=True)
# a.testar_ri_v(show=True, profundidade_haste=1.3)
#
# # a.calc_kii(show=True)
# # a.calc_kp(show=True)
# # a.calc_km(show=True)
# # a.calc_ki(show=True)
# # a.calc_v_malha(show=True)
# a.testar_vmalha_vtoq(show=True)
#
# # a.calc_kpp(show=True)
# # a.calc_vpsm(show=True)
# a.testar_vpsm_vpasso(show=True)

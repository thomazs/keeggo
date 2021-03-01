#!/usr/bin/python3

"""
Teste de desenvolvimento criado para a empresa Keeggo
Data: 2021-03-01
Autor: Marcos Thomaz da Silva
"""

import random
from constantes import *
from dado import Dado
from excecoes import *
from comportamentos import *
from jogador import Jogador
from propriedade import Propriedade


__ALL__ = [
    'Jogador', 'Comportamento', 'ComportamentoImpulsivo', 'ComportamentoExigente', 'ComportamentoCauteloso',
    'ComportamentoAleatorio', 'Jogo'
]
  
class Jogo:
    
    def __init__(self, jogadores=4, propriedades=20, valor_aluguel_equiv_valor_venda=True, tipos_jogador_aleatorio=False, tipos_jogadores=None, mostra_jogo=False,
                 range_valores_propriedade = (50, 400), range_valores_aluguel = (10, 200), bonus_por_rodada = 100, max_rodadas = 1000):
        """
        Inicialização da classe Tabuleiro
        Parametros:
        jogadores = Lista de <Jogador> ou quantidade de jogadores
        propriedades = Lista de <Propriedade> ou quantidade de propriedades
        valor_aluguel_equiv_valor_venda = True / False. 
                    - Apenas se for informada a quantidade de propriedades.
                    - Se True, indica que o valor do aluguel será 1% do valor de venda
        tipos_jogador_aleatorio = True / False
                    - Apenas se <jogadores> for a quantidade de jogadores
                    - Indica se é pra pegar os tipos de jogador em ordem (False) ou
                      aleatoriamente (True)
        tipos_jogadores = list contendo os tipos de jogador a utilizar
        mostra_jogo = Se é para mostrar ou não o jogo "passo-a-passo" (True/False)
        range_valores_propriedade = tupla com o valor mínimo e máximo usado para gerar valor de venda de uma prop.
        range_valores_aluguel = tupla com o valor mínimo e máximo usado para gerar valor de aluguel de uma prop.
        bonus_por_rodada = Valor do bonus pago por final de rodada no tabuleiro
        max_rodadas = Quantidade máxima de rodadas antes de dar timeout
        """

        self.mostra_jogo = mostra_jogo        
        self.valor_aluguel_equiv_valor_venda = valor_aluguel_equiv_valor_venda
        self.tipos_jogador_aleatorio = tipos_jogador_aleatorio
        self.range_valores_propriedade = range_valores_propriedade
        self.range_valores_aluguel = range_valores_aluguel
        self.bonus_por_rodada = bonus_por_rodada
        self.max_rodadas = max_rodadas
        
        if tipos_jogadores:
            self._tipos_jogadores = tipos_jogadores
        else:
            self._tipos_jogadores = [
                ComportamentoImpulsivo, 
                ComportamentoExigente, 
                ComportamentoCauteloso, 
                ComportamentoAleatorio
            ] 
        
        if isinstance(propriedades, list):
            self.propriedades = propriedades
            # todo Validar se todas as propriedades informadas são da classe Propriedade
        else:
            # todo Validar se o parametro propriedade é do tipo inteiro
            self._cria_propriedades(propriedades)
            
        if isinstance(jogadores, list):
            self.jogadores = jogadores
            # todo Validade se todos os jogadores são da classe Jogador
        else:
            # todo Validar se o parametro jogadores é do tipo inteiro
            self._cria_jogadores(jogadores)
            
        self.__qtd_jogadores = len(self.jogadores)
        self.__qtd_perdedores = 0        
        self.__vencedor = None
        self.__rodada = 0
        
    def mostra_tabuleiro(self):
        if not self.mostra_jogo:
            return

        print("RODADA: ", self.__rodada)
        print()
        print("JOGADORES:")
        for j, p in self.jogadores:
           print(f"<{j.nome}, tipo: {j.tipo_jogador}, pos: {p}, saldo: {j.saldo}>  ", end="")
        print()
        print()
        print('PROPRIEDADES')
        for i, p in enumerate(self.propriedades, 1):
            prop = '%.2d' % i
            dono = (p.proprietario.nome if p.proprietario else '-').ljust(10)
            vv = '%10d' % p.valor_venda
            va = '%10d' % p.valor_aluguel
            print(f"[PROP{prop} - VL.V: {vv} - VL.A: {va} - PROP: {dono} ]         ", end="")
            if (i % 2 == 0):
                print()
        print()
        print()
        print(input())
        
    def _cria_propriedades(self, qtd_propriedades):
        self.propriedades = []
        for i in range(1, qtd_propriedades+1):
            vlvenda = random.randint(*self.range_valores_propriedade)
            vlalug = vlvenda // 100 if self.valor_aluguel_equiv_valor_venda else \
                    random.randint(*self.range_valores_aluguel)
            self.propriedades.append(
                Propriedade(
                    f"Propriedade {i}",
                    vlvenda,
                    vlalug,
                )
            )
    
    def _cria_jogadores(self, qtd_jogadores):
        self.jogadores = []
        for i in range(1, qtd_jogadores + 1):
            comp = random.choice(self._tipos_jogadores) if self.tipos_jogador_aleatorio else \
                    self._tipos_jogadores[(i-1) % 4]
            self.jogadores.append([
                Jogador(
                    f"Jogador {i}",
                    comp
                ),
                0  # posição
            ])
    
    def executa_rodada(self):
        """
        Efetua a jogada e retorna True caso exista um vencedor ou False quando não
        """
        self.__rodada += 1
        if self.__rodada == 1:
            self.mostra_tabuleiro()
        houve_vencedor = False
        for ijogador in range(len(self.jogadores)):
            jogador = self.jogadores[ijogador][0]
            if jogador.situacao == PERDEU:
                continue
        
            num_dado = Dado.jogada()
            jogador.realiza_jogada(num_dado)            
            ipropriedade = self.jogadores[ijogador][1] + num_dado
            
            # priorizando aqui o recebimento do bonus
            if ipropriedade >= len(self.propriedades):
                jogador.credita_bonus_volta_tabuleiro(self.bonus_por_rodada)
                
            ipropriedade = (ipropriedade - 1) % len(self.propriedades)
            self.jogadores[ijogador][1] = ipropriedade
            propriedade = self.propriedades[ipropriedade]

            pagou_alug = False
            comprou_prop = False
            
            # se tem proprietário, paga aluguel
            if propriedade.proprietario:
                pagou_alug = True
                jogador.paga_aluguel(propriedade)
                
            # se não tem verifica se é ou não para comprar
            elif jogador.pode_comprar(propriedade):
                comprou_prop = True
                jogador.efetua_compra(propriedade)

            if self.mostra_jogo:
                print("    > JOGADOR:", jogador.nome, " DADO:", num_dado, "  A:", pagou_alug, " C:", comprou_prop, " P:", ipropriedade)
                
            if jogador.situacao == PERDEU:
                self.__qtd_perdedores += 1                
                if self.__qtd_perdedores == self.__qtd_jogadores - 1:
                    houve_vencedor = True
                    break

        self.mostra_tabuleiro()
        return houve_vencedor

    def jogar(self):
        tem_vencedor = False
        for i in range(self.max_rodadas):
            tem_vencedor = self.executa_rodada()
            if tem_vencedor:
                break
                
        maior_saldo = max([j.saldo for j, i in self.jogadores])
        vencedor = []
        for j,i in self.jogadores:
            if j.situacao != PERDEU and (tem_vencedor or j.saldo == maior_saldo):
                vencedor.append(j.comportamento.tipo)
        
        return {
            'timeout': not tem_vencedor,
            'qtd_rodadas': self.__rodada,
            'vencedor': vencedor
        }        


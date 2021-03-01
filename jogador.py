#!/usr/bin/python3

"""
Teste de desenvolvimento criado para a empresa Keeggo
Data: 2021-03-01
Autor: Marcos Thomaz da Silva
"""

from constantes import *
from excecoes import *
from comportamentos import Comportamento


class Jogador:
    def __init__(self, nome, comportamento):
        self.nome = nome
        self.__saldo = 300
        self.log = []
        self.situacao = JOGANDO
        self.comportamento = comportamento

    def __str__(self):
        return self.nome
        
    @property
    def saldo(self):
        return self.__saldo
        
    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo
        if self.__saldo <= 0:
            self.situacao = PERDEU
            self.log.append(('Perdeu o jogo', None))
    
    @property
    def comportamento(self):
        return self._comportamento
       
    @comportamento.setter
    def comportamento(self, classComportamento):
        if not issubclass(classComportamento, Comportamento):
            raise EComportamentoInvalido()
        self._comportamento = classComportamento(self)
        
    def pode_comprar(self, propriedade):
        return self._comportamento.pode_comprar(propriedade)
        
    @property
    def tipo_jogador(self):
        return self._comportamento.tipo
        
    def efetua_compra(self, propriedade):
        if propriedade.proprietario:
            raise EPropriedadeJaComprada()
        self.log.append(('Comprou propriedade', propriedade))
        propriedade.proprietario = self
        self.saldo -= propriedade.valor_venda
        
    def paga_aluguel(self, propriedade):
        if not propriedade.proprietario:
            raise EPropriedadeNaoComprada()
        self.log.append(('Pagou aluguel', propriedade))
        self.saldo -= propriedade.valor_aluguel
        
    def credita_bonus_volta_tabuleiro(self, bonus):
        self.log.append(('Ganhou bonus de volta no tabuleiro', None))
        self.saldo += bonus
        
    def realiza_jogada(self, num_dado):
        self.log.append((f'Jogou o dado tirando {num_dado}', None))


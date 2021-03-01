#!/usr/bin/python3

"""
Teste de desenvolvimento criado para a empresa Keeggo
Data: 2021-03-01
Autor: Marcos Thomaz da Silva
"""

import random
from excecoes import *


class Comportamento:
    tipo = 'ComportamentoGeral'
    def __init__(self, jogador):
        self.__jogador = jogador    
	
    def pode_comprar(self, propriedade):
        return  self.saldo >= propriedade.valor_venda and \
                self._pode_comprar(propriedade)
    
    def _pode_comprar(self, propriedade):
        raise EAbstractMethod()

    @property
    def saldo(self):
        return self.__jogador.saldo


class ComportamentoImpulsivo(Comportamento):
    tipo = 'Impulsivo'
    def _pode_comprar(self, propriedade):
        return True


class ComportamentoExigente(Comportamento):
    tipo = 'Exigente'
    def _pode_comprar(self, propriedade):
        return propriedade.valor_aluguel > 50


class ComportamentoCauteloso(Comportamento):
    tipo = 'Cauteloso'
    def _pode_comprar(self, propriedade):
        return self.saldo - propriedade.valor_venda > 80


class ComportamentoAleatorio(Comportamento):
    tipo = 'Aleatório'
    def _pode_comprar(self, propriedade):
        return random.random() * 100 >= 50.0


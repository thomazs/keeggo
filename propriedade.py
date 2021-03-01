#!/usr/bin/python3

"""
Teste de desenvolvimento criado para a empresa Keeggo
Data: 2021-03-01
Autor: Marcos Thomaz da Silva
"""

from excecoes import *
from jogador import Jogador


class Propriedade:
	def __init__(self, nome, valor_venda, valor_aluguel, proprietario=None):
		self.nome = nome
		self.valor_venda = valor_venda
		self.valor_aluguel = valor_aluguel
		self.proprietario = proprietario
	
	@property
	def proprietario(self):
		return self._proprietario
		
	@proprietario.setter
	def proprietario(self, p):
		if p is None or isinstance(p, Jogador):
			self._proprietario = p
		else:
			raise EProprietarioInvalido()
		

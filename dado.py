#!/usr/bin/python3

"""
Teste de desenvolvimento criado para a empresa Keeggo
Data: 2021-03-01
Autor: Marcos Thomaz da Silva
"""

import random


class Dado:
	@classmethod
	def jogada(cls):
		return random.randint(1, 6)

#!/usr/bin/python3

"""
Teste de desenvolvimento criado para a empresa Keeggo
Data: 2021-03-01
Autor: Marcos Thomaz da Silva
"""

class EAbstractMethod(Exception):
	def __init__(self, message="Método _pode_comprar precisa ser implementado"):
		self.message = message
		super().__init__(self.message)


class EComportamentoInvalido(Exception):
    def __init__(self, message="Comportamento invalido repassado ao jogador"):
        self.message = message
        super().__init__(self.message)


class EPropriedadeJaComprada(Exception):
    def __init__(self, message="Propriedade já possui dono"):
        self.message = message
        super().__init__(self.message)    
        

class EPropriedadeNaoComprada(Exception):
    def __init__(self, message="Propriedade NÃO possui dono"):
        self.message = message
        super().__init__(self.message)    
        

class EProprietarioInvalido(Exception):
	def __init__(self):
		self.message = "Proprietário inválido!"
		super().__init__(self.message)


class EIntegridadeJogo(Exception):
    def __init__(self, message="Erro de integrdade do jogo"):
        self.message = message
        super().__init__(self.message)

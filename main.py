#!/usr/bin/python3

"""
Teste de desenvolvimento criado para a empresa Keeggo
Data: 2021-03-01
Autor: Marcos Thomaz da Silva
"""

import random
from jogo import *


def simulacao(qtd_jogos = 300):
    tipos_jogadores = [
        ComportamentoImpulsivo, 
        ComportamentoExigente, 
        ComportamentoCauteloso, 
        ComportamentoAleatorio
    ] 
    resultados = []
    print("="*50)
    print("SIMULACAO DE JOGO")
    print("="*50)
    for i in range(qtd_jogos):
        print(' - Simulação %.4d: Executando ' % (i+1), end='')

        # Para ver o jogo "passo-a-passo" basta passar o parametro mostra_jogo=True ao instanciar o jogo
        jogo = Jogo(tipos_jogadores=tipos_jogadores, valor_aluguel_equiv_valor_venda=False)
        resultado = jogo.jogar()
        print(' - Vencedor:', resultado['vencedor'], end='')
        resultados.append(resultado)
        print(' - Concluído')
    
    print()
    print()
    print('Calculando estatísticas...', end='')
    
    partidas_por_timeout = 0
    qtd_turnos = 0
    vitoria_tipos = {t.tipo: 0 for t in tipos_jogadores}
    vitoria_tipos_uk = {t.tipo: 0 for t in tipos_jogadores}
    qtd_empates = 0
    for r in resultados:
        if r['timeout']:
            partidas_por_timeout += 1
        
        qtd_turnos += r['qtd_rodadas']
        
        if len(r['vencedor']) > 1:
            qtd_empates += 1
        
        else:
            vitoria_tipos_uk[r['vencedor'][0]] += 1
            
        for v in r['vencedor']:
            vitoria_tipos[v] += 1
    
    # diferente de qtd.jogadas pois podem existir empates
    total_vitorias = sum(vitoria_tipos.values())  
    total_vitorias_uk = sum(vitoria_tipos_uk.values())      
    
    print(" OK")
    print()
    print()
    print("-" * 50)
    print("ESTATÍSTICAS")
    print("-" * 50)
    print(" - Quantidade real de partidas jogadas: ", qtd_jogos)
    print(" - Quantidade de partidas que terminaram em timeout:", partidas_por_timeout)
    print(" - Quantidade média de turnos de uma partida: %.2f" % (qtd_turnos / qtd_jogos))
    print(" - Quantidade total de turnos jogados: ", qtd_turnos)    
    print(" - Quantidade de empates: ", qtd_empates)
    print(" - Porcentagem de Vitórias por Comportamento:")
    maior = None
    for i in sorted(vitoria_tipos, key=lambda x: vitoria_tipos[x], reverse=True):
        if not maior:
            maior = i
        print(
            "   -> ", 
            i.rjust(12, ' '), 
            "- Qtd.Vit: %4d" % vitoria_tipos[i], 
            "(%3.1f%%)" % (vitoria_tipos[i] / total_vitorias * 100),
            "- Qt.Vit.S/Empat: %4d" %  vitoria_tipos_uk[i],
            "(%3.1f%%)" % (vitoria_tipos_uk[i] / total_vitorias_uk * 100 if total_vitorias_uk > 0 else 0),
            " => ",
            "#" * int((vitoria_tipos[i] / total_vitorias) * 100)
        )
    print(" - Comportamento que mais venceu: ", maior)
    print('='*50)
    print()
    print()


if __name__ == '__main__':
    qtd = input('Qual a quantidade de simulações (padrão 300):')
    qtd = int(qtd) if qtd else 300
    simulacao(qtd)

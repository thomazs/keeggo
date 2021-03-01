# keeggo

## Descrição
Código desenvolvido para o desafio da Keeggo/BrasilPrev.


## Tecnologias utilizadas
- Linguagem Python 3.9


## Pré-requisitos
Sem pré-requisitos ou bibliotecas adicionais


## Para Executar
No console, basta executar:
```
python main.py
```

A eecução apresenta apenas linhas responsáveis pela execução, além dos resultados estatísticos, porém mudando o parâmetro na execução (dentro do main.py) é possível ver as rodadas "passo-a-passo".


## Lógica e Recursos Aplicados
Não havia sido considerado no desafio as condições de empate, que poderiam ocorrem quando a execução de um jogo fosse interrompida por timeout.
A condição foi adicionada e, além das estatísticas solicitadas, são apresentadas as estatísticas únicas, isto é, considerando apenas a não ocorrência de empate.
Para os tipos de comportamento foi criada uma classe Comportamento, e dela, criadas 4 subclasses, responsáveis por controlar as ações conforme o comportamento.
A classe pai leva em consideração a existência de fundos (saldo >= valor da propriedade), enquanto que as classes filho levam em consideração características únicas.
Isso permite expandir os experimentos e simulações, aplicando e agregando novos comportamentos com praticamente nenhuma mudança no código, uma vez que os comportamentos a serem analisados podem ser passados a partir da função de simulação, existente no arquivo main.py
Foram adicionadas validações de tipo, além do controle de visibilidade e acesso dos métodos (usando properties). 
Também foi criado um log do Jogador, que iria mapear todas as ocorrências envolvendo o mesmo. Em um ambiente real, isso poderia acarrear na geração de um novo perfil de simulação. 


### Estrutura de Arquivos
- comportamentos.py - Arquivo contendo a classe e subclasses responsáveis pelos comportamentos/perfis.
- constantes.py - Arquivo com constantes gerais
- dado.py - Arquivo com a classe responsável por simular o "lançar do dado". Criada uma classe pois seria possível mudar o comportamento, levando em conta características e variáveis adicionais.
- excecoes.py - Arquivo com as exceções customizadas que poderiam ser lançadas pelo sistema
- jogador.py - Arquivo com a classe responsável por definir os jogadores
- propriedade.py - Arquivo com a classe responsável por definir as propriedades
- jogo.py - Arquivo com a classe responsável por gerenciar o jogo, definir quantidade de propriedades, quantidade de jogadores e regras adicionais
- main.py - Arquivo principal, responsável pela execução das simulações. 


### Exemplo de Execução
Exemplo da apresentação das estatísticas
```
--------------------------------------------------
ESTATÍSTICAS
--------------------------------------------------
 - Quantidade real de partidas jogadas:  300
 - Quantidade de partidas que terminaram em timeout: 0
 - Quantidade média de turnos de uma partida: 14.18
 - Quantidade total de turnos jogados:  4254
 - Quantidade de empates:  0
 - Porcentagem de Vitórias por Comportamento:
   ->     Cauteloso - Qtd.Vit:  127 (42.3%) - Qt.Vit.S/Empat:  127 (42.3%)  =>  ##########################################
   ->     Aleatório - Qtd.Vit:   68 (22.7%) - Qt.Vit.S/Empat:   68 (22.7%)  =>  ######################
   ->      Exigente - Qtd.Vit:   63 (21.0%) - Qt.Vit.S/Empat:   63 (21.0%)  =>  #####################
   ->     Impulsivo - Qtd.Vit:   42 (14.0%) - Qt.Vit.S/Empat:   42 (14.0%)  =>  ##############
 - Comportamento que mais venceu:  Cauteloso
==================================================
```

No final de cada comportamento, é visto uma sequencia de caracteres # (hashtag), que simbolizam um gráfico gerado a partir do percentual de execução.

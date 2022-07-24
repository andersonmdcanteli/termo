<img src="icon.PNG" align="right" />

# Os melhores (ou o piores) chutes para o Termo!

### Descubra quais são as melhores palavras para começar o jogo termo!

Esse repositório guarda os scripts (Python) utilizados para determinar quais os melhores chutes possíveis para acertar a palavra do dia em jogos tipo Termo. Através de análise estatística, foi possível estimar quais as melhores palavras para serem utilizadas considerando duas condições:

1. Uma única palavra (sem repetição de letras)
2. Duas palavras (sem repetição de letras)
3. Três palavras (sem repetição de letras)   ---> Análise não finalizada


## Resultados

### Uma única palavra

#### Top 10 melhores palavras para o primeiro chute

| Palavra | "Força" |
| - | - |
| serao | 0.084141 |
| terao | 0.081602 |
| lerao | 0.080955 |
| verao | 0.080237 |
| meiao | 0.079954 |
| coras | 0.078370 |
| senao | 0.077442 |
| ceras | 0.077387 |
| moras | 0.077378 |
| roias | 0.077286 |


## Análise dos dados

Todos os detalhes relacionados análise estatística, códigos e premissas adotadas para encontrar as melhores palavras estão descritas [neste notebook](https://github.com/andersonmdcanteli/termo/blob/main/termo_analysis.ipynb), que também esta disponível via [google drive](https://colab.research.google.com/drive/1vmq6Hq2CaDEudNHVUDNd9e6bS1fikJqj?usp=sharing).

## Dashboard

Um dashboard onde para encontrar a força de uma palavra específica foi desenvolvido e o código esta disponível na sub-pasta **[dashboard](https://github.com/andersonmdcanteli/termo/tree/main/dashboard)**. É possível alterar a forma de cálculo e a quantiadde de palavras. A Figura abaixo é um print da versão final.


<p align="center">
<img src="https://raw.githubusercontent.com/andersonmdcanteli/termo/main/images/screenshot.PNG" alt="screenshot doa dashboard finalizando, mostrando o painel de confingurações" width="800px">
</p>

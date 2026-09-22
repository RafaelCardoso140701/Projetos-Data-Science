# Análise Exploratória — Base de Filmes

Análise exploratória sobre avaliações e características de filmes, combinando
duas fontes: o **MovieLens** (notas atribuídas por usuários) e o **TMDB**
(orçamento, receita e metadados de produção).

## O que a análise cobre

**Distribuição das notas** — frequência das avaliações na escala de 0,5 a 5
estrelas, com comparação entre média e mediana e leitura da assimetria por
histograma e boxplot.

**Características dos filmes** — separação dos gêneros, que chegam concatenados
por `|` numa única coluna, e contagem de ocorrências por categoria.

**Orçamento e receita** — distribuição de ambos no TMDB, com recorte dos filmes
que efetivamente registraram faturamento (`revenue > 0`). Boa parte da base tem
valor zero, o que distorce a distribuição se incluída.

**Idioma original** — contagem por idioma, evidenciando a concentração em inglês.

## Dados

As três bases são lidas diretamente por URL, sem necessidade de download:

| Base | Conteúdo |
|---|---|
| `ratings.csv` | 100.836 avaliações de 610 usuários |
| `movies.csv` | 9.742 filmes com título e gêneros |
| `tmdb_5000_movies.csv` | Orçamento, receita, idioma e metadados de produção |

Fonte: [MovieLens](https://grouplens.org/datasets/movielens/) (GroupLens,
Universidade de Minnesota) e [TMDB](https://www.themoviedb.org/).

## Executar

```bash
pip install pandas seaborn matplotlib
jupyter notebook analise_exploratoria_filmes.ipynb
```

O notebook roda de cima a baixo sem configuração — os dados vêm da rede.

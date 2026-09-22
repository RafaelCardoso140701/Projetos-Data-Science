# Projetos de Data Science

Coleção de projetos de análise de dados e machine learning, cobrindo o ciclo
completo: análise exploratória, tratamento, modelagem, deploy e consumo do
modelo treinado.

**Rafael Cardoso Nascimento** · [GitHub](https://github.com/RafaelCardoso140701)

`Python` `pandas` `scikit-learn` `matplotlib` `seaborn` `joblib`

---

## Projetos

### [Classificação — Titanic](classificacao-titanic/)

Previsão de sobrevivência dos passageiros do Titanic, percorrendo o fluxo
completo de um problema de classificação binária.

| Notebook | O que faz |
|---|---|
| `1_analise_exploratoria.ipynb` | Distribuições, correlações e primeiras hipóteses |
| `2_tratamento_de_dados.ipynb` | Valores ausentes, codificação de variáveis categóricas, engenharia de atributos |
| `3_modelos_classificacao.ipynb` | Regressão Logística, Árvore de Decisão e KNN, com comparação de métricas |

**Técnicas:** Logistic Regression · Decision Tree · K-Nearest Neighbors
**Dados:** `data/titanic_train.csv`, `data/titanic_test.csv`

---

### [Regressão — Preços de Imóveis](regressao-precos-casas/)

Modelo de regressão linear para prever o valor mediano de imóveis, com ênfase na
etapa que costuma ficar de fora: **serializar o modelo e consumi-lo depois**.

| Arquivo | O que faz |
|---|---|
| `1_treino_e_deploy.ipynb` | Treina o modelo e serializa com `joblib` |
| `2_consumo_do_modelo.ipynb` | Carrega o modelo salvo e gera previsões sobre dados novos |
| `ModeloML.py` | Script de inferência em lote, executável pela linha de comando |

**Técnicas:** Linear Regression · serialização com joblib · inferência em lote
**Dados:** `data/casas_treino.csv`, `data/casas_teste.csv`

O script de inferência depende do modelo serializado. Gere-o executando antes o
notebook `1_treino_e_deploy.ipynb`, que salva o `regressao.joblib` na pasta do
projeto. Depois:

```bash
cd regressao-precos-casas
python ModeloML.py --modelo regressao.joblib --entrada data/casas_teste.csv --saida previsoes.xlsx
```

---

### [Clustering — K-Means](clustering-kmeans/)

Aprendizado não supervisionado aplicado a agrupamento: escolha do número de
clusters, interpretação dos grupos e visualização das fronteiras.

**Técnicas:** K-Means · método do cotovelo · avaliação de clusters

---

### [Análise Exploratória — Gêneros Musicais](analise-generos-musicais/)

Exploração de preferências de streaming musical pelo mundo, comparando uma EDA
manual com a geração automática de relatório via `pandas-profiling`.

| Notebook | O que faz |
|---|---|
| `1_analise_exploratoria.ipynb` | EDA manual, com clusterização de perfis de ouvintes |
| `2_eda_pandas_profiling.ipynb` | Relatório automatizado com ydata-profiling |

**Dados:** `Global_Music_Streaming_Listener_Preferences.csv` — não versionado por
tamanho. Veja o README da pasta para a origem.

---

## Como executar

```bash
git clone https://github.com/RafaelCardoso140701/Projetos-Data-Science.git
cd Projetos-Data-Science
pip install -r requirements.txt
jupyter notebook
```

Cada projeto é independente: os notebooks leem os dados da subpasta `data/` do
próprio projeto e podem ser executados de cima a baixo sem configuração extra.

## Estrutura

```
Projetos-Data-Science/
├── analise-generos-musicais/
├── classificacao-titanic/
│   └── data/
├── clustering-kmeans/
├── regressao-precos-casas/
│   └── data/
└── requirements.txt
```

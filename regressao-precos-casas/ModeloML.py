"""
Inferencia em lote com o modelo de regressao serializado.

Carrega um modelo treinado (.joblib), aplica sobre um arquivo de entrada e
exporta as previsoes.

Uso:
    python ModeloML.py
    python ModeloML.py --entrada data/casas_teste.csv --saida previsoes.xlsx
"""

import argparse
from pathlib import Path

import pandas as pd
from joblib import load

COLUNA_ALVO = "MedHouseVal"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Gera previsoes a partir do modelo salvo")
    parser.add_argument("--modelo", default="regressao.joblib", help="Arquivo .joblib do modelo treinado")
    parser.add_argument("--entrada", default="data/casas_teste.csv", help="CSV com os dados de entrada")
    parser.add_argument("--saida", default="previsoes_modelo.xlsx", help="Arquivo de saida (.xlsx)")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    modelo = Path(args.modelo)
    entrada = Path(args.entrada)

    if not modelo.exists():
        raise SystemExit(
            f"Modelo nao encontrado: {modelo}\n"
            "Execute antes o notebook 1_treino_e_deploy.ipynb para gera-lo."
        )
    if not entrada.exists():
        raise SystemExit(f"Arquivo de entrada nao encontrado: {entrada}")

    print(f"Lendo {entrada}")
    dados = pd.read_csv(entrada)

    # Coluna de indice residual da exportacao original
    if "Unnamed: 0" in dados.columns:
        dados = dados.drop("Unnamed: 0", axis=1)

    X = dados.drop(COLUNA_ALVO, axis=1) if COLUNA_ALVO in dados.columns else dados.copy()

    print(f"Carregando modelo {modelo}")
    regressor = load(modelo)

    print(f"Gerando previsoes para {len(X):,} registros")
    X["previsao"] = regressor.predict(X)

    X.to_excel(args.saida, index=False)
    print(f"Previsoes salvas em {args.saida}")


if __name__ == "__main__":
    main()

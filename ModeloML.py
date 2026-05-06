# Importando o arquivo de teste
import pandas as pd
teste = pd.read_csv('/Users/llucaslleall/Desktop/Minicurso/6 Deploy/Usuarios/casas_teste.csv')

# Fazendo o load do modelo
import sklearn
from joblib import load
reg = load('/Users/llucaslleall/Desktop/Minicurso/6 Deploy/Modelo/regressao.joblib')

# Fazendo a previsão
teste = teste.drop('Unnamed: 0',axis=1)
X_teste = teste.drop('MedHouseVal',axis=1)


# Exportando esse arquivo
previsao = reg.predict(X_teste)
X_teste['previsao'] = previsao
import openpyxl
X_teste.to_excel('/Users/llucaslleall/Desktop/Minicurso/6 Deploy/Usuarios/previsoes_modelo.xlsx')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot

''' Regressão linear simples com os grupos divididos dos países com o maior consumo de cada bebida'''

#Carregamento do dataframe inicial
bebida = pd.read_csv('Consumo de bebidas alcoólicas ao redor do mundo.csv')

#Separação dos países com o grupo marjoritário de cada bebida, exceto os países não alcoólicos
maioria_cerveja = []
maioria_destilados = []
maioria_vinho = []

for index, column in bebida.iterrows():
   if column['beer_servings'] > column['spirit_servings'] and column['beer_servings'] > column['wine_servings']:
       maioria_cerveja.append(column)
   elif column['spirit_servings'] > column['beer_servings'] and column['spirit_servings'] > column['wine_servings']:
       maioria_destilados.append(column)
   elif column['wine_servings'] > column['beer_servings'] and column['wine_servings'] > column['spirit_servings']:
       maioria_vinho.append(column)

def tabela(x):
    x = pd.DataFrame(list(x))
    x.columns = ['country', 'beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol']
    return x

maioria_cerveja = tabela(maioria_cerveja)
maioria_destilados = tabela(maioria_destilados)
maioria_vinho = tabela(maioria_vinho)

'''1)Regressão linear da cerveja marjoritária VS total álcool ingerido'''

#Seleciona as colunas para serem as variáveis explanatória e resposta, respectivamente
X = maioria_cerveja.iloc[:, 1].values 
y = maioria_cerveja.iloc[:, 4].values 
correlacao_cerveja = np.corrcoef(X, y)

#Criação do modelo de regressão linear
X = X.reshape(-1, 1)
modelo_cerveja = LinearRegression()
modelo_cerveja.fit(X, y)

#Mostra a acurácia do modelo de regresão linear da cerveja
score_cerveja = modelo_cerveja.score(X, y)

#Mostra a interceptação e inclinação da reta de regressão linear do modelo, respectivamente
modelo_cerveja.intercept_
modelo_cerveja.coef_

#Gráfico da regressão linear da cerveja
plt.scatter(X, y)
plt.title('Quantidade de cerveja ingerida por ano', fontsize = 16)
plt.xlabel('Copos de cerveja por pessoa')
plt.ylabel('Total de álcool ingerido (L)')
plt.plot(X, modelo_cerveja.predict(X), color = 'red')

#Calculo manual e utilizando o modelo para prever o valor de y, respectivamente
modelo_cerveja.intercept_ + modelo_cerveja.coef_ * 400
modelo_cerveja.predict([[400]])

''' Cerveja - Como no estudo não informou uma porção em litros como referência, podemos fazer suposições a partir desse modelo
por exemplo, se uma pessoa bebe 400 copos de cerveja por ano, e adotando um copo de cerveja com 300 ml (0,3L), uma
pessoa que bebe 400 copos por ano (dependendo de cada país, obviamente), bebe 120 litros de cerveja, e só de alcool puro,
uma pessoa bebe, aproximadamente, 12.47 litros de álcool (cerca de 10.39% aproximadamente) '''

#Visualização dos resíduos e o seu gráfico(resultado entre a distância dos pontos com a linha de regressão)
modelo_cerveja._residues

visualizador_cerveja = ResidualsPlot(modelo_cerveja)
visualizador_cerveja.fit(X, y)
visualizador_cerveja.poof()

'''2)Regressão linear de destilados marjoritários VS total álcool ingerido'''

A = maioria_destilados.iloc[:, 2].values 
b = maioria_destilados.iloc[:, 4].values 
correlacao_destilados = np.corrcoef(A, b)

A = A.reshape(-1, 1)
modelo_destilados = LinearRegression()
modelo_destilados.fit(A, b)

score_destilados = modelo_destilados.score(A, b)

modelo_destilados.intercept_
modelo_destilados.coef_

plt.scatter(A, b)
plt.title('Quantidade de destilados ingerido por ano', fontsize = 16)
plt.xlabel('Copos de destilados por pessoa')
plt.ylabel('Total de álcool ingerido (L)')
plt.plot(A, modelo_destilados.predict(A), color = 'yellow')

modelo_destilados.intercept_ + modelo_destilados.coef_ * 400
modelo_destilados.predict([[400]])

'''Destilado - Como no estudo não informou uma porção em litros como referência, podemos fazer suposições a partir desse modelo
por exemplo, se uma pessoa bebe 400 copos de destilados por ano, e adotando um copo de destilado com 100 ml (0,1L), uma
pessoa que bebe 400 copos por ano (dependendo de cada país, obviamente), bebe 40 litros de destilado, e só de alcool puro,
uma pessoa bebe, aproximadamente, 11.85 litros de álcool (cerca de 29.63% aproximadamente) '''

modelo_destilados._residues

visualizador_destilados = ResidualsPlot(modelo_destilados)
visualizador_destilados.fit(A, b)
visualizador_destilados.poof()

'''3)Regressão linear de vinho marjoritário VS total álcool ingerido'''

C = maioria_vinho.iloc[:, 3].values  
d = maioria_vinho.iloc[:, 4].values 
correlacao_vinho = np.corrcoef(C, d)

C = C.reshape(-1, 1)
modelo_vinho = LinearRegression()
modelo_vinho.fit(C, d)

modelo_vinho.intercept_
modelo_vinho.coef_

score_vinho = modelo_vinho.score(C, d)

plt.scatter(C, d)
plt.title('Quantidade de vinho ingerido por ano', fontsize = 16)
plt.xlabel('Taças de vinho por pessoa')
plt.ylabel('Total de álcool ingerido (L)')
plt.plot(C, modelo_vinho.predict(C), color = 'purple')

modelo_vinho.intercept_ + modelo_vinho.coef_ * 400
modelo_vinho.predict([[400]])

'''Vinho - Como no estudo não informou uma porção em litros como referência, podemos fazer suposições a partir desse modelo
por exemplo, se uma pessoa bebe 400 copos de destilados por ano, e adotando uma taça de de vinho com 450 ml (0,45L),
entretanto uma pessoa só bebe cerca de 1/3 da taça então uma pessoa bebe 150 ml (0,15L), uma pessoa que bebe 400 copos
por ano (dependendo de cada país, obviamente), bebe 60 litros de vinho, e só de alcool puro,uma pessoa bebe,
aproximadamente, 13.96 litros de álcool (cerca de 23.26% aproximadamente) '''

modelo_vinho._residues

visualizador_vinho = ResidualsPlot(modelo_vinho)
visualizador_vinho.fit(C, d)
visualizador_vinho.poof()   
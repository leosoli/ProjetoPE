# -*- coding: utf-8 -*-
'''
Preparação do arquivo 'CasasTop.csv'

Este módulo realiza a preparação do arquivo CasasTop.csv para criação do chatbot. O arquivo 'kc_house_data.csv', que
contém uma lista mais completa de casas, é carregado e, a partir dele, é gerado um novo arquivo 'CasasTop.csv', com
apenas os dados referentes às casas com zipcode igual a "98055". Nesse arquivo 'CasasTop.csv', também é adicionada uma
nova coluna chamada 'Caro??', que possui valor 1, se o preço por pé quadrado dessa casa é maior do que a média ou 0, caso
contrário.
O arquivo 'kc_house_data.csv' não possui as 10 últimas linhas da tabela filtrada, pois essas últimas linhas são exportadas
para um novo arquivo chamado 'autoavaliacao.csv', a ser usado para testes com o chatbot pronto.

Entrada:	kc_house_data.csv
	
Saídas:		CasasTop.csv
		autoavaliacao.csv
'''

import pandas as pd

# Carregando arquivo com todas as casas originalmente existentes
data = pd.read_csv('kc_house_data.csv', sep=',')

# Filtrando dados para apenas as casas pertencentes ao zipcode 98055
data_98055 = data.query("zipcode==98055")
data_98055 = data_98055.reset_index(drop=True)

# Adicionado coluna com o preço por pé quadrado
data_98055['price_sqft_living'] = data_98055['price']/data_98055['sqft_living']

# Média do preço por pé quadrado arredondada na 2ª casa decimal
media = round(data_98055['price_sqft_living'].mean(), 2)

# Adicionando coluna 'Caro??', com 1 sendo verdadeiro e 0 caso contrário
data_98055['Caro??'] = data_98055['price_sqft_living'] > media
data_98055['Caro??'] = data_98055['Caro??'].replace([False, True], [0, 1])

# Eliminando a coluna de preço por pé quadrado
data_98055 = data_98055.drop(['price_sqft_living'], axis = 1)

# Separando as 10 últimas linhas para usar como autoavaliação ao final do desenvolvimento do chatbot
autoavaliacao = data_98055.tail(10)

# Eliminando as 10 ultimas linhas para não serem mais usadas durante a criação do chatbot
data_98055 = data_98055[:-10]

# Impressão das tabelas
print("\n-------------------------------------------------------------------------------------")
print('Tabela para construcao do chatbot')
print("-------------------------------------------------------------------------------------")
print(data_98055)
print("\n-------------------------------------------------------------------------------------")
print('Tabela para autoavaliacao do chatbot')
print("-------------------------------------------------------------------------------------")
print(autoavaliacao)
print()

# Exportando os dados das casas para processo de construção do chatbot como 'CasasTop.csv'
data_98055.to_csv(r'CasasTop.csv', index=False)
print('Arquivo CasasTop.csv gerado.')

# Exportando as 10 casas para serem usadas na autoavaliação do chatbot
autoavaliacao.to_csv(r'autoavaliacao.csv', index=False)
print('Arquivo autoavaliacao.csv gerado.')

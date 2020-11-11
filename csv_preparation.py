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

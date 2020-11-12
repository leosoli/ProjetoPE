# -*- coding: utf-8 -*-
'''
Geração da árvore de decisão

Este módulo utiliza o arquivo CasasTop.csv, gerado pelo csv_preparation.py. Utilizando somente as colunas
desejadas, é gerado a árvore de decisão através do arquivo tree_chatbot, contendo as ligações entre os
nós e seus respectivos critérios de análise

Entrada:	CasasTop.csv
Saídas:		tree_chatbot.dot
'''

import pandas as pd
from sklearn import tree

#Lendo o arquivo CasasTop.csv
train = pd.read_csv('CasasTop.csv')

#Selecionando as colunas desejadas para manter no dataset
keep_elements = ['bedrooms', 'bathrooms', 'floors', 'waterfront', 'view', 'condition', 'grade', 'Caro??']
train = train[keep_elements]

#Criando a árvore de decisão
y_train = train['Caro??']
x_train = train.drop(['Caro??'], axis=1).values
decision_tree = tree.DecisionTreeClassifier(max_depth = 20)
decision_tree.fit(x_train, y_train)

#Escrevendo o arquivo
with open("tree_chatbot.dot", 'w') as f:
     f = tree.export_graphviz(decision_tree,
                              out_file=f,
                              max_depth = 20,
                              impurity = True,
                              feature_names = list(train.drop(['Caro??'], axis=1)),
                              class_names = ['False', 'True'],
                              rounded = True,
                              filled= True )
        
        
       
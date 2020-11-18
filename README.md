# **Projeto Programação Estruturada**

Este projeto consiste na criação de um *chatbot* para predição das chances de um domicílio do condado de King (*King County*), WA, EUA, ser mais caro ou mais barato do que o valor médio dos preços das casas dessa região. A implementação poderia ser realizada para toda a cidade, porém, o foco deste projeto será nas residências que possuem *ZIP Code* **98055**.

<br />

---

<br />

- [**Projeto Programação Estruturada**](#projeto-programação-estruturada)
  - [**Visão geral do projeto**](#visão-geral-do-projeto)
    - [**Localização de estudo**](#localização-de-estudo)
      - [**CONDADO DE KING (*KING COUNTY*), WA, EUA**](#condado-de-king-king-county-wa-eua)
      - [**RENTON, CONDADO DE KING**](#renton-condado-de-king)
      - [**ZIP CODE 98055**](#zip-code-98055)
    - [**Banco de dados das casas do condado de King, WA, EUA**](#banco-de-dados-das-casas-do-condado-de-king-wa-eua)
    - [**Biblioteca Scikit-learn em Python para criação de árvores de decisão**](#biblioteca-scikit-learn-em-python-para-criação-de-árvores-de-decisão)
    - [**Chatbot a partir de uma árvore de decisão**](#chatbot-a-partir-de-uma-árvore-de-decisão)
  - [**Descrição da implementação**](#descrição-da-implementação)
    - [**Preparação do banco de dados**](#preparação-do-banco-de-dados)
    - [**Geração da árvore de decisão**](#geração-da-árvore-de-decisão)
    - [**Implementação do chatbot**](#implementação-do-chatbot)
  - [**Como rodar o chatbot**](#como-rodar-o-chatbot)

<br />

---

<br />

## **Visão geral do projeto**

Para a criação do *chatbot*, é necessário obter uma árvore de decisão a partir de técnicas de *Machine Learning* que seja capaz de direcionar um conjunto de informações sobre uma determinada casa para uma resposta a respeito das chances da mesma ser mais cara que o valor médio da região.

No geral, podemos definir os seguintes pontos importantes para o desenvolvimento deste projeto:

- Banco de dados das casas do condado de King, WA, EUA
- Biblioteca Scikit-learn em Python para criação de árvores de decisão
- Chatbot a partir de uma árvore de decisão

<br />

### **Localização de estudo**

<br />

<div align="center">

#### **CONDADO DE KING (*KING COUNTY*), WA, EUA**
</div>

<div align="center">

| [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Map_of_Washington_highlighting_King_County.svg/5936px-Map_of_Washington_highlighting_King_County.svg.png" alt="KingCountyInWA" width="300"/>](https://en.wikipedia.org/wiki/King_County,_Washington) | [ <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Washington_in_United_States.svg/1181px-Washington_in_United_States.svg.png" alt="WAinUSA" width="300"/>](https://en.wikipedia.org/wiki/Washington_(state))  |
|:---:|:---:|
| Localização do Condado de King, WA, EUA | Localização do Estado de Washington, EUA |

</div>


O Condado de King (King County, em inglês) é um dos 39 condados do estado americano de Washington, cuja maior cidade é Seattle.

<br />

<div align="center">

#### **RENTON, CONDADO DE KING**
</div>

<div align="center">

| [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/King_County_Washington_Incorporated_and_Unincorporated_areas_Renton_Highlighted.svg/1250px-King_County_Washington_Incorporated_and_Unincorporated_areas_Renton_Highlighted.svg.png" alt="RentoninKingCounty" width="500"/>](https://en.wikipedia.org/wiki/Renton,_Washington) |
|:---:|
| Localização da cidade de Renton dentro do Condado de King, à esquerda |

</div>

Renton é uma cidade do Condado de King, Washington, e considerada subúrbio de Seattle. Situa-se a 18 km ao sudeste do centro de Seattle. Possui áreas com *ZIP Codes* de 98055 a 98059.

<br />

<div align="center">

#### **ZIP CODE 98055**
</div>

<!--

<div align="center">

| [<img src="https://images.geodatadirect.com/api/images/GetCoverageImages?Id=45898" alt="zipcode98055" width="500"/>](https://www.unitedstateszipcodes.org/98055/) |
|:---:|
| Em destaque, localização da região incorporada ao ZIP Code 98055 |

</div>

-->

<br />

### **Banco de dados das casas do condado de King, WA, EUA**

Para a construção do *chatbot*, foi utilizado um banco de dados de preços de casas vendidas entre Maio de 2014 e Maio de 2015 no Condado de King. Esses dados foram disponibilizados pelo usuário [harlfoxem](https://www.kaggle.com/harlfoxem) através da plataforma [kaggle](https://www.kaggle.com/) e estão presentes em seu repositório chamado ["House Sales in King County, USA: Predict house price using regression"](https://www.kaggle.com/harlfoxem/housesalesprediction).

<br />

### **Biblioteca Scikit-learn em Python para criação de árvores de decisão**

*Scikit-learn* é um módulo de Python que integra uma ampla gama de algoritmos de aprendizado de máquina de última geração para problemas supervisionados e não supervisionados de média escala. Este pacote se concentra em levar o aprendizado de máquina para não especialistas usando uma linguagem de alto nível de uso geral. O código-fonte, os binários e a documentação podem ser baixados em http://scikit-learn.sourceforge.net.

O módulo [sklearn.tree](https://scikit-learn.org/stable/modules/classes.html?highlight=tree#module-sklearn.tree) inclui modelos baseados em árvore de decisão para classificação e regressão.

<br />

### **Chatbot a partir de uma árvore de decisão**

O algoritmo para implementação do chatbot a partir da estrutura de uma árvore de decisão foi disponibilizado pelo **Profº Mario Alexandre Gazziro** (CECS-UFABC), mas originalmente desenvolvido pelo aluno **Vinícius dos Santos Ribeiro**.

A versão modificada para o trabalho presente encontra-se neste repositório, sob o nome de [chatbot_maker.py](https://github.com/guigasalim/ProjetoPE/blob/main/chatbot_maker.py).

<br />

---

<br />

## **Descrição da implementação**
> A descrição a seguir demonstra os passos para desenvolver uma árvore de decisão capaz de prever a informação sobre se a casa escolhida possui preço acima ou abaixo do valor médio. O uso da biblioteca **Scikit-learn** promove ligeiras variações na árvore de decisão gerada de acordo com a complexidade da mesma. O usuário não deve desprezar essa discrepância caso deseje criar uma nova árvore de decisão.
> O arquivo [arvore.csv](https://github.com/guigasalim/ProjetoPE/blob/main/arvore.csv) deve ser modificado levando em conta as alterações promovidas ao arquivo [tree_chatbot.dot](https://github.com/guigasalim/ProjetoPE/blob/main/tree_chatbot.dot).

<br />

### **Preparação do banco de dados**

No arquivo [csv_preparation.py](https://github.com/guigasalim/ProjetoPE/blob/main/csv_preparation.py), inicia-se a preparação do arquivo de entrada para a geração da árvore de decisão a partir do script a seguir:

```py
data = pd.read_csv('kc_house_data.csv', sep=',')
```
Vale lembrar que **kc_house_data.csv** possui os dados de todas as casas vendidas no Condado de King.

Após isso, os dados devem ser filtrados para o *ZIP Code* desejado (98055, neste caso) e uma nova coluna com 1s e 0s que determinam se o preço da residência está acima ou abaixo, respectivamente, do preço médio por pé quadrado, como segue abaixo: 

```py
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
```

A seguir, a base de dados é dividida em 2 arquivos:

- **'autoavaliacao.csv':** as 10 últimas casas, para serem usadas na autoavaliação do chatbot;
- **'CasasTop.csv':** os restantes das casas, para processo de construção do chatbot.

```py
# Separando as 10 últimas linhas para usar como autoavaliação ao final do desenvolvimento do chatbot
autoavaliacao = data_98055.tail(10)

# Eliminando as 10 ultimas linhas para não serem mais usadas durante a criação do chatbot
data_98055 = data_98055[:-10]

# Exportando os dados das casas para processo de construção do chatbot como 'CasasTop.csv'
data_98055.to_csv(r'CasasTop.csv', index=False)

# Exportando as 10 casas para serem usadas na autoavaliação do chatbot
autoavaliacao.to_csv(r'autoavaliacao.csv', index=False)
```

Para rodar este algoritmo, insira o seguinte comando em um terminal:

```bash
py csv_preparation.py
```

que também gerará como saída uma mensagem exibindo uma amostra das tabelas exportadas para .CSV.

Dessa forma, os dados estão prontos para as próximas etapas.

<br />

### **Geração da árvore de decisão**

> Devido à utilização de *machine learning* com a bilioteca *Scikit-learn*, a geração de árvores de decisão pode variar ligeiramente, dependendo da complexidade do *chatbot* a ser desenvolvido.
> No caso em questão, todas as execuções do arquivo **csv_preparation.py** resultarem em árvores um pouco diferentes umas das outras.
**Faça as alterações necessárias ao arquivo .DOT, caso queira construir um *chatbot* a partir de uma árvore de decisão completamente nova.**

Após um processamento inicial dos dados das vendas de casas do Condado de King, agora volta-se para o arquivo [chatbot_sklearn.py](https://github.com/guigasalim/ProjetoPE/blob/main/chatbot_sklearn.py).

Nele é carregada a tabela sem as últimas 10 linhas de casas:

```py
train = pd.read_csv('CasasTop.csv')
```

São selecionadas, então, as colunas que deseja-se manter para a construção da árvore de decisão:

```py
keep_elements = ['bedrooms', 'bathrooms', 'floors', 'waterfront',
                'view', 'condition', 'grade', 'Caro??']
train = train[keep_elements]
```

Para definir quais colunas manter para elaboração da árvore, devem ser calculados os valores *gini* para cada coluna da tabela, para assim poder obter uma noção melhor de quais são mais favoráveis.

É usada, então, a biblioteca de funções **Scikit-learn**, por intermédio do seu módulo **tree**, para criar a árvore de decisão em função da coluna **'Caro??'**:

```py
y_train = train['Caro??']
x_train = train.drop(['Caro??'], axis=1).values
decision_tree = tree.DecisionTreeClassifier(max_depth = 20)
decision_tree.fit(x_train, y_train)
```

A variável **decision_tree** possuirá todos os dados a respeito da árvore de decisão gerada. Após isso, a árvore será exportada para o formato .DOT, com nome [**tree_chatbot.dot**](https://github.com/guigasalim/ProjetoPE/blob/main/tree_chatbot.dot). 
O trecho responsável por essa exportação é:

```py
with open("tree_chatbot.dot", 'w') as f:
     f = tree.export_graphviz(decision_tree,
                              out_file=f,
                              max_depth = 20,
                              impurity = True,
                              feature_names = list(train.drop(['Caro??'], axis=1)),
                              class_names = ['False', 'True'],
                              rounded = True,
                              filled= True )
```

Com o arquivo .DOT (10 primeiras linhas abaixo) do fluxograma da árvore de decisão definido, pode-se gerar a imagem em formato .PNG resultante.

```
digraph Tree {
node [shape=box, style="filled, rounded", color="black", fontname=helvetica] ;
edge [fontname=helvetica] ;
0 [label="yr_built <= 2002.5\ngini = 0.49\nsamples = 257\nvalue = [147, 110]\nclass = False", fillcolor="#f8dfcd"] ;
1 [label="bedrooms <= 3.5\ngini = 0.5\nsamples = 222\nvalue = [114, 108]\nclass = False", fillcolor="#fef8f5"] ;
0 -> 1 [labeldistance=2.5, labelangle=45, headlabel="True"] ;
2 [label="bedrooms <= 2.5\ngini = 0.487\nsamples = 155\nvalue = [65, 90]\nclass = True", fillcolor="#c8e4f8"] ;
1 -> 2 ;
3 [label="bathrooms <= 2.125\ngini = 0.395\nsamples = 48\nvalue = [13, 35]\nclass = True", fillcolor="#83c1ef"] ;
2 -> 3 ;
...
```

| [<img src="https://github.com/guigasalim/ProjetoPE/blob/main/arvore.png?raw=true" alt="arvore-png"/>](https://github.com/guigasalim/ProjetoPE/blob/main/arvore.png) |
|:---:|
| Imagem da árvore de decisão obtida. |

<br />

### **Implementação do chatbot**

Com o arquivo 


<br />

---

<br />

## **Como rodar o chatbot**

> Para rodar o *chatbot*, bastam os arquivos **arvore.csv** e **chatbot_maker.py**.
> A árvore de decisão utilizada será a apresentada em **arvore.csv**. Para gerar uma nova árvore, verifique os procedimentos na seção [**Descrição da implementação**](#descrição-da-implementação). 

Para executar o *chatbot*, primeiramente, escolha um diretório local em seu computador. Abra o terminal e execute:

 ```bash
git clone https://github.com/guigasalim/ProjetoPE.git
cd ProjetoPE
 ```

Após isso, basta digitar o comando a seguir para iniciar o *chatbot*:

```bash
py chatbot_maker.py
```
ou
```bash
python chatbot_maker.py
```

Será exibida a seguinte mensagem:

```bash
Escolha uma das opções abaixo:
0 para sair
1 para Sim
2 para Não

Tem 2 ou menos Banheiros?
```

Será então exibida uma série de perguntas a respeito das características da casa a ser considerada. Quando o *chatbot* encontrar uma solução baseada em sua árvore de decisão (arquivo **'arvore.csv'**), exibirá uma mensagem como:

```bash
Altas Chances de Ser Caro
```

que pode ser do tipo:

- Altas Chances de Ser Barato
- Chances Medias de ser Barato
- Chances de ser o preço do Mercado
- Chances Medias de ser Caro
- Altas Chances de Ser Caro

A seguir, o *chatbot* é reiniciado, sendo possível encerrar sua execução a qualquer momento usando a opção:

```bash
0 para sair
```
# **Projeto Programação Estruturada**

Este projeto consiste na criação de um *chatbot* para predição das chances de um domicílio do condado de King (*King County*), WA, EUA, ser mais caro ou mais barato do que o valor médio dos preços das casas dessa região. A implementação poderia ser realizada para toda a cidade, porém, o foco deste projeto será nas residências que possuem *ZIP Code* **98055**.

- [**Projeto Programação Estruturada**](#projeto-programação-estruturada)
  - [**Visão geral do projeto**](#visão-geral-do-projeto)
    - [**Localização de estudo**](#localização-de-estudo)
      - [**CONDADO DE KING (*KING COUNTY*), WA, EUA**](#condado-de-king-king-county-wa-eua)
      - [**RENTON, CONDADO DE KING**](#renton-condado-de-king)
      - [**ZIP CODE 98055**](#zip-code-98055)
    - [**Banco de dados das casas do condado de King, WA, EUA**](#banco-de-dados-das-casas-do-condado-de-king-wa-eua)
    - [**Bilioteca Scikit-learn em Python para criação de árvores de decisão**](#bilioteca-scikit-learn-em-python-para-criação-de-árvores-de-decisão)
    - [**Implementação do chatbot a partir de uma árvore de decisão**](#implementação-do-chatbot-a-partir-de-uma-árvore-de-decisão)
  - [**Descrição da implementação**](#descrição-da-implementação)
  - [**Como rodar o chatbot**](#como-rodar-o-chatbot)


## **Visão geral do projeto**

Para a criação do *chatbot*, é necessário obter uma árvore de decisão a partir de técnicas de *Machine Learning* que seja capaz de direcionar um conjunto de informações sobre uma determinada casa para uma resposta a respeito das chances da mesma ser mais cara que o valor médio da região.

No geral, podemos definir os seguintes pontos importantes para o desenvolvimento deste projeto:

- Banco de dados das casas do condado de King, WA, EUA
- Bilioteca Scikit-learn em Python para criação de árvores de decisão
- Implementação do *chatbot* a partir de uma árvore de decisão

### **Localização de estudo**

#### **CONDADO DE KING (*KING COUNTY*), WA, EUA**

<center>

| [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Map_of_Washington_highlighting_King_County.svg/5936px-Map_of_Washington_highlighting_King_County.svg.png" alt="KingCountyInWA" width="300"/>](https://en.wikipedia.org/wiki/King_County,_Washington) | [ <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Washington_in_United_States.svg/1181px-Washington_in_United_States.svg.png" alt="WAinUSA" width="300"/>](https://en.wikipedia.org/wiki/Washington_(state))  |
|:---:|:---:|
| Localização do Condado de King, WA, EUA | Localização do Estado de Washington, EUA |

</center>

O Condado de King (King County, em inglês) é um dos 39 condados do estado americano de Washington, cuja maior cidade é Seattle.

#### **RENTON, CONDADO DE KING**

<center>

| [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/King_County_Washington_Incorporated_and_Unincorporated_areas_Renton_Highlighted.svg/1250px-King_County_Washington_Incorporated_and_Unincorporated_areas_Renton_Highlighted.svg.png" alt="RentoninKingCounty" width="500"/>](https://en.wikipedia.org/wiki/Renton,_Washington) |
|:---:|
| Localização da cidade de Renton dentro do Condado de King, à esquerda |

</center>

Renton é uma cidade do Condado de King, Washington, e considerada subúrbio de Seattle. Situa-se a 18 km ao sudeste do centro de Seattle. Possui áreas com *ZIP Codes* de 98055 a 98059.

#### **ZIP CODE 98055**


<center>

| [<img src="https://images.geodatadirect.com/api/images/GetCoverageImages?Id=45898" alt="zipcode98055" width="500"/>](https://www.unitedstateszipcodes.org/98055/) |
|:---:|
| Em destaque, localização da região incorporada ao ZIP Code 98055 |

</center>


### **Banco de dados das casas do condado de King, WA, EUA**

Para a construção do *chatbot*, foi utilizado um banco de dados de preços de casas vendidas entre Maio de 2014 e Maio de 2015 no Condado de King. Esses dados foram disponibilizados pelo usuário [harlfoxem](https://www.kaggle.com/harlfoxem) através da plataforma [kaggle](https://www.kaggle.com/) e estão presentes em seu repositório chamado ["House Sales in King County, USA: Predict house price using regression"](https://www.kaggle.com/harlfoxem/housesalesprediction).


### **Bilioteca Scikit-learn em Python para criação de árvores de decisão**

*Scikit-learn* é um módulo de Python que integra uma ampla gama de algoritmos de aprendizado de máquina de última geração para problemas supervisionados e não supervisionados de média escala. Este pacote se concentra em levar o aprendizado de máquina para não especialistas usando uma linguagem de alto nível de uso geral. O código-fonte, os binários e a documentação podem ser baixados em http://scikit-learn.sourceforge.net.

O módulo [sklearn.tree](https://scikit-learn.org/stable/modules/classes.html?highlight=tree#module-sklearn.tree) inclui modelos baseados em árvore de decisão para classificação e regressão.


### **Implementação do chatbot a partir de uma árvore de decisão**

O algoritmo para implementação do chatbot a partir da estrutura de uma árvore de decisão foi disponibilizado pelo **Profº Mario Alexandre Gazziro** (CECS-UFABC), mas originalmente desenvolvido pelo aluno **Vinícius dos Santos Ribeiro**.

A versão modificada para o trabalho presente encontra-se neste repositório, sob o nome de [chatbot_maker.py](https://github.com/guigasalim/ProjetoPE/blob/main/chatbot_maker.py).

## **Descrição da implementação**
> A descrição a seguir demonstra os passos para desenvolver uma árvore de decisão capaz de prever a informação sobre se a casa escolhida possui preço acima ou abaixo do valor médio. O uso da biblioteca **Scikit-learn** promove ligeiras variações na árvore de decisão gerada de acordo com a complexidade da mesma. O usuário não deve desprezar essa discrepância caso deseje criar uma nova árvore de decisão.
> O arquivo [arvore.csv](https://github.com/guigasalim/ProjetoPE/blob/main/arvore.csv) deve ser modificado levando em conta as alterações promovidas ao arquivo [tree_chatbot.dot](https://github.com/guigasalim/ProjetoPE/blob/main/tree_chatbot.dot).


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
```
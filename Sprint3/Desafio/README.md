
# Desafio

[Arquivo .ipynb do desafio](Desafio.ipynb)

## Etapa 1 - Preparando o Ambiente

Para o ambiente, importei a biblioteca Pandas e Matplotlib, conforme pedido nas instruções.

![Ambiente](../evidencias/preparando_ambiente.jpg)

Também mudei algumas configurações do Pandas para poder visualizar melhor a base de dados.

![Config Pandas](../evidencias/visulizacao_dados_pd.jpg)

## Etapa 2 - Lendo arquivo .csv e removendo as linhas duplicadas

Passei o data frame para uma variável e removi as linhas duplicadas.

![remove_dup](../evidencias/remove_dup.jpg)

Depois verifiquei outras possíveis anomalias e corrigi elas.

![ver_app_dup](../evidencias/ver_app_dup.jpg)

Percebi que existiam apps com o mesmo nome e decidi removê-los.

![drop_app_dup](../evidencias/drop_app_dup.jpg)

Procurei por outras anomalias.

![anomalia](../evidencias/anomalia1.jpg)

Percebi algumas e corrigi.

![drop_app_rating](../evidencias/drop_app_rating.jpg)

## Etapa 3 - Criando um gráfico de barras para os top 5 apps por instalação

Para essa etapa, precisei formatar a coluna "Installs" do meu data frame.

![format_install](../evidencias/format_install.jpg)

Depois passei para a construção do gráfico de barras.

![graph_barra_ver](../evidencias/graph_barra_ver.jpg)

O gráfico ficou assim:

![graph_resul](../evidencias/graph_ver.jpg)

## Etapa 4 - Criando um pie chart para as categorias

Verifiquei a existência de anomilias na coluna "Installs

![anomalia_2](../evidencias/anomalia2.jpg)

Depois de garantir que não existia nenhuma categoria duplicada, construí o pie chart.
Optei por juntar todas as categorias que tivessem menos que 3% dos apps. Essas categorias coloquei em uma tabela lateral auxiliar.

![pie_chart](../evidencias/pie_chart.jpg)

O resultado ficou assim:

![pizza_pie](../evidencias/pizza_pie.jpg)

## Etapa 5 - Mostrar o app mais caro no dataset

Tive que formatar a coluna "Price". Após a formatação, escrevi o código para obter o aplicativo mais caro do dataset:

![format_price](../evidencias/format_price.jpg)

O resultado foi esse:

![app_mais_caro](../evidencias/app_mais_caro.jpg)

## Etapa 6 - Mostrar quantos apps tem o Rating "Mature 17+"

Primeira etapa foi formatar a coluna. Após a formatação, foi hora de obter o dado da quantidade de apps com Rating "Mature 17+"

![apps_mature](../evidencias/apps_mature.jpg)

O resultado foi esse:

![app_mature](../evidencias/app_mature.jpg)

## Etapa 7 - Mostre top 10 apps por número de reviews

Primeiro passo foi formatar a coluna "Reviews" para o tipo inteiro

![format_review](../evidencias/format_reviews.jpg)

Depois, fiz a lista dos top 10 apps por número de reviews

![top10_review](../evidencias/top10_review.jpg)

O resultado foi esse:

![resul_lista_review](../evidencias/resul_lista_review.jpg)

## Etapa 8 - Criar dois cálculos, um em forma de lista e outro em valor

Para o cálculo em forma de lista, escolhi cálcular os top 10 aplicativos pagos com maior receita estimada, levando em consideração o número de reviews e o preço.

![lista_receita](../evidencias/lista_receita.jpg)

O resultado foi esse:

![lista_app_receita](../evidencias/lista_app_receita.jpg)

Depois, para cálculo de valor, escolhi mostrar a categoria com o maior número de apps

![categoria_mais_app](../evidencias/categoria_mais_app.jpg)

Esse foi o resultado:

![app_mais_categoria](../evidencias/app_mais_categoria.jpg)

## Etapa 9 - Criar dois gráficos para cálculos anteriores

Optei pelo gráfico de linhas para representar os apps com maior número de reviews

![plot_review](../evidencias/plot_review.jpg)

O gráfico ficou assim:

![linhas_resul](../evidencias/linhas_resul.jpg)

Por último, escolhi um gráfico de barras horizontais para representar os top 10 apps por receita estimada

![graph_barra_hori](../evidencias/graph_barra_hori.jpg)

O gráfico ficou assim:

![resul_graph_hor](../evidencias/resul_graph_hori.jpg)

#!/bin/bash

data=$(date +"%Y%m%d")

if [ ! -d ~/ecommerce ]
then 
	mkdir -p ~/ecommerce/vendas/backup
	cp ~/dados_de_vendas.csv ~/ecommerce
fi 
DIR_VENDAS=~/ecommerce/vendas
cp ~/ecommerce/dados_de_vendas.csv $DIR_VENDAS
cp $DIR_VENDAS/dados_de_vendas.csv $DIR_VENDAS/backup
cd $DIR_VENDAS/backup
mv dados_de_vendas.csv dados-$data.csv
mv dados-$data.csv backup-dados-$data.csv
echo "Data do relatorio: $(date +"%Y/%m/%d %H:%M")" >> relatorio-$data.txt
echo -n "Data da primeira venda: " >> relatorio-$data.txt
head -n2 backup-dados-$data.csv | tail -n1 | cut -d',' -f5 >> relatorio-$data.txt
echo -n "Data da ultima compra: " >> relatorio.txt
tail -n1 backup-dados-$data.csv | cut -d',' -f5 >> relatorio-$data.txt
echo -n "Total de produtos vendidos :" >> relatorio-$data.txt
quant_total_itens=$(awk -F, 'NR > 1 {soma += $3} END {print soma}' backup-dados-$data.csv)
echo " $quant_total_itens" >> relatorio-$data.txt
echo "Ultimas 10 vendas: " >> relatorio-$data.txt
tail backup-dados-$data.csv >> relatorio-$data.txt
echo "" >> relatorio-$data.txt
zip $DIR_VENDAS/backup/backup-dados-$data.zip backup-dados-$data.csv
rm backup-dados-$data.csv
rm ../dados_de_vendas.csv


--SELECT * para verificar se os dados foram transferidos

SELECT *
from tb_locacao2 loc

SELECT *
FROM tb_carro car

SELECT *
FROM tb_clientes cli

SELECT *
FROM tb_vendedor ven

SELECT *
FROM tb_combustivel com

-- Aqui eu vou formatar as colunas das datas da tabela 'tb_locacao2' para o formato 'YYYY-MM-DD'

UPDATE tb_locacao2 
SET dataEntrega = date(CONCAT(SUBSTR(dataEntrega, 1,4),'-',SUBSTR(dataEntrega, 5,2),'-',SUBSTR(dataEntrega, 7,2)))
UPDATE tb_locacao2
SET dataLocacao = date(CONCAT(SUBSTR(dataLocacao, 1,4),'-',SUBSTR(dataLocacao, 5,2),'-',SUBSTR(dataLocacao, 7,2)))

-- Criei 5 dimensoes para o fato locacao

CREATE VIEW dim_carro AS
SELECT 
	tc.idCarro as codigo,
	tc.classiCarro as chassi,
	tc.marcaCarro as marca,
	tc.modeloCarro as modelo,
	tc.anoCarro as ano,
	tc2.tipoCombustivel as combustivel
FROM tb_carro tc
join tb_combustivel tc2 
	on tc.idCombustivel = tc2.idCombustivel
	
CREATE VIEW dim_cliente AS
SELECT 
	idCliente as codigo,
	nomeCliente as nome,
	cidadeCliente as cidade,
	estadoCliente as estado,
	paisCliente as pais
FROM tb_clientes tc 

CREATE VIEW dim_vendedor AS
SELECT
	idVendedor as codigo,
	nomeVendedor as nome,
	sexo as sexo,
	estadoVendedor as estado
FROM tb_vendedor 

CREATE VIEW dim_data_entrega AS
SELECT DISTINCT
	dataEntrega AS data_ent,
	horaEntrega AS horario,
	strftime('%d',dataEntrega) AS dia,
	strftime('%m',dataEntrega) AS mes,
	strftime('%Y',dataEntrega) AS ano,
	strftime('%u',dataEntrega) AS diadasemana
FROM tb_locacao2 tl 

CREATE VIEW dim_data_locacao AS
SELECT DISTINCT
	dataLocacao AS data_loc,
	horaLocacao AS horario,
	strftime('%d',dataLocacao) AS dia,
	strftime('%m',dataLocacao) AS mes,
	strftime('%Y',dataLocacao) AS ano,
	strftime('%u',dataLocacao) AS diadasemana
FROM tb_locacao2 tl 

CREATE VIEW fato_locacao AS
SELECT 
	idLocacao as codigo,
	idCliente as cliente,
	idVendedor as vendedor,
	idCarro as carro,
	dataLocacao as dataLocacao,
	dataEntrega as dataEntrega,
	kmCarro as quilometragem,
	vlrDiaria as valorDiaria
FROM tb_locacao2 tl


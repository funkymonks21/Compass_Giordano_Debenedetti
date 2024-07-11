-- Verifiquei os dados da tabela, aplicando a 1FN

SELECT *
FROM tb_locacao tl 

-- Confirmei que não existe nenhum dado composto ou multivalorado.
-- Após isso, verifiquei valores redundantes nas colunas e consegui separar os atributos em outras entidades.
-- Também verifiquei a chave principal de cada tabela.

-- Aplicando a 2FN, verifiquei se não haviam chaves concatenadas.

-- Aplicando a 3FN, confirmei se não existiam depedências transitivas e alterei as entidades

CREATE TABLE tb_clientes ( 
	idCliente INT PRIMARY KEY,
	nomeCliente VARCHAR(100),
	cidadeCliente VARCHAR(40),
	estadoCliente VARCHAR (40),
	paisCliente VARCHAR (40)
)

INSERT INTO tb_clientes (idCliente,nomeCliente,cidadeCliente,estadoCliente,paisCliente)
SELECT DISTINCT idCliente,nomeCliente,cidadeCliente,estadoCliente,paisCliente
FROM tb_locacao tl
order by idCliente

CREATE TABLE tb_combustivel( 
	idCombustivel INT PRIMARY KEY,
	tipoCombustivel VARCHAR(20)
)

INSERT INTO tb_combustivel (idCombustivel, tipoCombustivel)
SELECT DISTINCT idcombustivel, tipoCombustivel
FROM tb_locacao
order by idcombustivel

CREATE TABLE tb_carro( 
	idCarro INT PRIMARY KEY,
	classiCarro VARCHAR(50),
	marcaCarro VARCHAR(80),
	modeloCarro VARCHAR(80),
	anoCarro INT,
	idCombustivel INT,
	FOREIGN KEY (idCombustivel) REFERENCES tb_combustivel(idCombustivel)
)

INSERT INTO tb_carro(idCarro,classiCarro,marcaCarro,modeloCarro,anoCarro,idCombustivel)
select DISTINCT idCarro,classiCarro,marcaCarro,modeloCarro,anoCarro,idCombustivel
from tb_locacao
order by idCarro

CREATE TABLE tb_vendedor( 
	idVendedor INT PRIMARY KEY,
	nomeVendedor VARCHAR(15),
	sexoVendedor SMALLINT,
	estadoVendedor VARCHAR(40)
)

INSERT INTO tb_vendedor(idVendedor,nomeVendedor,sexoVendedor,estadoVendedor)
SELECT DISTINCT idVendedor, nomeVendedor,sexoVendedor, estadoVendedor
from tb_locacao
order by idVendedor

CREATE TABLE tb_locacao2 (
	idLocacao INT PRIMARY KEY,
	idCliente INT,
	idCarro INT,
	idVendedor INT,
	dataLocacao DATE,
	horaLocacao TIME,
	qtdDiaria INT,
	vlrDiaria DECIMAL(18,2),
	dataEntrega DATE,
	horaEntrega TIME,
	kmCarro INT,
	FOREIGN KEY (idCliente) REFERENCES tb_clientes(idCliente)
	FOREIGN KEY (idCarro) REFERENCES tb_carro(idCarro)
	FOREIGN KEY (idVendedor) REFERENCES tb_vendedor(idVendedor)
)

INSERT INTO tb_locacao2 (idLocacao,idCliente,idCarro,idVendedor,dataLocacao,horaLocacao,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega,kmCarro)
SELECT idLocacao,idCliente,idCarro,idVendedor,dataLocacao,horaLocacao,qtdDiaria,vlrDiaria,dataEntrega,horaEntrega,kmCarro 
FROM tb_locacao tl
order by idLocacao 


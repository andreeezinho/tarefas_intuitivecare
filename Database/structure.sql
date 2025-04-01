-- demonstracoes contábeis

CREATE TABLE IF NOT EXISTS demonstracoes_contabeis (
    data DATE,
    reg_ans INT NOT NULL,
    cd_conta_contabil BIGINT NOT NULL,
    descricao TEXT,
    vl_saldo_inicial FLOAT,
    vl_saldo_final FLOAT
);

-- relatorio cadop

CREATE TABLE IF NOT EXISTS relatorio_cadop (
    registro_ans INT NOT NULL PRIMARY KEY,
    cnpj VARCHAR(15) UNIQUE NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(200),
    modalidade VARCHAR(150),
    logradouro VARCHAR(255),
    numero VARCHAR(10),
    complemento VARCHAR(200),
    bairro VARCHAR(100),
    cidade VARCHAR(150),
    uf VARCHAR(2),
    cep VARCHAR(10),
    ddd VARCHAR(2),
    telefone VARCHAR(15),
    fax VARCHAR(12),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(200),
    cargo_representante VARCHAR(150),
    regiao_de_comercializacao INT,
    data_registro_ans DATE
);

-- importar relatorio_cadop.csv
LOAD DATA INFILE 'data/Relatorio_cadop.csv'
    INTO TABLE relatorio_cadop
        FIELDS TERMINATED BY ';' 
        ENCLOSED BY '"' 
        LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


--importar demonstracoes contabeis
LOAD DATA INFILE 'data/1T2023.csv'
    INTO TABLE relatorio_cadop
        FIELDS TERMINATED BY ';' 
        ENCLOSED BY '"' 
        LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'data/1T2024.csv'
    INTO TABLE relatorio_cadop
        FIELDS TERMINATED BY ';' 
        ENCLOSED BY '"' 
        LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'data/2t2023.csv'
    INTO TABLE relatorio_cadop
        FIELDS TERMINATED BY ';' 
        ENCLOSED BY '"' 
        LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'data/2T2024.csv'
    INTO TABLE relatorio_cadop
        FIELDS TERMINATED BY ';' 
        ENCLOSED BY '"' 
        LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'data/3T2023.csv'
    INTO TABLE relatorio_cadop
        FIELDS TERMINATED BY ';' 
        ENCLOSED BY '"' 
        LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'data/3T2024.csv'
    INTO TABLE relatorio_cadop
        FIELDS TERMINATED BY ';' 
        ENCLOSED BY '"' 
        LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'data/4T2023.csv'
    INTO TABLE relatorio_cadop
        FIELDS TERMINATED BY ';' 
        ENCLOSED BY '"' 
        LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'data/4T2024.csv'
    INTO TABLE relatorio_cadop
        FIELDS TERMINATED BY ';' 
        ENCLOSED BY '"' 
        LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
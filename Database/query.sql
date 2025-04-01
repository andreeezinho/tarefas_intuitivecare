-- demonstracoes contábeis

CREATE TABLE IF NOT EXISTS `demonstracoes_contabeis` (
    data DATE,
    reg_ans INT NOT NULL,
    cd_conta_contabil BIGINT NOT NULL,
    descricao TEXT,
    vl_saldo_inicial FLOAT,
    vl_saldo_final FLOAT
)

-- relatorio cadop

CREATE TABLE IF NOT EXISTS `relatorio_cadop` (
    registro_ans INT NOT NULL PRIMARY KEY,
    cnpj VARCHAR(15) UNIQUE NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(200),
    modalidade VARCHAR(150),
    logradouro VARCHAR(255)
    logradouro VARCHAR(255),
    numero VARCHAR(10),
    complemento VARCHAR(200),
    bairro VARCHAR(100),
    cidade VARCHAR(150),
    uf VARCHAR(2),
    CEP VARCHAR(10),
    ddd VARCHAR(2),
    telefone VARCHAR(15),
    fax VARCHAR(12),
    endereco_eletronico VARCHAR(255),
    representante VARCHAR(200),
    cargo_representante VARCHAR(150),
    regiao_de_comercializacao INT,
    data_registro_ans DATE

)
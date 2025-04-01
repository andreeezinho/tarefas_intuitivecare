-- demonstracoes contábeis

CREATE TABLE IF NOT EXISTS `demonstracoes_contabeis` (
    data DATE,
    reg_ans INT NOT NULL,
    cd_conta_contabil BIGINT NOT NULL,
    descricao TEXT,
    vl_saldo_inicial FLOAT,
    vl_saldo_final FLOAT
)
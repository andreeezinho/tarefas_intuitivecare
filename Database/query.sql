-- 10 maiores despesas do trimestre
SELECT 
    contabil.reg_ans,
    relatorio.razao_social,
    contabil.descricao,
    SUM(contabil.vl_saldo_inicial) as despesa_total 
FROM demonstracoes_contabeis
    INNER JOIN relatorio_cadop
        ON contabil.reg_ans = relatorio.registro_ans
WHERE 
    descricao = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "
AND
    data >= "2024-10-01"
GROUP BY
    reg_ans
ORDER BY 
    despesa_total DESC
LIMIT 10;


-- 10 maiores despesas do ultimo ano
SELECT 
    contabil.reg_ans,
    relatorio.razao_social,
    contabil.descricao,
    SUM(contabil.vl_saldo_inicial) as despesa_total 
FROM demonstracoes_contabeis
    INNER JOIN relatorio_cadop
        ON contabil.reg_ans = relatorio.registro_ans
WHERE 
    descricao = "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR "
AND
    data >= "2024-01-01"
GROUP BY
    reg_ans
ORDER BY 
    despesa_total DESC
LIMIT 10;

# Teste de Nivelamento IntuitiveCare

Projeto para resolução de questões de um teste de nivelamento para vaga de estágio da IntuitiveCare

### T1 - Webscraping
 - Realizado acesso à um site específico para fazer o download de dois anexos .pdf e compactar os dois arquivos em .zip

Como rodar o projeto
```
cd Webscraping
py main.py
```

### T2 - Transformação de Dados
 - Código realiza a extração de um arquivo .csv, substitui linhas com "OD" e "AMB", salva os dados em uma tabela e compacta em um .zip

Como rodar o projeto
```
cd DataTransformation
py main.py
```

### T3 - Teste de Banco de Dados
 - Querys .sql de estruturação de duas tabelas, querys para importar conteúdo dos arquivos .csv. Por final, uma query analítica para responder a:

        Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS  OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
        Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

Como ver os arquivos
```
cd Database
```

### T4 - Teste de API
 - Criação de uma API com python que retorna dados de operadoras de acordo com um filtro. Criação do front-end utilizando Vue.js, onde ele faz a requisição da API e retorna o valor dela.

Como rodar o projeto

- Iniciar servidor backend
```
cd API/backend
uvicorn main:app --reload
```

- Iniciar servidor frontend
```
cd API/frontend
npm install
npm run dev
```


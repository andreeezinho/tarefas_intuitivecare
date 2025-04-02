class Model:
    registro_ans = None
    cnpj = None
    razao_social = None
    nome_fantasia = None
    modalidade = None

    def getData(data):
        model = Model()
        model.registro_ans = data.Registro_ANS
        model.cnpj = data.CNPJ
        model.razao_social = data.Razao_Social
        model.nome_fantasia = data.Nome_Fantasia
        model.modalidade = data.Modalidade
        return model
    
class Model:
    registro_ans = None
    cnpj = None
    razao_social = None
    nome_fantasia = None
    modalidade = None

    def getData(data):
        model = Model()
        model.registro_ans = data.registro_ans
        model.cnpj = data.cnpj
        model.razao_social = data.razao_social
        model.nome_fantasia = data.nome_fantasia
        model.modalidade = data.modalidade
        return model
    
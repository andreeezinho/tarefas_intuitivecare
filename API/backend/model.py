class Model:
    
    def __init__(self):
        self.razao_social = None
        self.nome_fantasia = None
        self.modalidade = None


    def getData(data):
        model = Model()
        model.razao_social = data.Razao_Social
        model.nome_fantasia = data.Nome_Fantasia
        model.modalidade = data.Modalidade
        return model
    
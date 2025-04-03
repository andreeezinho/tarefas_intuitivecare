class Controller:
    def __init__(self):
        pass

    def search(filter, data):
        if data.empty:
            return False
        
        #retornar apenas o que contem o dado do filter
        result = data[
            data["Razao_Social"].str.contains(filter, case=False, na=False)
        ]

        #retorna result como dict
        return result.to_dict(orient="records")
        
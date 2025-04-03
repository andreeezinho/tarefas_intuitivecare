class Controller:
    def __init__(self):
        pass

    def search(filter, data):
        if data.empty:
            return False
        
        result = data[
            data["Razao_Social"].str.contains(filter, case=False, na=False)
        ]

        return result.to_dict(orient="records")
        
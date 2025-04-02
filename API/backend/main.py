import os
import pandas as pd
from fastapi import FastAPI
from model import Model
class apiMain:

    app = FastAPI()

    def __init__(self):
        file = "Relatorio_cadop.csv"
        file_path = os.path.join("data", file)

        dados = pd.read_csv(file_path, sep=";", encoding="utf-8")
        teste = Model.getData(dados)
        print(teste)
if __name__ == "__main__":
    apiMain()
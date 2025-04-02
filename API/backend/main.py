import os
from fastapi import FastAPI
import pandas as pd
from controller import Controller

class apiMain:

    app = FastAPI()

    def __init__(self):
        self.file = "Relatorio_cadop.csv"
        self.file_path = os.path.join("data", file)
        self.data = pd.read_csv(file_path, sep=";", encoding="utf-8")

    @app.get("/search")
    def search(self):
        search = Controller.search(self.data)

        if search == True

if __name__ == "__main__":
    apiMain()
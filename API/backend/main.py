import os
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from controller import Controller

app = FastAPI()

# Configuração do cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

file = "Relatorio_cadop.csv"
file_path = os.path.join("data", file)

#retorna todas as linhas do csv
data = pd.read_csv(file_path, sep=";", encoding="utf-8")

#substitui null por "N/A"
data = data.fillna("N/A")

#rota das operadoras
@app.get("/search")
#método recebe parametro da api
def search(filter):
    search = Controller.search(filter, data)

    if search != False:
        return search

    return {"Erro na resposta da API"}

#rota para verificar api
@app.get("/api")
def verifyApi():
    return {"API ativa!"}

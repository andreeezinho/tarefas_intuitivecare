import os
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

data = pd.read_csv(file_path, sep=";", encoding="utf-8")
data = data.fillna("N/A")

@app.get("/search")
def search():
    search = Controller.search(data)

    if search != False:

        return search
    
    return {"Erro: API não pode respoder"}

@app.get("/api")
def verifyApi():
    return {"API ativa!"}


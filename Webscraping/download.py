import os
import requests

class downloadFiles:

    def __init__(self, file, dir_name):
        self.download(file, dir_name)

    def download(self, file, dir_name):
        #requisicao para o arquivo
        response = requests.get(file, stream=True)

        #pegar somente nome do arquivo
        file = os.path.basename(file)

        self.save(response, os.path.join(dir_name, file))

    def save(self, response, file):
        with open(file, 'wb') as f:
            #salvar arquivo com 8192 de velocidade
            for chunk in response.iter_content(8192): 
                f.write(chunk)

            print(f"Arquivo {file} baixado com sucesso!")

import os
import requests
from urllib.parse import urljoin

class downloadFiles:

    def __init__(self, file, dir_name):
        self.download(file, dir_name)

    def download(self, file, dir_name):
        response = requests.get(file, stream=True)

        file = os.path.basename(file)

        self.save(response, os.path.join(dir_name, file))

    def save(self, response, file):
        with open(file, 'wb') as f:
            for chunk in response.iter_content(4024): 
                f.write(chunk)
                
            print(f"Arquivo {file} baixado com sucesso!")

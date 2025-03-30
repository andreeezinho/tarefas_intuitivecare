import os
import requests
from urllib.parse import urljoin

class downloadFiles:

    def __init__(self, file):
        self.download(file)

    def download(self, file):
        response = requests.get(file, stream=True)
        
        if response == 200:
            self.save(response, file)

    def save(response, file):
        with open(file, 'wb') as f:
            for chunk in response.iter_content(1024): 
                f.write(chunk)
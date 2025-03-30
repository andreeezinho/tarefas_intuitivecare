import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

from download import downloadFiles
from compact import compactFiles

URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos";

class scrapeFiles:

    def __init__(self):
        os.makedirs("downloads", exist_ok=True)

    def validateLink(self, link, prefix, extension):
        link = os.path.basename(link).lower() 

        if link.startswith(prefix.lower()) and link.endswith(extension):
            return link

    def extractLinks(self, URL):
        page = requests.get(URL);
        
        soup = BeautifulSoup(page.content, 'html.parser')

        links = soup.find_all('a', href=True)

        for link in links:
            href = link.get('href', '').strip()

            if self.validateLink(href, 'Anexo', '.pdf'):
                downloadFiles(href, 'downloads')

        compactFiles('downloads')


if __name__ == '__main__':
    scraper = scrapeFiles()
    scraper.extractLinks(URL)
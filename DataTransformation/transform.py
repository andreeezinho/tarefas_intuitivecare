import os
import tabula

class transform:
    def dataInCsv(pdf_path):
        if pdf_path != None:
            tabula.convert_into(pdf_path, "Arquivo.csv", output_format="csv", pages="all", stream=True)
            print("Tabela CSV salva")
            return True
        
        return False
    
    def renameLines():
        csv_file = open("Arquivo.csv", mode="r+")
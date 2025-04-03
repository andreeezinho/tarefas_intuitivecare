import os
import tabula

class transform:
    def dataInCsv(pdf_path):
        if pdf_path != None:
            #converter pdf em arquivo csv
            tabula.convert_into(pdf_path, "Arquivo.csv", output_format="csv", pages="all", stream=True)
            print("Tabela CSV salva")
            return True
        
        return False
    
    def renameLines():
        csv_file = open("Arquivo.csv", mode="r")

        #retornar todas as linhas
        lines = csv_file.readlines()

        #substituir as linhas OD e AMB pelo desejado
        lines = [
            line.replace("OD", "Seg. Odontológica").replace("AMB", "Seg. Ambulatorial") for line in lines
        ]
        
        #"abrir" csv e substituir as linhas ajustadas
        with open("Arquivo.csv", "w") as f:
            f.writelines(lines)

        csv_file.close()

        return True
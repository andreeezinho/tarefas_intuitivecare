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
        csv_file = open("Arquivo.csv", mode="r")
        lines = csv_file.readlines()

        lines = [
            line.replace("OD", "Seg. Odontológica").replace("AMB", "Seg. Ambulatorial") for line in lines
        ]
        
        with open("Arquivo.csv", "w") as f:
            f.writelines(lines)

        csv_file.close()

        return True
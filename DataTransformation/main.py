import os

from transform import transform

class transformData:

    def __init__(self):
        pdf_file = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
        pdf_path = os.path.join('../Webscraping/downloads', pdf_file)

        self.getDataTransformed(pdf_path)

    def getDataTransformed(self, pdf_path):
        if transform.dataInCsv(pdf_path) == True:
            transform.renameLines()

        return False
        
if __name__ == '__main__':
    transformData()
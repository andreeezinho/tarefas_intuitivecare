import os
from zipfile import ZipFile, ZIP_DEFLATED

class compactFiles:

    def compact(zip_path, csv_file):
        if os.path.isfile(csv_file):
            with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zip:
                zip.write(csv_file)
                
                print("Arquivo compactado!")
                return True

        print("Arquivo não encontrado")
        return False
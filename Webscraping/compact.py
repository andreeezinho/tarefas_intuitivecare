import os
from zipfile import ZipFile, ZIP_DEFLATED

class compactFiles:

    def __init__(self, dir_name):
        self.compact(dir_name)

    def compact(self, dir_name):
        zip_dir = os.path.join('', 'Anexos.zip')

        with ZipFile(zip_dir, 'w', ZIP_DEFLATED) as zip_file:
            for name in os.listdir(dir_name):
                new_dir_name = os.path.join(dir_name, name)

                if os.path.isfile(new_dir_name):
                    zip_file.write(new_dir_name, name)
        
        print("Arquivos compactados!")
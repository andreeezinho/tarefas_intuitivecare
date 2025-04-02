import os
from model import Model

class Controller:
    def __init__(self):
        pass

    def search(self, data):
        if data.empty:
            return False
        
        data = Model.getData(data)

        return data
        
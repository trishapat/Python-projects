import json


class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def load_data_from_file(self):
        with open(self.filename) as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

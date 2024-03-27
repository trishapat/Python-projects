import csv

class FileHandler:
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.matrix = self.load_data_from_input_file()

    def load_data_from_input_file(self):
        temp_matrix = []
        with open(self.input_file) as file:
            data = csv.reader(file)
            for line in data:
                temp_line = []
                for something in line:
                    temp_line.append(something)
                temp_matrix.append(temp_line)
        return temp_matrix

    def save_data_to_output_file(self):
        with open(self.output_file, mode="w") as file:
            writer = csv.writer(file)
            for line in self.matrix:
                writer.writerow(line)

    def transform(self):
        for transformation in self.changes:
            transformation_list = transformation.split(",")
            column = int(transformation_list[0])
            row = int(transformation_list[1])
            value = transformation_list[2]
            self.matrix[row][column] = value

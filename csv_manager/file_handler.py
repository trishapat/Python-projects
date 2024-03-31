import csv
import sys

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
                element_of_the_line = line[0]
                temp_line = element_of_the_line.split(';')
                temp_matrix.append(temp_line)
        return temp_matrix

    def save_data_to_output_file(self):
        with open(self.output_file, mode="w", newline='') as file:
            writer = csv.writer(file)
            for line in self.matrix:
                writer.writerow(line)

    def transform(self):
        for transformation in self.changes:
            transformation_list = transformation.split(",")
            if len(transformation_list) != 3:
                print(f"Change '{transformation}' is not in the format 'x,y,value'. Try again.")
                sys.exit(1)
            row = int(transformation_list[0])
            column = int(transformation_list[1])
            value = transformation_list[2]
            if not (0 <= row < len(self.matrix) and 0 <= column < len(self.matrix[0])):
                print(f"Coordinates '{row},{column}' out of bounds. Try again.")
                sys.exit(1)
            self.matrix[row][column] = value

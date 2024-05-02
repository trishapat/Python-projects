from abc import ABC, abstractmethod
import csv
import json
import pickle
import sys


class FileHandler(ABC):
    def __init__(self, input_file, output_file, changes):
        self.input_file = input_file
        self.output_file = output_file
        self.changes = changes
        self.data = self.load_data_from_input_file()

    @abstractmethod
    def load_data_from_input_file(self):
        pass

    @abstractmethod
    def save_data_to_output_file(self):
        pass

    @abstractmethod
    def apply_changes(self):
        pass


class CSVFileHandler(FileHandler):

    def load_data_from_input_file(self):
        temporary_data = []
        with open(self.input_file) as file:
            data = csv.reader(file)
            for line in data:
                element_of_the_line = line[0]
                temp_line = element_of_the_line.split(';')
                temporary_data.append(temp_line)
        return temporary_data

    def save_data_to_output_file(self):
        with open(self.output_file, mode="w", newline='') as file:
            writer = csv.writer(file)
            for line in self.data:
                writer.writerow(line)

    def apply_changes(self):
        for transformation in self.changes:
            transformation_list = transformation.split(",")
            if len(transformation_list) != 3:
                print(f"Change '{transformation}' is not in the format 'x,y,value'. Try again.")
                sys.exit(1)
            row = int(transformation_list[0])
            column = int(transformation_list[1])
            value = transformation_list[2]
            if not (0 <= row < len(self.data) and 0 <= column < len(self.data[0])):
                print(f"Coordinates '{row},{column}' out of bounds. Try again.")
                sys.exit(1)
            self.data[row][column] = value


class PickleFileHandler(FileHandler):
    def load_data_from_input_file(self):
        with open(self.input_file, mode="rb") as file:
            self.data = pickle.load(file)

    def save_data_to_output_file(self):
        with open(self.output_file, mode="wb") as file:
            pickle.dump(self.data, file)

    def apply_changes(self):
        for change in self.changes:
            y_position, x_position, value = change.split(",")
            self.data[int(y_position)][int(x_position)] = value


class TXTFileHandler(FileHandler):
    def load_data_from_input_file(self):
        temporary_data = []
        with open(self.input_file) as file:
            for line in file:
                temporary_data.append(line.strip().split(","))
            self.data = temporary_data
        return temporary_data

    def save_data_to_output_file(self):
        with open(self.output_file, mode="w") as file:
            for line in self.data:
                file.write(",".join(line) + "\n")

    def apply_changes(self):
        for change in self.changes:
            y_position, x_position, value = change.split(",")
            self.data[int(y_position)][int(x_position)] = value


class JsonFileHandler(FileHandler):
    def load_data_from_input_file(self):
        with open(self.input_file, 'r') as file:
            self.data = json.load(file)

    def save_data_to_output_file(self):
        with open(self.output_file, 'w') as file:
            json.dump(self.data, file)

    def apply_changes(self):
        for change in self.changes:
            change_dict = json.loads(change)
            for key, value in change_dict.items():
                self.data[key] = value

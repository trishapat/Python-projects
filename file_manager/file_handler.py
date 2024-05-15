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
    def save_data_to_output_file(self, data):
        pass

    def apply_changes(self, data, changes):
        for transformation in changes:
            transformation_list = transformation.split(",")
            if len(transformation_list) != 3:
                print(f"Change '{transformation}' is not in the format 'x,y,value'. Try again.")
                sys.exit(1)
            row = int(transformation_list[0])
            column = int(transformation_list[1])
            value = transformation_list[2]
            if not (0 <= row < len(data) and 0 <= column < len(data[0])):
                print(f"Coordinates '{row},{column}' out of bounds. Try again.")
                sys.exit(1)
            data[row][column] = value
        return data


class CSVFileHandler(FileHandler):

    def load_data_from_input_file(self):
        with open(self.input_file) as file:
            data = csv.reader(file)
            return list(data)

    def save_data_to_output_file(self, data):
        with open(self.output_file, mode="w", newline='') as file:
            writer = csv.writer(file)
            for line in data:
                writer.writerow(line)


class PickleFileHandler(FileHandler):  # don't use (;
    def load_data_from_input_file(self):
        with open(self.input_file, mode="rb") as file:
            self.data = pickle.load(file)

    def save_data_to_output_file(self,  data):
        with open(self.output_file, mode="wb") as file:
            pickle.dump(data, file)


class TXTFileHandler(FileHandler):
    def load_data_from_input_file(self):
        temporary_data = []
        with open(self.input_file) as file:
            for line in file:
                line_values = line.strip().split(",")
                temporary_data.append(line_values)
            self.data = temporary_data
        return temporary_data

    def save_data_to_output_file(self, data):
        with open(self.output_file, mode="w") as file:
            for line in data:
                line = [str(element) for element in line]
                file.write(",".join(line) + "\n")


class JsonFileHandler(FileHandler):
    def load_data_from_input_file(self):
        with open(self.input_file, 'r') as file:
            if self.input_file.endswith(".json"):
                return json.load(file)
            else:
                return self.convert()

    def convert(self):
        with open(self.input_file) as file:
            data = csv.reader(file)
            return list(data)

    def save_data_to_output_file(self, data):
        with open(self.output_file, 'w') as file:
            json.dump(data, file)

'''Write a program that reads the input CSV file, then modifies it and displays
its contents in the terminal, and finally writes it to the selected location.

Run the program through the terminal:
python reader.py <input_file> <output_file> <change_1> <change_2> ... <change_n>

<input_file> - the name of the file to be read, e.g. in.csv
<file_out> - the name of the file to which the contents are to be written, e.g. out.csv
<change_x> - Change in the form "x,y,value". - x (column) and y (row) are the
coordinates counted from 0, while "value" is the change to go to the specified location.'''

import sys
from file_handler import FileHandler

arguments = sys.argv
print(arguments)
def load_system_arguments():
    return sys.argv[1], sys.argv[2], sys.argv[3:]

input_file, output_file, changes = load_system_arguments()

file_handler = FileHandler(input_file, output_file, changes)

file_handler.transform()

file_handler.save_data_to_output_file()

print(input_file)
print(output_file)
print(changes)

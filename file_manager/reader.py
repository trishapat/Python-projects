import sys
import os.path
from file_handler import CSVFileHandler, JsonFileHandler, TXTFileHandler, PickleFileHandler


def load_system_arguments():
    args = sys.argv[1:]
    if len(args) < 2:
        print("Enter: python reader.py <input_file> <output_file> [<change_1> <change_2> ... <change_n>]")
        sys.exit(1)
    input_file, output_file = args[0], args[1]
    changes = args[2:]
    return input_file, output_file, changes


def main():
    input_file, output_file, changes = load_system_arguments()
    if not os.path.isfile(input_file):
        print(f"Input file '{input_file}' does not exist.")
        sys.exit(1)

    if input_file.endswith(".txt"):
        input_file_handler = TXTFileHandler(input_file, output_file, changes)
    elif input_file.endswith(".pkl"):
        input_file_handler = PickleFileHandler(input_file, output_file, changes)
    elif input_file.endswith(".csv"):
        input_file_handler = CSVFileHandler(input_file, output_file, changes)
    elif input_file.endswith(".json"):
        input_file_handler = JsonFileHandler(input_file, output_file, changes)
    else:
        print("Unsupported file format.")

    if output_file.endswith(".txt"):
        output_file_handler = TXTFileHandler(input_file, output_file, changes)
    elif output_file.endswith(".pkl"):
        output_file_handler = PickleFileHandler(input_file, output_file, changes)
    elif output_file.endswith(".csv"):
        output_file_handler = CSVFileHandler(input_file, output_file, changes)
    elif output_file.endswith(".json"):
        output_file_handler = JsonFileHandler(input_file, output_file, changes)
    else:
        print("Unsupported file format.")

    input_file_handler.apply_changes()
    output_file_handler.save_data_to_output_file()
    print(input_file)
    print(output_file)
    print(changes)


main()

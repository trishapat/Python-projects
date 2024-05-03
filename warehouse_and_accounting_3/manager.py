from file_handler import FileHandler


class Manager:
    def __init__(self, path_history="history.json", path_balance_and_warehouse="balance_and_warehouse.json"):
        self.file_handler = FileHandler(path_history, path_balance_and_warehouse)
        self.balance, self.warehouse = self.file_handler.data_get_balance_and_warehouse()
        self.operations = self.file_handler.data_get_history()
        self.actions = {}

    def assign(self, name):
        def decorate(cb):
            self.actions[name] = cb
        return decorate

    def execute(self, name):
        if name not in self.actions:
            print("Action not defined")
        else:
            self.actions[name](self)

    def data_append_to_history(self, operation):
        self.operations.append(operation)
        self.file_handler.data_append_to_history(operation)


manager = Manager()

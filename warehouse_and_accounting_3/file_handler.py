import json


class FileHandler:
    def __init__(self, path_history, path_balance_and_warehouse):
        self.path_history = path_history
        self.path_balance_and_warehouse = path_balance_and_warehouse

    def data_get_balance_and_warehouse(self):
        with open(self.path_balance_and_warehouse) as file:
            data = json.loads(file.read())
            data.get("balance")
            print((data.get("balance"), data.get("warehouse")))
            return (data.get("balance"), data.get("warehouse"))

    def data_get_history(self):
        with open(self.path_history) as file:
            data = json.loads(file.read())
            return data

    def data_save_balance_and_warehouse(self, balance, warehouse):
        with open(self.path_balance_and_warehouse, 'w') as file:
            file.write(json.dumps({
                "balance": balance,
                "warehouse": warehouse
            }))

    def data_append_to_history(self, operation):
        history = self.data_get_history()
        history.append(operation)
        with open(self.path_history, 'w') as file:
            file.write(json.dumps(history))

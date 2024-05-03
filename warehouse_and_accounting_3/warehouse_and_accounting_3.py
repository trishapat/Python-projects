from manager import Manager

manager = Manager()


@manager.assign("withdraw_deposit")
def withdraw_deposit_action(manager):
    withdraw_deposit = int(input("Provide the amount you want to withdraw or deposit: "))
    operation_type = int(input("Choose option:\n1. Withdraw\n2. Deposit\n"))
    if operation_type == 1:
        if manager.balance >= withdraw_deposit:
            manager.balance -= withdraw_deposit
            manager.operations.append(f"You have withdrawn {withdraw_deposit} EUR")
            manager.data_append_to_history(f"You have withdrawn {withdraw_deposit} EUR")
            print(f"You have withdrawn {withdraw_deposit} EUR")
        else:
            print(f"You can't withdraw. Your balance is: {manager.balance} ")
    elif operation_type == 2:
        manager.balance += withdraw_deposit
        manager.operations.append(f"You have deposited {withdraw_deposit} EUR")
        manager.data_append_to_history(f"You have deposited {withdraw_deposit} EUR")
        print(f"You have deposited {withdraw_deposit} EUR")
    else:
        print("Choose correct option")


@manager.assign("sell")
def sell_action(manager):
    name = input("Enter product's name: ")
    amount = int(input("How much do you want to sell? "))
    product_found = False
    if amount < 0:
        print("You can't choose values below 0")
    else:
        for product in manager.warehouse:
            if product.get("name") == name:
                product_found = True
                if product.get("quantity") >= amount:
                    product["quantity"] -= amount
                    manager.balance += amount * product["price"]
                    print("You have sold a product.")
                    manager.operations.append(f"You have sold {name} in: {amount} quantity")
                    manager.data_append_to_history(f"You have sold {name} in: {amount} quantity")
                else:
                    print(f"We are sorry. Product in stock: {product['quantity']} ")
    if not product_found:
        print("We are sorry. We don't have such a product in our assortment.")


@manager.assign("buy")
def buy_action(manager):
    name = input("Enter product's name: ")
    price = float(input("Enter product's price: "))
    quantity = int(input("Enter the quantity of ordered products: "))
    if price < 0 or quantity < 0:
        print("You can't choose values below 0")
    else:
        if manager.balance >= price * quantity:
            manager.warehouse.append({
                "name": name,
                "price": price,
                "quantity": quantity
            })
            manager.balance = manager.balance - (price * quantity)
            manager.operations.append(f"You have bought {name} in {quantity} quantity for {price} EUR each")
            manager.data_append_to_history(f"You have bought {name} in {quantity} quantity for {price} EUR each")
            print(f"You have bought {name} in {quantity} quantity for {price} EUR each")
        else:
            print(f"We are sorry, but you can't buy these items. Your balance is: {manager.balance}")


@manager.assign("show_balance")
def show_balance_action(manager):
    print(f"Your balance is: {manager.balance} EUR")


@manager.assign("list_products")
def list_products_action(manager):
    print(manager.warehouse)


@manager.assign("warehouse")
def warehouse_action(manager):
    name = input("Enter product's name: ")
    product_found = False
    for product in manager.warehouse:
        if product.get("name") == name:
            product_found = True
            print("Product details:")
            print(f"Name: {product['name']}")
            print(f"Price: {product['price']} EUR")
            print(f"Quantity in stock: {product['quantity']}")
    if not product_found:
        print("Product not found in the warehouse.")


@manager.assign("overview")
def overview_action(manager):
    if not manager.operations:
        print("No operations to show.")
    else:
        start_input = input("Enter the initial range (leave empty to start from the beginning): ")
        finish_input = input("Enter the final range (leave empty to end at the last index): ")
        start = int(start_input) if start_input else 0
        finish = int(finish_input) if finish_input else len(manager.operations)
        invalid_input = False
        try:
            if start < 0 or finish > len(manager.operations) or start >= finish:
                invalid_input = True
                print("Invalid range. Please enter valid indexes.")
            else:
                for index, op in enumerate(manager.operations[start:finish], start=start):
                    print(f"{index}: {op}")
        except ValueError:
            invalid_input = True
            print("Invalid input. Please enter valid indexes.")
        if invalid_input:
            print("Valid range: ")
            for index in range(len(manager.operations)):
                print(index)


@manager.assign("end")
def end_action(manager):
    manager.data_save_balance_and_warehouse()


while True:
    operation = input(
        f"Select an option:\n1. Withdraw or deposit\n2. Sell\n3. Buy\n4. Show account balance\n5. List out the products"
        f"\n6. Warehouse\n7. Overview\n8. End\n"
    )

    if operation == "1":
        manager.execute("withdraw_deposit")
    elif operation == "2":
        manager.execute("sell")
    elif operation == "3":
        manager.execute("buy")
    elif operation == "4":
        manager.execute("show_balance")
    elif operation == "5":
        manager.execute("list_products")
    elif operation == "6":
        manager.execute("warehouse")
    elif operation == "7":
        manager.execute("overview")
    elif operation == "8":
        break

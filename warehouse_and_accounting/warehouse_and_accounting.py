'''Napisz program, który będzie rejestrował operacje na koncie firmy i stan magazynu.

Program po uruchomieniu wyświetla informację o dostępnych komendach:

saldo
 sprzedaż
zakup
konto
lista
magazyn
przegląd
koniec

Po wprowadzeniu odpowiedniej komendy, aplikacja zachowuje się w unikalny sposób dla każdej z nich:

saldo - Program pobiera kwotę do dodania lub odjęcia z konta.
sprzedaż - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt musi znajdować się w magazynie. Obliczenia respektuje względem konta i magazynu (np. produkt "rower" o cenie 100 i jednej sztuce spowoduje odjęcie z magazynu produktu "rower" oraz dodanie do konta kwoty 100).
zakup - Program pobiera nazwę produktu, cenę oraz liczbę sztuk. Produkt zostaje dodany do magazynu, jeśli go nie było. Obliczenia są wykonane odwrotnie do komendy "sprzedaz". Saldo konta po zakończeniu operacji „zakup” nie może być ujemne.
konto - Program wyświetla stan konta.
lista - Program wyświetla całkowity stan magazynu wraz z cenami produktów i ich ilością.
magazyn - Program wyświetla stan magazynu dla konkretnego produktu. Należy podać jego nazwę.
przegląd - Program pobiera dwie zmienne „od” i „do”, na ich podstawie wyświetla wszystkie wprowadzone akcje zapisane pod indeksami od „od” do „do”. Jeżeli użytkownik podał pustą wartość „od” lub „do”, program powinien wypisać przegląd od początku lub/i do końca. Jeżeli użytkownik podał zmienne spoza zakresu, program powinien o tym poinformować i wyświetlić liczbę zapisanych komend (żeby pozwolić użytkownikowi wybrać odpowiedni zakres).
koniec - Aplikacja kończy działanie.

Dodatkowe wymagania:

Aplikacja od uruchomienia działa tak długo, aż podamy komendę "koniec".
Komendy saldo, sprzedaż i zakup są zapamiętywane przez program, aby móc użyć komendy "przeglad".
Po wykonaniu dowolnej komendy (np. "saldo") aplikacja ponownie wyświetla informację o dostępnych komendach, a także prosi o wprowadzenie jednej z nich.
Zadbaj o błędy, które mogą się pojawić w trakcie wykonywania operacji (np. przy komendzie "zakup" jeśli dla produktu podamy ujemną kwotę, aplikacja powinna wyświetlić informację o niemożności wykonania operacji i jej nie wykonać). Zadbaj też o prawidłowe typy danych.'''

# Write a programme to record the company's account and warehouse operations.

account_balance = 5000
warehouse = [
    {
        "name": "chocolate",
        "price": 3.50,
        "quantity": 76
    },
    {
        "name": "candy",
        "price": 4,
        "quantity": 7
    }
]

operations = []
end_programme = False
print("Welcome to Sweet Dream")
while not end_programme:
    operation = input(f"Select an option:\n1. Deposit or withdraw\n2. Sell\n3. Buy"
                      f"\n4. Show account balance\n5. List out the products\n"
                      f"6. Warehouse\n7. Overview\n8. End\n")

    if operation == "1":
        withdraw_deposit = int(input("Provide the amount you want to withdraw or deposit: "))
        type = int(input("Choose option:\n1. withdraw\n2. deposit\n"))
        if type == 1:
            if account_balance >= withdraw_deposit:
                account_balance -= withdraw_deposit
                operations.append(f"You have withdrawn {withdraw_deposit} EUR")
                print(f"You have withdrawn {withdraw_deposit} EUR")
            else:
                print(f"You can't withdraw. Your balance is: {account_balance} ")
        elif type == 2:
            account_balance += withdraw_deposit
            operations.append(f"You have deposited {withdraw_deposit} EUR")
            print(f"You have deposited {withdraw_deposit} EUR")
        else:
            print("Choose correct option")

    if operation == "2":
        name = input("Enter product's name: ")
        amount = int(input("How much do you want to sell? "))
        product_found = False
        if amount < 0:
            print("You can't choose values below 0")
        else:
            for product in warehouse:
                if product.get("name") == name:
                    product_found = True
                    if product.get("quantity") >= amount:
                        product_sold = True
                        product["quantity"] -= amount
                        account_balance += amount * product["price"]
                        print("You have sold a product.")
                        operations.append(f"You have sold {name} in: {amount} quantity")
                    else:
                        print(f"We are sorry. Product in stock: {product["quantity"]} ")
                        product_sold = False
            if not product_found:
                print("We are sorry. We don't have such a product in our assortment.")

    if operation == "3":
        name = input("Enter product's name: ")
        price = float(input("Enter product's price: "))
        quantity = int(input("Enter the quantity of ordered products: "))
        if price < 0 or quantity < 0:
            print("You can't choose values below 0")
        else:
            if account_balance >= price * quantity:
                warehouse.append({
                    "name": name,
                    "price": price,
                    "quantity": quantity
                })
                account_balance = account_balance - (price * quantity)
                operations.append(f"You have bought {name} in {quantity} quantity for {price} EUR each")
                print(f"You have bought {name} in {quantity} quantity for {price} EUR each")
            else:
                print(f"We are sorry, but you can't buy these items. "
                      f"Your balance is: {account_balance}")

    if operation == "4":
        print(f"Your balance is: {account_balance} EUR")

    if operation == "5":
        print(warehouse)

    if operation == "6":
        name = input("Enter product's name: ")
        product_found = False
        for product in warehouse:
            if product.get("name") == name:
                product_found = True
                print("Product details:")
                print(f"Name: {product['name']}")
                print(f"Price: {product['price']} EUR")
                print(f"Quantity in stock: {product['quantity']}")
        if not product_found:
            print("Product not found in the warehouse.")

    if operation == "7":
        if not operations:
            print("No operations to show.")
        else:
            start_input = input("Enter the initial range (leave empty to start from the beginning): ")
            finish_input = input("Enter the final range (leave empty to end at the last index): ")
            start = int(start_input) if start_input else 0
            finish = int(finish_input) if finish_input else len(operations)
            invalid_input = False
            try:
                if start < 0 or finish > len(operations) or start >= finish:
                    invalid_input = True
                    print("Invalid range. Please enter valid indexes.")
                else:
                    for index, op in enumerate(operations[start:finish], start=start):
                        print(f"{index}: {op}")
            except ValueError:
                invalid_input = True
                print("Invalid input. Please enter valid indexes.")
            if invalid_input:
                print("Valid range: ")
                for index in range(len(operations)):
                    print(index)

    if operation == "8":
        end_programme = True

from flask import Flask, render_template, request, redirect, url_for, flash
from file_handler import FileHandler
from decimal import Decimal

app = Flask(__name__)
app.secret_key = 'firstsecond'

operation_file_handler = FileHandler(
    path_history="history.json",
    path_balance_and_warehouse="balance_and_warehouse.json"
)


@app.route('/')
def index():
    balance, warehouse = operation_file_handler.data_get_balance_and_warehouse()
    return render_template('index.html', balance=balance, warehouse=warehouse)


@app.route('/purchase', methods=['POST'])
def purchase():
    name = request.form['name']
    price = Decimal(request.form['price'])
    quantity = Decimal(request.form['quantity'])

    balance, warehouse = operation_file_handler.data_get_balance_and_warehouse()

    if price < 0 or quantity < 0:
        flash("You can't choose values below 0")
    elif balance >= price * quantity:
        for product in warehouse:
            if product['name'] == name:
                product['quantity'] += quantity
                break
        else:
            warehouse.append({"name": name, "price": price, "quantity": quantity})

        balance -= price * quantity
        operation_file_handler.data_save_balance_and_warehouse(balance, warehouse)
        operation_file_handler.data_append_to_history(
            f"You have bought {name} in {quantity} quantity for {price} EUR each")
        flash(f"You have bought {name} in {quantity} quantity for {price} EUR each")
    else:
        flash(f"Insufficient balance to purchase {quantity} of {name}")

    return redirect(url_for('index'))


@app.route('/sale', methods=['POST'])
def sale():
    name = request.form['name']
    quantity = Decimal(request.form['quantity'])

    balance, warehouse = operation_file_handler.data_get_balance_and_warehouse()

    for product in warehouse:
        if product['name'] == name:
            if product['quantity'] >= quantity:
                product['quantity'] -= quantity
                balance += quantity * Decimal(product['price'])
                operation_file_handler.data_save_balance_and_warehouse(balance, warehouse)
                operation_file_handler.data_append_to_history(f"You have sold {name} in {quantity} quantity")
                flash(f"You have sold {name} in {quantity} quantity")
            else:
                flash(f"Not enough stock for {name}. Available quantity: {product['quantity']}")
            break
    else:
        flash(f"Product {name} not found in warehouse")

    return redirect(url_for('index'))


@app.route('/adjust_balance', methods=['POST'])
def adjust_balance():
    value = Decimal(request.form['value'])

    balance, warehouse = operation_file_handler.data_get_balance_and_warehouse()
    balance += value
    operation_file_handler.data_save_balance_and_warehouse(balance, warehouse)

    if value >= 0:
        operation_file_handler.data_append_to_history(f"You have deposited {value} EUR")
        flash(f"You have deposited {value} EUR")
    else:
        operation_file_handler.data_append_to_history(f"You have withdrawn {abs(value)} EUR")
        flash(f"You have withdrawn {abs(value)} EUR")

    return redirect(url_for('index'))


@app.route('/history/')
@app.route('/history/<int:start>/<int:end>')
def history(start=None, end=None):
    operations = operation_file_handler.data_get_history()

    if start is None or end is None:
        return render_template('history.html', operations=enumerate(operations))

    if start < 0 or end > len(operations) or start >= end:
        flash("Invalid range. Please enter valid indexes.")
        return render_template('history.html', operations=enumerate(operations), valid_range=range(len(operations)))

    return render_template('history.html', operations=enumerate(operations[start:end], start=start))


if __name__ == '__main__':
    app.run(debug=True)

cart = {}

def add_items(name, price):
    global cart
    price = int(price)
    if name in cart:
        cart[name] += price
    else:
        cart[name] = price
    return f"Added {name} of price {price}"


def view_items():
    global cart
    if not cart:
        return "Your cart is empty."
    for item, price in cart.items():
        print(f"{item} - {price}")
    return "End of cart items."


def calculate_total():
    total_price = 0
    for price in cart.values():
        total_price += price
    return f"Total price is {total_price}"


def exit_program():
    print("Exiting the program. Thank you for shopping!")
    exit()


print(add_items('Bat', '477'))
print(add_items('Dress', '4400'))
print(view_items())
print(calculate_total())
exit_program()

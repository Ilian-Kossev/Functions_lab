def calculate(product, quantity):
    if product == "coffee":
        return quantity * 1.5
    elif product == "coke":
        return quantity * 1.4
    elif product == "water":
        return quantity
    elif product == "snacks":
        return quantity * 2


product_name = input()
quantity_value = int(input())
result = calculate(product_name, quantity_value)
print(f'{result:.2f}')
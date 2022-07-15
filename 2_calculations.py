def calculate(oper, num_1, num_2):
    if oper == "multiply":
        return num_1 * num_2
    elif oper == "divide":
        return num_1 // num_2
    elif oper == "add":
        return num_1 + num_2
    elif oper == "subtract":
        return num_1 - num_2


operator = input()
number_1 = int(input())
number_2 = int(input())
print(calculate(operator, number_1, number_2))
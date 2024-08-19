import os

def clear ():
    os.system('cls')

def calculate (number1, number2, sign):
    if sign == "+":
        return number1 + number2
    elif sign == "-":
        return number1 - number2
    elif sign == "*":
        return number1 * number2
    elif sign == "/":
        return number1 / number2

number1 = float(input())
sign = input(f"{number1} (+, -, *, /) ")
clear()
input2 = input(f"{number1} {sign} ")

while input2 != "q":
    number2 = float(input2)
    result = calculate(number1, number2, sign)
    print(f"= {result}")

    print("\nKeep calculating. Press q to quit\n")
    number1 = result
    sign = input(f"{number1} (+, -, *, /) ").lower()

    if sign =="q":
        break
    else:
        clear()
        input2 = input(f"{number1} {sign} ").lower()

os.system('exit')
from typing import Union


def calculator(num1: Union[float, int], num2: Union[float, int], operator: str):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

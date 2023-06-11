from typing import Union

def add(nums: list) -> float:
    return sum(nums)
    
def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> Union[float, str]:
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero not allowed." 

def just_because():
    print("bet you weren't expecting this turn of events!")
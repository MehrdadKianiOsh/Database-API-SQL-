import math
import exerciseWithRE as fct

while True:
    try:
        value=input("Please enter a float value: ")
        if fct.isFloat(value):
            value=float(value)
            print(f"the cosine of {value} is {math.cos(value)} ")
            break
        else:
            print(f"{value} is not a valid Float")
    except Exception as ex:
        print(f"Invalid input: {ex}")
from rich import print
from decimal import Decimal

if __name__ == "__main__":
    print("input two float numbers")
    num1 = Decimal(input("1: "))
    num2 = Decimal(input("2: "))

    print(f"float: {float(num1)/float(num2)}")
    print(f"decimal: {Decimal(num1)/Decimal(num2)}")

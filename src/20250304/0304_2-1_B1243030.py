from rich import print


def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for digit in reversed(binary):
        decimal += int(digit) * (2**power)
        power += 1
    return decimal


if __name__ == "__main__":
    num1 = float(input("Enter a interger: "))
    print(num1)

    num2 = binary_to_decimal(input("input a binary: "))
    print(num2)

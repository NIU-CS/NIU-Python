from rich import print
from decimal import Decimal


def different_from_digit(num1, num2):
    num1_str = str(num1).split(".")[1]
    num2_str = str(num2).split(".")[1]
    min_len = min(len(num1_str), len(num2_str))
    for i in range(min_len):
        if num1_str[i] != num2_str[i]:
            return i
    return min_len


if __name__ == "__main__":
    print("input two float numbers")
    num_1 = Decimal(input("1: "))
    num_2 = Decimal(input("2: "))
    ans_1 = float(num_1) / float(num_2)
    ans_2 = Decimal(num_1) / Decimal(num_2)

    print(f"float:   {ans_1}")
    print(f"decimal: {ans_2}")
    print(f"從小數點後 {different_from_digit(ans_1, ans_2)} 位開始不同")

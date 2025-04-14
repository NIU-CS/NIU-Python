from rich import print


def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


def month_season(month):
    if month in [1, 2, 3]:
        return "Winter"
    elif month in [4, 5, 6]:
        return "Spring"
    elif month in [7, 8, 9]:
        return "Summer"
    else:
        return "Autumn"


def month_fruits(month):
    if month in [1, 2, 3]:
        return ["Apple", "Banana", "Orange"]
    elif month in [4, 5, 6]:
        return ["Strawberry", "Blueberry", "Raspberry"]
    elif month in [7, 8, 9]:
        return ["Watermelon", "Cantaloupe", "Pineapple"]
    else:
        return ["Grape", "Peach", "Pear"]


def fruits_month(fruit):
    match fruit:
        case "Apple":
            return [1, 2, 3]
        case "Banana":
            return [1, 2, 3]
        case "Orange":
            return [1, 2, 3]
        case "Strawberry":
            return [4, 5, 6]
        case "Blueberry":
            return [4, 5, 6]
        case "Raspberry":
            return [4, 5, 6]
        case "Watermelon":
            return [7, 8, 9]
        case "Cantaloupe":
            return [7, 8, 9]
        case "Pineapple":
            return [7, 8, 9]
        case "Grape":
            return [10, 11, 12]
        case "Peach":
            return [10, 11, 12]
        case "Pear":
            return [10, 11, 12]
        case _:
            return []


if __name__ == "__main__":
    month = int(input("輸入月份："))
    print(f"月份 {month} 的當季水果有：")
    print(month_fruits(month))
    fruit = input("輸入水果名稱：")
    print(f"水果 {fruit} 的月份有：")
    print(fruits_month(fruit))

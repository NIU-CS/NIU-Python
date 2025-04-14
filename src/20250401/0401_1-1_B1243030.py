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


if __name__ == "__main__":
    month = int(input("輸入月份："))
    print(f"月份 {month} 的天數是 {days_in_month(2025, month)}")
    print(f"月份 {month} 的季節是 {month_season(month)}")

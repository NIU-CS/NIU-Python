from rich import print


# 閏年
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def is_valid_year(year):
    return year >= 1


if __name__ == "__main__":
    print("輸入年份：")
    year = int(input())
    while not is_valid_year(year):
        year = int(input())
    print(f"{year} 年{'是' if is_leap_year(year) else '不是'}閏年")

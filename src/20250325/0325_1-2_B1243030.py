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
    print(f"{year} 年的二月有 {29 if is_leap_year(year) else 28} 天")

    print(
        "需要有閏年的原因是因為地球繞太陽公轉一周的時間約為 365.2422 天，而一年只有 365 天，因此每四年增加一天，即閏年。"
    )
    print("有了閏年，我們可以更準確地計算日期和時間，避免日曆上的偏移。")

from rich import print

if __name__ == "__main__":
    locations = ["火車站", "早餐店", "博物館", "老街", "夜市"]
    locations_iterator = iter(locations)
    for i in range(3):
        print(
            f"{next(locations_iterator)}, 還剩下 {len(locations) - i - 1} 個景點尚未拜訪"
        )

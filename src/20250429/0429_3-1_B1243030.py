from rich import print

if __name__ == "__main__":
    nums = input("輸入一串用 , 分隔的數字：").split(",")
    target_num = input("請輸入要查詢的數字：")
    buffer = (
        "總數："
        + str(len(nums))
        + "\n"
        + "總和："
        + str(sum(map(int, nums)))
        + "\n"
        + "最小值與最大值："
        + str(min(map(int, nums)))
        + ", "
        + str(max(map(int, nums)))
        + "\n"
        + "找出某個數字出現了幾次："
        + str(nums.count(target_num))
        + "\n"
        + "找出某個數字第一次出現的位置："
        + str(nums.index(target_num))
        + "\n"
    )
    print(buffer)

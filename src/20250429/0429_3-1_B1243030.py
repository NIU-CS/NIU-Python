from rich import print

if __name__ == "__main__":
    nums = input("輸入一串用 , 分隔的數字：").split(",")
    print("總數：", len(nums))
    print("總和：", sum(map(int, nums)))
    print("最小值與最大值：", min(map(int, nums)), max(map(int, nums)))
    print("找出某個數字出現了幾次：", nums.count(input("請輸入要查詢的數字：")))
    print("找出某個數字第一次出現的位置：", nums.index(input("請輸入要查詢的數字：")))
    full_string = ",".join(nums)
    print(full_string)

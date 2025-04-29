from rich import print

if __name__ == "__main__":
    nums = input("輸入一串用 , 分隔的數字：").split(",")
    # 去除每個元素的前後空白，並且過濾掉非數字
    nums = [num.strip() for num in nums if num.strip().isdigit()]
    nums = list(map(int, nums))  # 全部轉成整數

    print("總數：", len(nums))
    print("總和：", sum(nums))
    print("最小值與最大值：", min(nums), max(nums))

    target = input("請輸入要查詢的數字：").strip()
    if target.isdigit():
        target = int(target)
        print("找出某個數字出現了幾次：", nums.count(target))
        try:
            print("找出某個數字第一次出現的位置：", nums.index(target))
        except ValueError:
            print("[red]找不到該數字！[/red]")
    else:
        print("[red]輸入的不是數字！[/red]")

    full_string = "+".join(map(str, nums))
    print(f"{full_string} 分析完成！")

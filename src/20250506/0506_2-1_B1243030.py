from rich import print

if __name__ == "__main__":
    word = input("輸入一個英文字串：")

    print(f"第 0, 1, 2 個字元：{word[0:3]}")
    print(f"前 3 個字元：{word[:3]}, 後 3 個字元：{word[-3:]}")
    print(f"第 2 到倒數第 2 個字元：{word[2:-2]}")
    print(f"倒轉的字串：{word[::-1]}")
    print(f"重複三次：{word * 3}")
    print(f"前 2 個字元 + 後 2 個字元：{word[:2] + word[-2:]}")

from rich import print


def main():
    # 1. 讓使用者輸入一段文字 s
    s = input("請輸入一段文字：")
    # 2. 讓使用者輸入要搜尋的字元 c（假設只取第一個字元）
    c = input("請輸入要搜尋的字元：")
    if len(c) == 0:
        print("沒有輸入要搜尋的字元，程式結束。")
        return
    c = c[0]

    # 使用 find() 找出字元 c 第一次出現的位置
    first_pos = s.find(c)
    if first_pos != -1:
        print(f"字元 '{c}' 第一次出現的位置：{first_pos}")
    else:
        print(f"字元 '{c}' 未出現於字串中。")

    # 使用 rfind() 找出字元 c 最後一次出現的位置
    last_pos = s.rfind(c)
    if last_pos != -1:
        print(f"字元 '{c}' 最後一次出現的位置：{last_pos}")
    else:
        # 與第一次相同，未出現則已提示，可省略
        pass

    # 使用 count() 統計字元 c 出現的次數
    count = s.count(c)
    print(f"字元 '{c}' 出現次數：{count}")

    # 3. 讓使用者再輸入一個替代字元 r
    r = input("請輸入要將字元 '{}' 取代成的字元：".format(c))
    if len(r) == 0:
        print("沒有輸入替代字元，程式結束。")
        return
    r = r[0]

    # 使用 replace() 將所有 c 取代為 r，並印出結果
    new_s = s.replace(c, r)
    print("取代後的結果：")
    print(new_s)


if __name__ == "__main__":
    main()

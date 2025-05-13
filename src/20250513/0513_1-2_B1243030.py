from rich import print


def main():
    # 1. 輸入原始字串 S
    s = input("請輸入一段文字：")

    # 2. 輸入關鍵字 keyword
    keyword = input("請輸入關鍵字：")
    if not keyword:
        print("未輸入關鍵字，程式結束。")
        return

    # 3. 找出首次與末次出現位置
    first = s.find(keyword)
    last = s.rfind(keyword)

    if first == -1:
        print(f"關鍵字「{keyword}」未出現。")
    else:
        print(f"關鍵字「{keyword}」第一次出現位置：{first}")
        print(f"關鍵字「{keyword}」最後一次出現位置：{last}")

        # 4. 若出現超過 1 次，顯示所有中間出現位置
        #    （包含 first, last 也一起列出）
        positions = []
        start = 0
        while True:
            idx = s.find(keyword, start)
            if idx == -1:
                break
            positions.append(idx)
            start = idx + len(keyword)
        if len(positions) > 1:
            print(f"所有出現位置：{positions}")

    # 5. 輸入 replacement，取代所有 keyword → replacement
    replacement = input("請輸入要將關鍵字取代成的新詞：")
    if not replacement:
        print("未輸入 replacement，跳過取代。")
        replaced = s
    else:
        replaced = s.replace(keyword, replacement)
        print("取代後句子：")
        print(replaced)

    # 6. 輸入要隱藏的字詞 hide_word，將此字詞取代為 '*' 並顯示
    hide_word = input("請輸入想隱藏的字詞：")
    if not hide_word:
        print("未輸入隱藏字詞，程式結束。")
    else:
        mask = "*" * len(hide_word)
        hidden = replaced.replace(hide_word, mask)
        print("隱藏後句子：")
        print(hidden)


if __name__ == "__main__":
    main()

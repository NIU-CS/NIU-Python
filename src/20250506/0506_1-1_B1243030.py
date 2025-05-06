from rich import print

if __name__ == "__main__":
    word = input("輸入一段英文句子: ")
    for i, char in enumerate(word):
        if char.isupper():
            char_type = "大寫英文字母"
        elif char.islower():
            char_type = "小寫英文字母"
        else:
            char_type = "非英文字元"

        print(f"索引 {i} : 字元 {char}，ASCII 編碼 {ord(char)}，字元類型：{char_type}")

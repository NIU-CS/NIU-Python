from rich import print

if __name__ == "__main__":
    word = input("輸入一段英文句子: ")
    max_ascii = float("-inf")
    min_ascii = float("inf")
    encrypted_word = ""
    for i, char in enumerate(word):
        if char.isupper():
            char_type = "大寫英文字母"
            new_char = chr((ord(char) - ord("A") + 3) % 26 + ord("A"))
            max_ascii = max(max_ascii, ord(char))
            min_ascii = min(min_ascii, ord(char))
        elif char.islower():
            char_type = "小寫英文字母"
            new_char = chr((ord(char) - ord("a") + 3) % 26 + ord("a"))
            max_ascii = max(max_ascii, ord(char))
            min_ascii = min(min_ascii, ord(char))
        else:
            char_type = "非英文字元"
            new_char = char

        encrypted_word += new_char

        print(
            f"索引 {i} : 原字元 {char}，加密後字元 {new_char}，ASCII 編碼 {ord(char)}，字元類型：{char_type}"
        )

    if max_ascii == float("-inf") or min_ascii == float("inf"):
        max_ascii = None
        min_ascii = None

    print(f"加密後的句子：{encrypted_word}")
    print(f"最大 ASCII 值（僅英文字母）：{max_ascii}")
    print(f"最小 ASCII 值（僅英文字母）：{min_ascii}")

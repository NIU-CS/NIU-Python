from rich import print


def main():
    # 1. 讓使用者輸入一個由空白鍵分隔的句子
    s = input("請輸入句子：")  # 例如：Python is fun

    # 2. 使用 split() 將句子分割成單字列表
    words = s.split()
    print("單字列表：", words)  # 例如：['Python', 'is', 'fun']

    # 3. 使用 '|' .join() 將單字重新串接成一個以 '|' 分隔的新句子
    joined = "|".join(words)
    print("分隔的句子：", joined)  # 例如：Python|is|fun

    # 4. 使用 center() 將原句置中顯示，寬度 50，空格填充
    centered = s.center(50)
    print("置中顯示：[", centered, "]", sep="")
    # 顯示時用中括號包起來比較清楚

    # 5. 顯示原句長度（使用 len()）
    length = len(s)
    print("句子長度：", length)  # 例如：14

    # 6. 使用 strip() 去除置中後字串左右的空白，並印出
    stripped = centered.strip()
    print("去空白後內容：", stripped)  # 應與原句相同


if __name__ == "__main__":
    main()

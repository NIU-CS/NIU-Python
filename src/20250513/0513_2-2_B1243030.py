from rich import print


def paragraph_analyzer():
    # 1. 輸入關鍵字
    keyword = input("請輸入關鍵字：")
    if not keyword:
        print("未輸入關鍵字，程式結束。")
        return

    # 2. 依序輸入多個段落，空行結束
    print("請依序輸入段落，輸入空行後結束：")
    paragraphs = []
    idx = 1
    while True:
        p = input(f"段落 {idx}: ")
        if p == "":
            break
        paragraphs.append(p)
        idx += 1

    if not paragraphs:
        print("沒有輸入任何段落，程式結束。")
        return

    # 3. 檢查格式並去除首尾空白
    cleaned = []
    bad_count = 0
    for p in paragraphs:
        p_stripped = p.strip()
        # 檢查開頭與結尾
        if not (p_stripped.startswith(keyword) and p_stripped.endswith(";")):
            bad_count += 1
        cleaned.append(p_stripped)

    # 4. 格式化串接
    formatted = "\n---\n".join(cleaned)

    # 5. 列印分析結果與格式化後內容
    print("\n— 分析結果 —")
    print(f"總段落數：{len(paragraphs)}")
    print(f"不符合「以 {keyword} 開頭 且以 ';' 結尾」的段落數：{bad_count}")

    print("\n— 格式化輸出 —")
    print(formatted)


if __name__ == "__main__":
    paragraph_analyzer()

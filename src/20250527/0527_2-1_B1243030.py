from rich import print

def main():
    # 初始菜單：各品項目前剩餘份數
    menu = {
        '美式咖啡': 10,
        '澳式咖啡': 6,
        '摩卡': 0,
        '卡布奇諾': 4,
        '焦糖瑪奇朵': 2
    }

    # 1. 檢查「冰滴咖啡」是否已在菜單中，若無則新增 7 份
    if '冰滴咖啡' not in menu:
        menu['冰滴咖啡'] = 7
        print("[green]已新增「冰滴咖啡」：7 份[/]")

    # 2. 若「摩卡」庫存為 0，則刪除此品項
    if menu.get('摩卡', 0) == 0:
        menu.pop('摩卡')
        print("[yellow]已刪除庫存為 0 的「摩卡」[/]")

    # 3. 補貨「拿鐵」5 份（若原本不存在，視為 0 再加）
    menu['拿鐵'] = menu.get('拿鐵', 0) + 5
    print(f"[blue]「拿鐵」補貨後剩餘：{menu['拿鐵']} 份[/]")

    print()  # 空行

    # 4. 以 for 迴圈列出所有品項及剩餘數量
    print("[bold]目前菜單品項與剩餘份數：[/]")
    for name, qty in menu.items():
        print(f"- {name}：{qty} 份")

    print()  # 空行

    # 5. 示範使用 key in menu 及 key not in menu 查詢品項是否存在
    for item in ['冰滴咖啡', '摩卡', '拿鐵']:
        exists = "存在" if item in menu else "不存在"
        print(f"品項「{item}」{exists}於菜單中。")

if __name__ == "__main__":
    main()

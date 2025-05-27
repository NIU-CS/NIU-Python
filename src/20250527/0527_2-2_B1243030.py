from rich import print

def main():
    # 進階初始菜單：庫存管理員需定期清理並更新
    menu = {
        '拿鐵'    : 12,
        '美式咖啡': 3,
        '澳式咖啡': 0,
        '卡布奇諾': 1,
        '冰滴咖啡': 0
    }

    # 1. 清除所有庫存為 0 的品項（使用 for + pop）
    zero_keys = [k for k, v in menu.items() if v == 0]
    for k in zero_keys:
        menu.pop(k)
        print(f"[yellow]已刪除庫存為 0 的「{k}」[/]")

    # 2. 刪除最後一筆品項（popitem），並印出該項 key 與 value
    last_item_key, last_item_val = menu.popitem()
    print(f"[red]已移除最後一筆品項：「{last_item_key}」剩餘 {last_item_val} 份[/]")

    # 3. 顧客點錯商品（安全刪除不存在的「濃縮咖啡」）
    result = menu.pop('濃縮咖啡', '查無此項目')
    if result == '查無此項目':
        print("[cyan]顧客誤點「濃縮咖啡」，查無此品項，已進行安全刪除（無任何變更）[/]")
    else:
        print(f"[cyan]已刪除「濃縮咖啡」：剩餘 {result} 份[/]")

    # 4. 清空整份菜單，並印出結果（應為 {}）
    menu.clear()
    print(f"[bold]清空後的菜單內容：{menu}[/]")

if __name__ == "__main__":
    main()

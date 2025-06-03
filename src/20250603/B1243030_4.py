def main():
    menu: dict = {
        "紅茶": 10,
        "綠茶": 6,
        "奶茶": 0,
        "冬瓜檸檬": 3,
        "烏龍茶": 7,
        "青茶": 2,
        "檸檬綠茶": 4,
        "百香果綠茶": 0
    }

    # 1. 若 "蜂蜜檸檬" 不在菜單中，請新增 "蜂蜜檸檬" :13
    if "蜂蜜檸檬" not in menu:
        menu["蜂蜜檸檬"] = 13
    # 2. 若 "奶茶" 庫存為 0，請移除
    if menu.get("奶茶", 0) == 0:
        menu.pop("奶茶", None)
    # 3. 將 "綠茶" 補貨 x 份（原本有 x 份就加 x 份）
    x = menu.get("綠茶", 0)
    menu["綠茶"] = x + x  # 假設 x 是綠茶的原本數量，這裡將其補貨兩倍
    # 4. 使用 for 印出所有品項與剩餘數量（格式如：紅茶：10 份）
    for item, quantity in menu.items():
        print(f"{item}：{quantity} 份")
    # 5. 讓使用者輸入一個品項名稱，使用 .pop() 嘗試安全刪除：
        # 若有該品項，請刪除並印出「已刪除 OO」
        # 若沒有該品項，請印出「查無此項目」
    item_to_remove = input("請輸入要刪除的品項名稱：")
    if item_to_remove in menu:
        menu.pop(item_to_remove)
        print(f"已刪除 {item_to_remove}")
    else:
        print("查無此項目")
    # 6. 批次清理：移除所有庫存為 0 的品項
    items_to_remove = [item for item, quantity in menu.items() if quantity == 0]
    for item in items_to_remove:
        menu.pop(item, None)
    # 7. 將菜單依 "以上操作過後" 的剩餘數量由多到少排序後印出
    sorted_menu = sorted(menu.items(), key=lambda x: x[1], reverse=True)
    print("【菜單】")
    for item, quantity in sorted_menu:
        print(f"{item}：{quantity} 份")

if __name__ == "__main__":
    main()

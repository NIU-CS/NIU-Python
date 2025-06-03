def main():
    VIP_price: map = {
        "VIP": 0.8,
        "金卡": 0.85,
        "銀卡": 0.9,
        "普通": 1
    }

    VIP = input("輸入會員等級(VIP/金卡/銀卡/普通): ")
    input_amount = ""
    amount_list: list[str] = []
    while input_amount != "finish":
        input_amount = input("請輸入消費金額: ")
        amount_list.append(input_amount)

    amount_list.pop() # pop finish

    origin_total = 0
    VIP_total = 0
    n_item = len(amount_list)
    print()
    print("每筆折扣後金額: ")
    for amount in amount_list:
        print(f"{amount} -> {int(float(amount) * VIP_price[VIP])} 元")
        origin_total += int(amount)
        VIP_total += float(amount) * float(VIP_price[VIP])

    print()
    print(f"原始總金額: {origin_total} 元")
    print(f"折扣後總金額: {int(VIP_total)} 元")
    print(f"平均每筆應付: {int(VIP_total/n_item)} 元")

if __name__ == "__main__":
    main()

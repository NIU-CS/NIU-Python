def main():
    meals: list = [["牛肉飯", 100], ["雞腿飯", 90], ["蔬食便當", 85]]
    drinks:list = [["紅茶", 30], ["綠茶", 25], ["奶茶", 35]]
    # 輸出所有主餐 + 飲料的組合與價格
    print("【無甜點】")
    for meal in meals:
        for drink in drinks:
            print(f"{meal[0]} + {drink[0]} = {meal[1] + drink[1]}元")
    # 輸出所有主餐 + 飲料 + 甜點的組合與價格
    print("【加購甜點】")
    for meal in meals:
        for drink in drinks:
            print(f"{meal[0]} + {drink[0]} + 甜點 = {meal[1] + drink[1] + 20}元")


if __name__ == "__main__":
    main()

from rich import print

def discount(spent):
    if spent >= 0 and spent < 500:
        return 1
    elif spent >= 500 and spent <= 999:
        return 0.95
    elif spent >= 1000 and spent <= 1999:
        return 0.9
    elif spent >= 2000 and spent <= 2999:
        return 0.85
    elif spent >= 3000 and spent <= 3999:
        return 0.8
    elif spent >= 4000 and spent <= 4999:
        return 0.75
    elif spent > 5000:
        return 0.7
    else:
        return 0

def gap_to_next_level(spent):
    if spent >= 0 and spent < 500:
        return 500 - spent
    elif spent >= 500 and spent <= 999:
        return 1000 - spent
    elif spent >= 1000 and spent <= 1999:
        return 2000 - spent
    elif spent >= 2000 and spent <= 2999:
        return 3000 - spent
    elif spent >= 3000 and spent <= 3999:
        return 4000 - spent
    elif spent >= 4000 and spent <= 4999:
        return 5000 - spent
    elif spent > 5000:
        return 0

if __name__ == "__main__":
    spent = float(input("輸入購物金額："))
    print(f"折扣後的金額：{discount(spent) * spent}")
    print(f"更優惠折扣還需要：{gap_to_next_level(spent)} 元")

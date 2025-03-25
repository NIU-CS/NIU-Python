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

if __name__ == "__main__":
    spent = float(input("輸入購物金額："))
    print(f"折扣後的金額：{discount(spent) * spent}")

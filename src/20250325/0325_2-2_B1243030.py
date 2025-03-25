from rich import print

def grade(score):
    if score < 0 or score > 100:
        return 'N'
    elif score >= 90:
        return 'A'
    elif score >= 85:
        return 'B+'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C+'
    elif score >= 60:
        return 'C'
    else:
        return 'F'

if __name__ == "__main__":
    score = input("輸入分數：")
    print(f"等第：{grade(int(score))}")
    print("及格" if (grade(int(score)) != 'F' and grade(int(score)) != 'N') else "不及格")

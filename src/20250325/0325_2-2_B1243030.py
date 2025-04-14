from rich import print


def grade(score):
    if score < 0 or score > 100:
        return "N"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "B+"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C+"
    elif score >= 60:
        return "C"
    else:
        return "F"


def grade_score(grade):
    if grade == "A":
        return "90~100"
    elif grade == "B+":
        return "85~89"
    elif grade == "B":
        return "80~84"
    elif grade == "C+":
        return "70~79"
    elif grade == "C":
        return "60~69"
    else:
        return "0~59"


if __name__ == "__main__":
    score = input("輸入分數：")
    print(f"等第：{grade(int(score))}")
    print(
        "及格" if (grade(int(score)) != "F" and grade(int(score)) != "N") else "不及格"
    )
    print(f"分數區間在 {grade_score(grade(int(score)))}")

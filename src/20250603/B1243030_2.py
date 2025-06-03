def main():
    height = int(input("請輸入身高(cm): "))
    weight = int(input("請輸入體重(kg): "))
    BMI = weight / pow(float(height)/100, 2)
    print(f"BMI = {BMI:.2f}")

    if BMI < 18.5:
        print("健康評估: BMI 偏低")
    elif 18.5 <= BMI < 24:
        print("健康評估: BMI 適中")
    elif 24 <= BMI < 27:
        print("健康評估: BMI 偏高")
    elif 27 <= BMI < 30:
        print("健康評估: BMI 過高")
    elif 30 <= BMI < 35:
        print("健康評估: BMI 明顯過高")
    else:
        print("健康評估: BMI 嚴重過高")

if __name__ == "__main__":
    main()

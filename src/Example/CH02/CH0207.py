from fractions import Fraction #匯入fractions模組

num1 = Fraction(7, 8)
num2 = Fraction(12, 17)
print(num1 + num2)   # 將兩個分數相加，輸出 215/136
num3 = num1 * num2   # 將兩個數相乘
num3.numerator       # 取得分子，輸出21
num3.denominator     # 取得分母，輸出34
print(float(num3))

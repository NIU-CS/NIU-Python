from decimal import * #滙入decimal所有內容

getcontext().prec = 8   #設精確度為4
result = Decimal(20) / Decimal(3)
print('20/3 = ', result)

num1, num2 = Decimal(2.358), Decimal(0.669)
print('num1 + num2 =', num1 + num2)
print('num1 * num2 =', num1 * num2)

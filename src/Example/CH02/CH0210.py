#使用位元運算子
x, y = 6, 13
print('x =',x, 'y =', y)

# bin()函式轉為二進位
print('x 二進位 ->', bin(x), ', y 二進位->', bin(y))
print('x & y =', bin(x & y))

# 函式int()把二進位轉為10進位
print('轉為10進位 ->', int('100', 2))

# 位元運算子直接以10進位做運算
print('x | y =', x | y)
print('x ^ y =', x ^ y)
print('~110 ->', ~110, '轉-111為10進位', int('-111', 2))
print('~x =', ~x, ', ~y =', ~y)

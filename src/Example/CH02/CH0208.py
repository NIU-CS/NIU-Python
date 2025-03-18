import math	#匯入math模組

#求平方根，輸出12.0, math模組和數值運算
print('math.sqrt(144) = ', math.sqrt(144))	
print('144 ** 0.5 = ', 144 ** 0.5)

# 使用pow()方法
print('math.pow(3, 3) =', math.pow(3, 3)) # 3*3*3或是3^3，輸出27
print(math.pow(27, 1.0/3))   # 立方根∛27，輸出3.0
print(math.pow(4, 4))        # 4的4次方，輸出256
print(math.pow(256, 1.0/4))  # 4方根，輸出4.0

# ceil()方法，無條件進位
print('math.ceil(4.2) =', math.ceil(4.2),
      ', math.ceil(-4.2) =', math.ceil(-4.2))	# 輸出5, -4

# floor()方法無條件捨位
print(math.floor(-8.9), math.floor(9.7))# 輸出-9, 9

# √(3^2+9^2 )的結果，輸出9.4868
print('math.hypot(3, 9) =', math.hypot(3, 9))	

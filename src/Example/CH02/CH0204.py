number = 88.12694   #宣告為float型別
num16 = number.hex()   # 以16進位回傳

# 輸出0x1.6081fc8f32379p+6
print('16進制浮點數', num16)
# 回傳88.12694，轉換回10進位
print('轉換10進位', float.fromhex(num16))

import math #匯入math模組

a = 1E309
print('a = 1E309, a 是', a)
# 輸出True，表示它是NaN
print('為NaN?', math.isnan(float(a/a)))

b = -1E309
print('b = -1309, b 是', b)
# 輸出True，表示它是Inf
print('為Inf?', math.isinf(float(-1E309)))

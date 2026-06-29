# Floor Division (//)

print(7 // 3)    # 2
print(-7 // 3)   # -3   (floors down: -2.333... → -3)


# Modulo %
print(7 % 3)    # 1   #   7/3 =  2.33.. floor to  2,  2*3  =  6,  7 =  6 + remainder=1   
print(-7 % 3)   # 2   #  -7/3 = -2.33.. floor to -3, -3*3  = -9, -7 = -9 + remainder=2
print(7 % -3)   # -2  #  7/-3 = -2.33.. floor to -3, -3*-3 =  9,  7 =  9 + remainder=-2
print(14 % 12)  # 2   # 14/12 = 1.1666667 flor to 1, 1*12 = 12, 14 = 12 + remainder=2

# Selecting every 3rd item in a list
kids = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in kids:
    if i % 3 == 0:
        print(kids[i])

# Printing every 3rd number from numbers generated from range
for i in range(0,100):
    if i % 3 == 0:
        print(i)

print("2.675 gets rounded to:",round(2.675,2), "Not 2.68 b/c actual stored value is 2.67499999999")          
# 2.67  (binary float nuance)

# When the value you’re rounding is exactly halfway between 
# two possible results, Python will pick the one with an 
# even least significant digit.
# “Ties to even” rounding (a.k.a. banker's rounding)
print("2.5 gets rounded down to: ",round(2.5),"is even") # 2   ← 2 is even
print("4.5 gets rounded down to: ",round(4.5),"is even") # 4   ← 4 is even
print("6.5 gets rounded down to: ",round(6.5),"is even") # 6   ← 4 is even
print("1.5 gets rounded up to: ",round(1.5),"is even")   # 2   ← 2 is even
print("3.5 gets rounded up to: ",round(3.5),"is even")   # 4   ← 4 is even
print("5.5 gets rounded up to: ",round(5.5),"is even")   # 6   ← 6 is even

import math
print(math.floor(2.9), math.ceil(2.1), math.trunc(-2.9))  # 2  3  -2
print(math.sqrt(9))                                       # 3.0
print(math.pi, math.e)                                    # 3.14159...  2.71828...
print(math.isfinite(1.0), math.isfinite(float('inf')))    # True False

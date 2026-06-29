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

print(round(2.5), round(3.5))   # 2  4
print(round(2.675, 2))          # 2.67  (binary float nuance)


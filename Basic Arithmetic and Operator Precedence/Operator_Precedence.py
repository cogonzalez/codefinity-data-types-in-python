print(2 + 3 * 4)     # 14  (multiplication before addition)
print((2 + 3) * 4)   # 20  (parentheses change the order)

# Exponentiation binds tighter than unary minus
print(-3 ** 2)       # -9  (equivalent to -(3 ** 2))
print((-3) ** 2)     # 9

# Right-associative exponentiation
print(2 ** 3 ** 2)   # 512 (2 ** (3 ** 2))

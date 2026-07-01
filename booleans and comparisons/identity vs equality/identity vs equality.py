# Comparing two shopping carts in an online store
cart_today = ["milk", "bread"]
cart_yesterday = ["milk", "bread"]
shared_cart = cart_today

#   is checks object identity, whether two variables point to the same object in memory
#      check if two names point to the same object
#   == checks equality of values, whether two objects have the same contents.
#      check if two values are equal

print(cart_today == cart_yesterday)  # True → same items
print(cart_today is cart_yesterday)  # False → two separate cart objects
print(cart_today is shared_cart)     # True → both refer to the same cart

# Use ( is ) in comparison with singletons such as None;
# Checking if the user has entered their phone number
user_phone = None

if user_phone is None:
    print("No phone number provided yet")

# ( is not ) is the negated identity check;
# Checking if the user's age is stored in the system
user_age = 64

if user_age is not None:
    print(f"User age is recorded: {user_age}")

# Avoid using is to check for equality between numbers or strings.
# Due to internal caching/interning, identity may appear to "work" sometimes, 
# but it's not reliable across different runs and environments, use == instead;
# Comparing user IDs and usernames in a system

user_id_a = 256
user_id_b = 256

print(user_id_a == user_id_b)  # True → same user ID value
print(user_id_a is user_id_b)  # True → May appear True, but identity check is unreliable for numbers

username_a = "hello"
username_b = "he" + "llo"

print(username_a == username_b)  # True → same text
print(username_a is username_b)  # True → Avoid using 'is' for string comparison (implementation detail)

# Comparing user IDs and usernames in a system
user_id_a = 175256
user_id_b = 175256

print(user_id_a == user_id_b)  # True → same user ID value
print(user_id_a is user_id_b)  # False, but identity check is unreliable for numbers

# Small integers (typically between −5 and 256) are interned in CPython,
# meaning multiple variables with the same small-integer literal may actually
# point to the same object. For larger ints this caching can break, so relying 
# on is for numbers is unreliable.

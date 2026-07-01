profile_complete = True
user_name = ""
messages_sent = 0

if profile_complete:
    print("Welcome to your dashboard!")  # Printed because profile is complete

print(bool(user_name))     # False → no name provided yet
print(bool(messages_sent)) # False → user hasn't sent any messages
print(bool("ok"))          # True  → any non-empty string counts as valid input

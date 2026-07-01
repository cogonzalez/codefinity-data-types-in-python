age = 21
has_id = True
print(age >= 18 and has_id)   # True

# Choosing a display name for a user profile
username = ""             # user didn't set a custom name
print(username or "Guest")   # "Guest" → fallback to default name

username = "Alice"
print(username or "Guest")   # "Alice" → custom name is used

# Checking login attempts and access permissions
login_attempts = 0
access_level = 123
print(login_attempts and access_level)  # 0 → login not yet attempted

login_attempts = 5
print(login_attempts and access_level)  # 123 → user has access after attempts

# Checking empty and non-empty values
print(not 0, not "Hello")  # True False → 0 is falsey, non-empty string is truthy

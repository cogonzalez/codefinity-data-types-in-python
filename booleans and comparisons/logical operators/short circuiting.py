# Choosing a display name for a user profile
username = ""       # user didn't set a custom name
un = bool(username) # username is an empty string, & is Falsy boolean
g = bool("Guest")   # "Guest" is a string, & is Truthy boolean
print(f"username is {un}, & 'Guest' is:{g}, so (username or 'Guest') returns")
print(username or "Guest") 
# A or B:
# If A is falsy, the outcome depends entirely on B, 
# so Python evaluates and returns B.
# "Guest" → fallback to default name

username = "Alice"
un = bool(username) # username is NOT empty string, & is Truthy boolean
g = bool("Guest")   # "Guest" is a string, & is Truthy boolean
print(f"username is {un}, & 'Guest' is:{g}, so (username or 'Guest') returns")
print(username or "Guest") 
# A or B:
# If A is truthy, the result is guaranteed to be truthy, 
# so Python short-circuits and returns A (without evaluating B).
# "Alice" → custom name is used

# Checking login attempts and access permissions
login_attempts = 0     # falsy
access_level = 123     # truthy
la = bool(login_attempts)
al = bool(access_level)
print(f"login_attempts is: {la}, & access_level is: {al},\n so (login_attempts and access_level) returns:")
print(login_attempts and access_level)
# A and B:
# If A is falsy, the result is guaranteed to be falsy, 
# so Python short-circuits and returns A (without evaluating B).
# 0 → login not yet attempted

login_attempts = 5       # truthy
la = bool(login_attempts)
al = bool(access_level)
print(f"login_attempts is: {la}, & access_level is: {al},\n so (login_attempts and access_level) returns:")
print(login_attempts and access_level)  
# A and B:
# If A is truthy, the outcome depends entirely on B,
# so Python evaluates and returns B.
# 123 → user has access after attempts

# Checking empty and non-empty values
print(f"not 0 is:{not 0}, not 'Hello' is: {not 'Hello'}")  
# True False → 0 is falsey, non-empty string is truthy

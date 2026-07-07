age_str = "19"
has_id_str = " Yes "
ticket_code = "VIP-023-A"
is_member = False
adult_age = 18
max_seat_number = 150

# 1) Age as int
age = ___(___.___())

# 2) ID possession as Boolean from text
has_id = ___(___.___() ___ "yes")

# 3) Parse ticket parts by fixed positions
tier = ticket_code[___:___]             # "VIP"
seat_number_str = ticket_code[___:___]  # "023"
zone = ticket_code[___]                 # "A"

# 4) Seat number as int
seat_number = ___(seat_number_str)

# 5) Rules
is_adult = age ___ adult_age
can_enter = has_id ___ is_adult
vip_perk = tier ___ "VIP"
member_fastlane = is_member ___ can_enter
seat_ok = ___ ___ seat_number ___ ___
entry_granted = can_enter ___ seat_ok

# 6) Summary line
summary = f"{tier}-{seat_number_str}-{zone} | age={age} | enter={entry_granted} | vip={vip_perk} | fastlane={member_fastlane}"

print(age, has_id, tier, seat_number_str, zone, seat_number, is_adult, can_enter, vip_perk, member_fastlane, seat_ok, entry_granted, sep=" | ")
print(summary)
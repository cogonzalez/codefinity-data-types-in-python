num_calls = 8
minutes_per_call = 9
available_minutes = 60

# 1) Total time needed
#    * Multiplies numbers
total_minutes = num_calls * minutes_per_call

# 2) How many minutes you are short
#    Subtracts the right number from the left
shortfall = total_minutes - available_minutes

# 3) How many full calls you can finish
#    // Performs floor division (rounds down)
completed_calls = available_minutes // minutes_per_call

# 4) How many minutes remain unused
#    Returns the remainder of division
unused_time = available_minutes % minutes_per_call

# Print results
print("Total minutes needed:", total_minutes)
print("Minutes short:", shortfall)
print("Completed calls:", completed_calls)
print("Unused time:", unused_time)
import musical_scales

# Get key and scale user would like to play in
user_key = input("Please enter the key you'd like to play in.\n:")
user_scale = input("Please enter the scale you'd like to play in.\n:")

# Change the casing to match the function parameters
user_key = user_key.upper()
user_scale = user_scale.lower()

# Print the users key and scale notes
notes = musical_scales.scale(user_key, user_scale)
print(notes)
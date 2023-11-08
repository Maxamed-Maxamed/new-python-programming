# Get the user's name
name = input("What's your name? ")

# Get information about what the user does for a living
occupation = input("What do you do for a living? ")

# Print the collected information
print(f"Hello, {name}! It's nice to meet you.")
print(f"So, you are a {occupation}. That's interesting!")

# Optionally, you can save this information to a file for later use
with open("user_info.txt", "w") as file:
    file.write(f"Name: {name}\nOccupation: {occupation}")

# Close the program
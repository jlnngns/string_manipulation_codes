# Ask the user to input their full name
full_name = input("Input your full name: ")

# Convert to snake_case (lowercase and replace spaces with underscores)
snake_case_name = "_".join(full_name.lower().split())

# Print the result
print("Output:", snake_case_name)

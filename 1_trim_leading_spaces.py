# Ask the user to input their full name with leading spaces
full_name = input("Input your full name (with leading spaces): ")

# Remove leading spaces
cleaned_name = " " + full_name.lstrip()

# Print the output
print("Output:", cleaned_name)

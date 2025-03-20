# Ask the user to input their full name
full_name = input("Input your full name: ")

# Convert to Pascal Case (capitalize each word and remove spaces)
pascal_case_name = "".join(full_name.title().split())

# Print the result
print("Output:", pascal_case_name)

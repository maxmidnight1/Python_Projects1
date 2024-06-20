# Ask user for their name
name = input("What's your name? ").strip().title()

# Remove whitespace from str and capitalize user name
#name = name.strip().title()

# Split user's name into first name andd last name
first, last = name.split(" ")

# Say hello to user
print("hello, " + first)
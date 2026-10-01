# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") #prints normally
print(f"Modified String 1: {user_string.lower()}")#changes to all lowercases
print(f"Modified String 2: {user_string.upper()}")#changes to all uppercases
print(f"Modified String 3: {user_string.strip()}")#removes spaces
print(f"Modified String 4: {user_string.replace('a', '@')}")#replaces a with @
print(f"Modified String 5: {user_string.capitalize()}") #capitalize only the first letter
print(f"Modified String 6: {user_string[::-1]}")#reverses the string
print(f"Modified String 7: {user_string.title()}")# capitalizes every letter at the beginning of the word
print(f"Modified String 8: {len(user_string)}")#the total count of the world
print(f"Modified String 9: {user_string.find('a')}")#find if there any occurences of a
print(f"Modified String 10: {user_string.count('a')}")#counts how many occurences of a
print(f"Modified String 11: {user_string.startswith('Hello')}")#returns true if starts with hellor or false if not
print(f"Modified String 12: {user_string.endswith('!')}")# returns true if it ends with ! or false if not
print(f"Modified String 13: {user_string.isalnum()}")#returns true if its alphanumeric or false if not
print(f"Modified String 14: {user_string.isalpha()}")#returns true if its alphabetic letters or false if  not
print(f"Modified String 15: {user_string.isdigit()}")#returns true if its number or false if not



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!
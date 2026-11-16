import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many namesde
# from the list, avoiding any duplicate choices
numtochoose=int(input("Enter a number to print how many names:"))
chosennames=random.sample(names,numtochoose)
for name in chosennames:
    print(name)

# Display the chosen names, one per line

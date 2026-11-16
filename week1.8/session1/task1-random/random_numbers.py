import random

# Get user to input how many random numbers they want
numrandomnumbers=int(input("Enter how many random numbers you want:"))
with open("random.txt","w") as file:
    for i in range(numrandomnumbers):
        file.write(str(random.randint(0,100))+"\n")
   
# Generate this many random numbers

# Write the random numbers to a file named random.txt, one number per line

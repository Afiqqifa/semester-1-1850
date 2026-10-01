# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)
num1=input("enter a number")
num2=input("enter a number")

while not num1.isdigit() or not num2.isdigit():
    print("thats not a number")
    num1=input("enter a number")
    num2=input("enter a number")
# multiply those numbers together
num1=int(num1)
num2=int(num2)
total=num1*num2
# print out the result
print(total)
# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!
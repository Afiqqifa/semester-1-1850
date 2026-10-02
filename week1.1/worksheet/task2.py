"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

num=input("enter amount:")
try:
  monthlyamount=int(num)
  totalamount=monthlyamount*12
  amountsaved=totalamount*1.008
  print(f"Total amount saved in a year:£{totalamount}")
  print(f"Total amount saved:£{amountsaved:.2f}")
except ValueError:
  print("Invalid amount")
        

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.


# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.


# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).


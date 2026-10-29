# Week 1.5, Session 2: Task 5

# Write a program here to create a Dataset containing data
# from a file named by the user
from data import Dataset

d1=Dataset(input("Enter the filename: "))
print("Dataset size:", len(d1))
print("Mean:", d1.mean())
print("Median:", d1.median())
for i in range(len(d1)):
    print(d1[i])
print(d1[2])

# Your program should display dataset size, mean and median,
# followed by the individual values (using a for loop)

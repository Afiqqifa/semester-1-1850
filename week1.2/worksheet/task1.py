# Worksheet 1.2: Task 1 Solution
import sys

rawgradenum=input("Enter your grade:")
try:
    gradenum=int(rawgradenum)
    if gradenum>=0 and gradenum<40:
        grade="Fail"
    elif gradenum>=40 and gradenum<70:
        grade="Pass"
    elif gradenum>=70 and gradenum<=100:
        grade="Distinction"
    else:
        sys.exit("Error: Grade must be an integer between 0 and 100")
    print(f"{gradenum} is a {grade}")
except(ValueError,EOFError,KeyboardInterrupt):
    sys.exit("Error: Grade must be an integer between 0 and 100")


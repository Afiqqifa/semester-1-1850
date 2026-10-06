# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

listofnumbers=read_numbers()

try:
    minval=min(listofnumbers)
    maxval=max(listofnumbers)
    mean=(sum(listofnumbers)/len(listofnumbers))
    sortedlist=sorted(listofnumbers)
    n=len(listofnumbers)
    if n%2==0:
        median=(sortedlist[(n//2)-1]+sortedlist[n//2])/2
    else:
        median=sortedlist[n//2]
    print("Minimum:",minval)
    print("Maximum:",maxval)
    print("Mean:",mean)
    print("Median:",median)
except:
    sys.exit("Error: no numbers provided")
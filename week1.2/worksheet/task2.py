# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

try:
    listofnumbers=read_numbers()
    if not listofnumbers:
        raise ValueError

    minval=min(listofnumbers)
    maxval=max(listofnumbers)
    mean=(sum(listofnumbers)/len(listofnumbers))
    sortedlist=sorted(listofnumbers)
    n=len(listofnumbers)
    if n%2==0:
        median=float((sortedlist[(n//2)-1]+sortedlist[n//2])/2)
    else:
        median=float(sortedlist[n//2])
    print("Minimum:",{minval:.1f})
    print("Maximum:",{maxval:.1f})
    print("Mean:",{mean:.1f})
    print("Median:",{median:1.f})
except(ValueError,ZeroDivisionError,EOFError,KeyboardInterrupt):
    sys.exit("Error: no numbers provided")
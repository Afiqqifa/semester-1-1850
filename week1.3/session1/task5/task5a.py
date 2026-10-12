# Week 1.3, Session 1: Task 5a

course = "computer science"
mylist=[]

for ch in course:
	print(ch)
	if ch!=" ":
		mylist.append(ch)
print(mylist)

mylist.sort()
print(mylist)

# create a list data structure of the characters from the course string
# sort the list into alphabetical order
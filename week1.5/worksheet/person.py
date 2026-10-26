# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self, name, birth):
       
        self.name = name
        self.birth = birth
    
    def initials(self):
        initialsperson="".join([part[0].upper() for part in self.name.split()])
        return initialsperson
    
    def is_birthday(self):
        today = date.today()
        return (self.birth.month, self.birth.day) == (today.month, today.day)

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
person1=Person("Afiq Hazmi", date(2000, 6, 15))
print(person1.initials())
if person1.is_birthday():
    print("Happy Birthday!")

person2=Person("John Doe", date(1990, 10, 26))
print(person2.initials())
if person2.is_birthday():
    print("Happy Birthday!")

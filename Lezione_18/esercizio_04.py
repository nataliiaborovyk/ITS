

'''
Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date,
 delete a given date, modify a date, and perform a query on a given date is required.  
 A query on a given date allows for retrieving a given new date. 
 Note that a date is an object for your database; it must be instantiated from a string.
'''

from datetime import datetime


class Data:

    def __init__(self, date:str):
        try: self.date = datetime.strptime(date, "%d.%m.%Y")       #strptime method serve per convertire stringa in datetime object
        except ValueError:
            raise ValueError(f"{date} is not correct format, must be gg.mm.aaaa")
         
    def __str__(self) -> str:
        return self.date.strftime("%d.%m.%Y")       #strftime method serve per convertire datetime object in stringa


# a = Data("132.32.4325")
# print(a)

try:  
    a = Data("132.32.4325")
    print(a)
except ValueError as error:
    print(error)


    
'''
Exercise 1: Create a function in Python
Write a program to create a function that takes two arguments, 
name and age, and print their value.
'''
# versione 1

def date(name: str, age: int) -> dict[str, int]:
    return {"Name":name, "age": age}

user= date("Nat", 40)
#print(f"Name: {user["Name"]}, age: {user["age"]}\n")
print(user["Name"])
print(user["age"])



# versione 2

def date_2(name:str, age:int):
    print(f"\nName is: {name} and age is: {age}")

date_2("Nataliia", 25)


def date_3(**kwargs) -> dict[str, int]:
    for name, age in kwargs.items():
        print(f"\n{name}: {age}")
    return {"Name": name, "Age": age}
  
print(date_3(name="Nat", age=40))

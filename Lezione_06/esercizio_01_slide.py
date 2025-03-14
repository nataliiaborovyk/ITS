class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

print(f"\nEta di Bob: {bob.age}")

if alice.age > bob.age:
    print(f"{alice.name } è piu grande")
elif alice.age < bob.age:
    print(f"{bob.age}  è piu grande")
else:
    print("Hanno eta uguale")

marco = Person("Marco C", 36)
federico = Person("Federico H", 27)
leonardo = Person("Leonardo P", 29)


people:list = [alice, bob, marco, federico, leonardo]
p_min = people[0]
for p in people:
    if p.age < p_min.age:
        p_min = p
   
print(f"Eta minore: {p_min.name}")

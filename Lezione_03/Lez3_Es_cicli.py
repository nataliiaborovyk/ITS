#esercizio 4-1
print("\n Esercizio 4-1 \n")

pizza_n:list = ["Margherita", "Marinara", "Napoletana"]

for i in pizza_n:
    print(i)

for i in pizza_n:
    print(f"I like {i} pizza")

print("Margherita Pizza is made with tomato sauce or marinara as the base sauce on the crust. \n\
Marinara Pizza is made with tomato sauce, extra virgin olive oil, oregano, and garlic. \n\
Napoletana pizza is made with mozzarella slices topped off with olives\
anchovies \nand a scatter of capers and basil leaves.\n \
I really love pizza!\n")



#esercizio 4-2
print("\n Esercizio 4-2 \n")

animals:list = ["Dog", "Cat", "Parrot"]

for i in animals:
    print(i)

for i in animals:
    print(f"A {i} would make a great pet")

print("Any animal og our list would make a great pet!")



#esercizio 4-3
print("\n Esercizio 4-3 \n")

for i in range(1,21):
    print(i)


'''
#esercizio 4-4
print("\n Esercizio 4-4 \n")

list_num:list = []

for i in range(1,1000001):
    list_num.append(i)

print(list_num)

'''

#esercizio 4-5
print("\n Esercizio 4-5 \n")

list_num:list = []

for i in range(1,1000001):
    list_num.append(i)

print(min(list_num),max(list_num), sum(list_num))



#esercizio 4-6
print("\n Esercizio 4-6 \n")

list_disp:list = []

for i in range(1,21,2):
    list_disp.append(i)

print(*list_disp)



#esercizio 4-7
print("\n Esercizio 4-7 \n")

list_mult3:list = []

for i in range(3,31,3):
    list_mult3.append(i)

print(*list_mult3)


#esercizio 4-8
print("\n Esercizio 4-8 \n")

list_cub:list = []

for i in range(1,10):
    i=i**3
    list_cub.append(i)
for i in list_cub:
    print(i)

'''
numbers:list=[1,11]
cubi=[]
for i in numbers:
    n=n**3
    cubi.append(cubo)
'''


#esercizio 4-9
print("\n Esercizio 4-9 \n")



#esercizio 4-10
print("\n Esercizio 4-10 \n")

#esempio es 4-7
list_mult3:list = []

for i in range(3,31,3):
    list_mult3.append(i)

print(*list_mult3)

'''
print(f"The  first three items in the list are: {list_mult3[0]}, {list_mult3[1]}, {list_mult3[2]}")

print(f"Three items from the middle of the list are: ")

print(f"The last three items in the list are: ")
'''
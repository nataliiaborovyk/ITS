'''
4-4. One Million: Make a list of the numbers from one to one million, and then use 
a for loop to print the numbers. (If the output is taking too long, 
stop it by pressing CTRL-C or by closing the output window.)
'''

#esercizio 4-4
print("\n Esercizio 4-4 \n")

list_num: list = []

for i in range(1,1000001):
    list_num.append(i)

print(list_num)
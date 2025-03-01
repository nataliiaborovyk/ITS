'''
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names 
in a list, and then use a for loop to print the name of each pizza.
• Modify your for loop to print a sentence using the name of the pizza, instead of printing 
just the name of the pizza. For each pizza, you should have one line of output containing 
a simple statement like I like pepperoni pizza.
• Add a line at the end of your program, outside the for loop, that states how much you like pizza. 
The output should consist of three or more lines about the kinds of pizza you like 
and then an additional sentence, such as I really love pizza!
'''

#esercizio 4-1
print("\n Esercizio 4-1 \n")

pizza_n: list = ["Margherita", "Marinara", "Napoletana"]

for i in pizza_n:
    print(i)

for i in pizza_n:
    print(f"I like {i} pizza")

print("Margherita Pizza is made with tomato sauce or marinara as the base sauce on the crust. \n\
Marinara Pizza is made with tomato sauce, extra virgin olive oil, oregano, and garlic. \n\
Napoletana pizza is made with mozzarella slices topped off with olives\
anchovies \nand a scatter of capers and basil leaves.\n \
I really love pizza!\n")
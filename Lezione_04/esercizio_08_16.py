'''
8-16. Imports: Using a program you wrote that has one function in it,
 store that function in a separate file. Import the function into your main program file, 
 and call the function using each of these approaches:
import module_name
- from module_name import function_name
from module_name import function_name as fn
- import module_name as mn
- from module_name import *
'''


#import sys
#sys.path.append("/home/its/Esercizi/Lezione_04/Tools")


# VERSIONE 1       from module_name import *
print("\n Versione 1")

from Tools import functions_1

functions_1.print_numbers([3, 3])    #perche stampa anche print che stanno fuori funzioni???
functions_1.saluto()


# VERSIONE 2       from module_name import function_name
print("\n Versione 2")

from Tools.functions_1 import print_numbers, saluto

print_numbers([2, 2, 3, 3])
saluto()


# VERSIONE 3       import module_name as mn
print("\n Versione 3")

import Tools.functions_1 as mn

mn.saluto()
mn.print_numbers([5,5,5])


# VERSIONE 4       from module_name import function_name as fn
print("\n Versione 4")

from Tools.functions_1 import print_numbers as fn1
from Tools.functions_1 import saluto as fn2

fn1([1,1,1,1])
fn2()
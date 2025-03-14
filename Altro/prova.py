firstlst: list[int] = [1, 2, 3, 4, 5]
firstlst.extend( {8, 7, 6} )
print(firstlst[5])
print(type(firstlst[5]))

firstlst: list[int] = [1, 5, 7, 8] 
secondlst: list[int] = [2, 3, 7, 6]
hirdlst: list[int] = firstlst + secondlst
print(hirdlst)

#Inserisco la stringa di parentesi
bilanciate:str = input(str())

#Definisco le variabili "parentesi aperte", "parentesi chiuse" e imposto l'output su false
open_par:int = 0
close_par:int = 0
output:bool = False

#Se il numero di parentesi chiuse supera il numero di parentesi aperte è False e esce dal ciclo
for p in bilanciate:
    if p == "(":
        open_par += 1
    elif p == ")":
        close_par += 1
    else:
        output = False
        break
    
    if close_par <= open_par:
        output = True
    elif close_par > open_par:
        output = False
        break

#Se alla fine del conteggio le parentesi aperte superano il numero delle chiuse è False
if open_par != close_par:
    output = False

print(output)
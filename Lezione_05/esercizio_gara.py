
import random

print("Band!!! And They're off!!!!")

#come si muove la tartaruga

def tartaruga(posizione_t:int = 1):

    i_t: int = random.randint(1,10)

    if 1 <= i_t <= 5:     #Passo veloce 
        posizione_t += 3

    elif 6 <= i_t <= 7:     #Scivolata
        posizione_t -= 6

    elif 8 <= i_t <= 10:      #Passo lento
        posizione_t += 1

    if posizione_t < 1:
        posizione_t = 1
        
    return posizione_t
    

#come si muove la lepre  

def lepre(posizione_l:int = 1):

    i_h: int = random.randint(1,10)
    
    if 1 <= i_h <= 2:   #riposo 20%
        posizione_l += 0 

    elif 3 <= i_h <= 4:  #grande balzo 20%
        posizione_l -= 9

    elif 5 == i_h:
        posizione_l -= 12   #grande scivolata 10%

    elif 6 <= i_h <= 8:   #piccolo balzo 30%
        posizione_l += 1

    elif 9 <= i_h <= 10:   #piccolo scivolata 20%
        posizione_l += 2

    if posizione_l < 1:
        posizione_l = 1
        
    return posizione_l




def gara(quadratini:int = 70):
    tick = 0
    posizione_t = 1
    posizione_l = 1

    while (posizione_t < quadratini) and (posizione_l < quadratini):

        posizione_t = tartaruga(posizione_t)      #aggiorno la posizione dei animali in ogni atterazione
        posizione_l = lepre(posizione_l)
        
        percorso:list = []               #ogni volta creo una nuova lista e aggiungo le posizioni dei animali

        for i in range(quadratini):
            percorso.append("_")

        if posizione_l != posizione_t:
            percorso[posizione_t-1] = "T"      #animali partono dalla posizione 1 e indici della lista cominciano da 0
            percorso[posizione_l-1] = "H"

        else:
            percorso[posizione_l-1] = "OUCH!!!"

        tick += 1

        print(*percorso)

    if posizione_t == quadratini:             #verifico chi prima è arrivato al finish
        print("TORTOISE WINS! || VAY!!!")

    elif posizione_l == quadratini:
        print("HARE WINS || YUCH!!!")

    else:
        print("IT'S A TIE")
    

gara()
    
        

        

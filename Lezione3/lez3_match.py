'''
#Esercizio 3C-00A
print("Esercizio 3C-00A\n")

n = int(input(f"Inserisci un numero di neonati: \n"))
match n:
    case 1:
        print("Congratulazioni!\n")
    case 2:
        print("Wow! Gemelli!\n")
    case 3:
        print("Wow! Tre!\n")
    case 4:
        print("Mamma mia Quarto! Wow!\n")
    case 5:
        print("Incredibile! Cinque!\n")
    case _:
        print(f"Non ci credo! {n} bambini!\n")

'''

'''
#Esercizio 3C-00B
print("\nEsercizio 3C-00B\n")

nome:str = input(f"Inserisci il proprio nome: \n")
gen:str = input(f"Inserisci il suo genere (ez. \"m\" o \"f\"): \n")

match (nome, gen):
    case (x, "m"):
        print(f"{x}: gerene \"Maschio\"\n")
    case (y, "f"):
        print(f"{y}: genere \"Femmina\"\n")
    case _:
        print(f"\"Errore\" non è possibile generare un documento di identita\n")

'''

#Esercizio 3C-1
print("\nEsercizio 3C-1\n")

voto = int(input("Inserisci il voto numerico intero da 1 a 10: \n"))

match voto:
    case 8|9:
        print("Eccellente\n")
    case 6|7:
        print("Molto buono\n")
    case 4|5:
        print("Sufficiente\n")
    case 1|2|3:
        print("Gravemente insufficiente\n")
    case _:
        print("Voto no valido\n")
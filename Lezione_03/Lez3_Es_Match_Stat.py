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

'''

'''
#Esercizio 3C-2
print("\n Esercizio 3C-2 \n")

voto = int(input("Inserisci un voto di laurea italiano compreso tra 66 e 110: "))

match voto:
    case voto if voto >= 106 and voto <=110:
        print("Voto nel sistema GPA é 4.0\n")
    case voto if voto >= 101 and voto <=105:
        print("Voto nel sistema GPA é 3.7\n")
    case voto if voto >= 96 and voto <=100:
        print("Voto nel sistema GPA é 3.3\n")
    case voto if voto >=91 and voto <=95:
        print("Voto nel sistema GPA é 3.0\n")
    case voto if voto >= 86 and voto <=90:
        print("Voto nel sistema GPA é 2.7\n")
    case voto if voto >= 81 and voto <=85:
        print("Voto nel sistema GPA é 2.3\n")
    case voto if voto >= 76 and voto <=80:
        print("Voto nel sistema GPA é 2.0\n")
    case voto if voto >= 70 and voto <=75:
        print("Voto nel sistema GPA é 1.7\n")
    case voto if voto >= 66 and voto <=69:
        print("Voto nel sistema GPA é 1.0\n")
    case _:
        print("Voto non valido")

'''

#Esercizio 3C-3
print("\n Esercizio 3C-3\n")

oggetti:list = []

for i in range(3):
    x:str = input("Inserisci oggetto: ")
    oggetti.append(x)

print(f"\n La lista contiene: {oggetti}")

match oggetti:

    case ["penna", "matita", "quaderno"]:
        print("\n Materiale scolastico \n")

    case ["pane", "latte", "uova"]:
        print("\n Prodotti alimentari \n ")

    case ["sedia", "tavolo", "armadio"]:
        print("\n Mobili \n")

    case ["telefono","computer", "tablet"]:
        print("\n Dispositivi elettronici \n")

    case _:
        print("\n Categoria sconosciuta \n")

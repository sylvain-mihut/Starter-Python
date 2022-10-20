hauteur = int(input("Entrez la hauteur : "))
largeur = int(input("Entrez la largeur : "))

side = "|"
separator = "-"

for i in range(hauteur):
    if i == 0 or i == hauteur -1:
        separator = "-"
    else:
        separator = " "
    print(side + separator * largeur + side)
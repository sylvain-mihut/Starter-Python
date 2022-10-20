a = int(input("Entrez un premier nombre: "))

b = int(input("Entrez un second nombre: "))

if (a < b):
    for distance in range(a + 1, b):
        print(distance)
elif (a > b): 
    for distance in range(a - 1, b, -1):
        print(distance)

else:
    print("Les valeurs sont égales")
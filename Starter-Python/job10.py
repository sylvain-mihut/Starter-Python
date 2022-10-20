texte = str(input("Entrez votre texte ici : "))

f = open('output.txt','w')
f.write(texte)
f.close()

f = open('output.txt','r')
texte = f.read()
print(texte)
f.close()
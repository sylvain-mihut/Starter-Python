txt = open('data.txt','r')
result = txt.read()
words = result.split()

print("Nombre de mots dans le texte : ", len(words))
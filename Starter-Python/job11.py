f = open('domains.xml','r')
content = f.read()
print(content.count('name="domain"'))
f.close()
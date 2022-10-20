def fonction1(*argument):
    mylist = []

    for param in argument:
        if isinstance(param, (int)):
            mylist.append(param)
        else:
            print("Attention ce ne sont pas des chiffres")
    
    for element in mylist:
        if element % 2  == 0:
            print(element)
fonction1(9,3,8,18,14,92,54,67,36,6,4,1)
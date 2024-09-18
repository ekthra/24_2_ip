def animal():
    a = int(input('Me deixe advinhar seu animal favorito!\n[ 1 ] Se o animal for um réptil\n[ 2 ] Se o animal for um mamífero\n Digite um número:  '))
    if a == 1:
        print('Eu aposto que é uma tartaruga!')
    elif a == 2:
        print('Eu aposto que é um cachorro!')
    else:
        animal()
animal()



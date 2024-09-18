e = int(input('Escolha uma porta!\nPorta [ 1 ]\nPorta [ 2 ]\nPorta [ 3 ]\nPorta [ 4 ]\nPorta [ 5 ]\nFaça sua escolha:'))
match e:
        case 1:
            print('Você enfrentará um Dragão!!!')
        case 2:
            print('Você enfrentará um Goblin!!!')
        case 3:
            print('Você deve subir em uma corda de 100 metros!!!')
        case 4:
            print('Você deve domesticar um lobo filhote!!!')
        case 5:
            print('Você deve aprender Python!!!')
        case _:
            print('Escolha inválida.')


f = int(input('Escolha um feitiço!\n[ 1 ] Para um feitiço de fogo\n[ 2 ] Para um feitiço de água\n[ 3 ] Para um feitiço de terra\nSua escolha:'))
match f:
        case 1:
            print('Você escolheu Fogo!!!')
        case 2:
            print('Você escolheu Água!!!')
        case 3:
            print('Você escolheu Terra!!!')
        case _:
            print('Escolha inválida.')


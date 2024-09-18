e = int(input('Digite um número para posição do exército.\n[ 1 ]Fora do castelo\n[ 2 ]Dentro do castelo\nFaça sua escolha:'))
match e:
    case 1:
        print('O sistema do castelo permanece desativado.')
    case 2:
        print('O sistema de defesa do castelo está ativado!')
    case _:
        print('Escolha inválida.')

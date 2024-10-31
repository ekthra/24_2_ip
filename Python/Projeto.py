lista_de_compras = ['LAPIS','CANETA','CADERNO','LAPISEIRA']
print('-'*10, end='')
print('LISTA DE COMPRAS',end='')
print('-'*10, end='')


for c in range(len(lista_de_compras)):
                print(f'\n{c + 1}|{lista_de_compras[c]}')
                print('')

while True:

    escolha = str(input('Faça sua escolha:\nAdcionar item [A]\nRemover item [R]\nExibir lista [E]\nSair do programa [S]\nDigite aqui: ')).upper().strip()

    if escolha in 'ARES':

        if escolha in 'A':
            novo = str(input('Digite um novo item:')).upper().strip()
            lista_de_compras.append(novo)
        if escolha in 'E':
            
            print('-'*10, end='')
            print('LISTA DE COMPRAS',end='')
            print('-'*10, end='')
           
            for i in range(len(lista_de_compras)):
                print(f'\n{i + 1}|{lista_de_compras[i]}')
                print('')

        if escolha in 'R':
            print('-'*10, end='')
            print('LISTA DE COMPRAS',end='')
            print('-'*10, end='')
           
            for i in range(len(lista_de_compras)):
                print(f'\n{i + 1}|{lista_de_compras[i]}')
                print('')

            remover = int(input('Digite o número do item a ser removido: '))
            lista_de_compras.remove(lista_de_compras[remover - 1])

        if escolha in 'S':
            break
print('-'*10, end='')
print('PROGRAMA FINALIZADO',end='')
print('-'*10, end='')




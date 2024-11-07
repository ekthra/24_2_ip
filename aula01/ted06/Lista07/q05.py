numeros = int(input('Digite a quantidade de números que você deseja ver na senquência de Fibonnaci! '))
cont = 3
primeiro = 0
segundo = 1
terceiro = primeiro + segundo
if numeros == 1:
    print(primeiro)
        
elif numeros == 2:
    print(primeiro, segundo)

elif cont == 3:
    print('-> {} -> {} -> {} '.format(primeiro, segundo, terceiro), end='')
        
while cont != numeros:
    
    cont += 1
    primeiro = segundo
    segundo = terceiro
    terceiro = primeiro + segundo
    print('-> {} '.format(terceiro), end='')
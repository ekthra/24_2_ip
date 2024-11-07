altura = int(input('Digite a altura do triangulo:'))
print("Triângulo:")
for i in range(1, altura + 1):
    for j in range(i):
        print("*", end="")
    print()


lado = int(input('Digite o tamanho do quadrado:'))
print("\nQuadrado:")
for i in range(lado):
    for j in range(lado):
        print("*", end="")
    print()


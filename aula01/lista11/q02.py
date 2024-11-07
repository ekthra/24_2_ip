lista_notas = []
soma_media = 0
nota = 0
contador_acima = 0

for v in range(5):
    nota = float(input('Digite a nota do aluno(a): '))

    lista_notas.append(nota)

for notas in range(len(lista_notas)):

    nota = lista_notas[notas]
    soma_media += nota

soma_media = soma_media / 5

for i in range(len(lista_notas)):

    nota = lista_notas[i]

    if nota > soma_media:
        contador_acima += 1

print(f'{contador_acima} alunos receberam a nota maior que a média da turma.\nA média da turma é: {soma_media}')


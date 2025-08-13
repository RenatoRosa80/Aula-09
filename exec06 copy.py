"""
6.	Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

notas = []
alunos = 3
nmaior7 = 0

for i in range(alunos):
    soma = 0
    for j in range(4):
        nota = float(input(f"Informe a {j + 1}ª nota do {i + 1}º aluno: "))
        soma += nota
    media = soma / 4
    print(f" A média do {i+1}º aluno é: {media}")
    notas.append(media)

for i in range(alunos):
    if notas[i] >= 7:
        nmaior7 += 1

print(f"A quantidade de alunos com média maior ou igual a 7 foi: {nmaior7}")

    

    




    

        


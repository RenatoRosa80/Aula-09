"""
6.	Faça um Programa que peça as quatro notas de 10 alunos, calcule e 
armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""
alunos = 10
medias = []

for aluno in range(1, alunos + 1):
    notas = []
    print(f'\nNotas do {aluno}º Aluno: ')
    
    for i in range(1, 5):
        nota = float(input(f" Informe a {i}ª Nota: "))
        notas.append(nota)

    media = sum(notas) / 4
    medias.append(media)  # Guarda a média na lista

    print(f" Notas do ano letivo: {notas}")
    print(f" Média do {aluno}º Aluno: {media:.2f} ")

# Conta quantos alunos têm média >= 7
aprovados = sum(1 for m in medias if m >= 7.0)

print("\n==============================")
print(f"Total de alunos com média >= 7.0: {aprovados}")
print("==============================")



    




    

        


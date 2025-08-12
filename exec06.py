"""
6.	Faça um Programa que peça as quatro notas de 10 alunos, calcule e 
armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

alunos = 3

for aluno in range(1, alunos + 1):
    notas = []
    print(f'\n Nota do {aluno}º Aluno: ')
    
    
    for i in range(1, 5):
        
        nota = float(input(f" Informe a {i}ª Nota: "))
        notas.append(nota)

        #notas.append(nota)
    media = sum(notas) / 4
    print(f" Notas do ano letivo: {notas}")
    print(f" Média do {aluno}º Aluno: {media:.2f} ")
    
    



    




    

        


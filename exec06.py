"""
6.	Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

notas = []
alunos = 10
soma = media = 0
aluno = 0
nota = 0 
for i in range(4):
    print(f' Nota do {i+1}º Aluno')
    nota = float(input (f" Informe a {i+1}ª Nota: "))
   
    for j in range(3):
     
     nota = float(input (f" Informe a {j+2}ª Nota: "))
     notas.append(nota)
    
media = sum(notas) / 4
print(media)
    




    

        


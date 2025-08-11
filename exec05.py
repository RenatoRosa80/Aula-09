"""
5.	Faça um Programa que leia 10 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
 Imprima os três vetores.
"""
vetor = []
vetor_par = []
vetor_impar = []



for i in range(10):
    n = int(input(f" Informe o {i + 1}º número: "))
    vetor.append(n)
    if n %2 == 0:
        vetor_par.append(n)
    else:
        vetor_impar.append(n)
print(f" Números digitados foram: {vetor}")
print(f" Números digitados Ímpares foram: {vetor_impar}")
print(f" Números digitados Pares foram: {vetor_par}")




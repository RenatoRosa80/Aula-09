#2.	Faça um Programa que leia um vetor de 10 números reais e 
#mostre-os na ordem inversa.

# Criando a Lista


lista = []

for i in range (10):
    n = float(input(f'Digite o {i+1}º número da lista: '))
    lista.append(n)
    #lista.reverse() vira a lista ao contrário

for i in range (1):
    print(list(reversed(lista)))
        #também vira a lista ao contrário, porém mais objetivo
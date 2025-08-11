#1.	Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

# Criando a Lista
lista = []

# Entrando com os 5 números na lista

for i in range (0,5):
    l = int(input(f" Digite o {i + 1}º elemento da Lista: "))
    # Gravando os numeros na lista
    lista.append(l)
# Imprimir o conteudo da lista

for i in range (5):
    
    print(f" posição ----->{i} na lista, tem o conteudo {lista[i]} ")
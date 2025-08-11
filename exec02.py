#2.	Faça um Programa que leia um vetor de 10 números reais e 
#mostre-os na ordem inversa.

# Criando a Lista
lista = []


for i in range (10):
    l = float(input(f" Digite o {i + 1}º elemento da Lista: "))
    # Gravando os numeros na lista
    lista.append(l)
# Imprimir o conteudo da lista
lista.reverse()
for i in range (10):
    
    print(f" posição ----->{i} na lista, tem o conteudo {lista[i]:.0f} ")
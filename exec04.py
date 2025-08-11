#Faça um Programa que leia um vetor de 10 caracteres, 
#e diga quantas consoantes foram lidas. 
#Imprima as consoantes.
# Criando a Lista
lista = []
total = 0
vogais =  ['a','e','i','o','u']
consoantes = []

for i in range (10):
    letra = input(f" Digite o {i + 1}º elemento da Lista: ")
    # Gravando os numeros na lista
    lista.append(letra)
# Imprimir o conteudo da lista
    if letra.isalpha() and letra not in "aeiou":
        total += 1
        #print(f" Letra {list[i]}")
    if letra not in vogais:
        consoantes.append(letra)

    
print(f" Foi informado {total} Consoantes. ")
print(f" As consoantes informadas foram: {consoantes}")


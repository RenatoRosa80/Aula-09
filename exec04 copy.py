#Faça um Programa que leia um vetor de 10 caracteres, 
#e diga quantas consoantes foram lidas. 
#Imprima as consoantes.
# Criando a Lista
vetor = []

for i in range(10):
    letra = input(f'digite o {i+1}° caracteres:> ').lower()
    vetor.append(letra)

vogais = ['a', 'e', 'i', 'o', 'u']

consoantes = [letra for letra in vetor if letra and letra not in vogais]

print(f'quantidade de cosoantes: {len(consoantes)}')
print(f'consoantes lidas: {consoantes}')

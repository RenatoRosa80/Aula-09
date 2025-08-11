# 3.	Faça um Programa que leia 4 notas, mostre as notas e a média na tela.


notas = []

for i in range(4):
    nota = float(input (f" Informe a {i+1}ª Nota: "))
  
    notas.append(nota)

media = sum(notas) / 4
print(f" Sua média foi: {media:.2f} ")


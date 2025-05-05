# 13.Escreva um programa que receba a idade de uma pessoa e o preço de um ingresso (inteiros). Aplique descontos: 50% para menores de 12 anos, 30% para maiores de 60 anos, 10% para estudantes (pergunte se é estudante com 'S' ou 'N'). Imprima o preço final.

idade = int(input("Digite a sua idade: "))
preco_ingresso = int(input("Digite o preço do ingresso: "))

estudante = (input("Você é estudante? (S/N): "))

if idade < 12:
    desconto = 0.50
elif idade > 60:
    desconto = 0.30
elif estudante == 'S':
    desconto = 0.10
else:
    desconto = 0

preco_final = preco_ingresso * (1 - desconto)

print(f"O preço final do ingresso é: R${preco_final:.2f}")

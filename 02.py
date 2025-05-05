#2. Crie um programa que receba dois números como entrada e imprima sua soma, diferença, produto e divisão.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
diferenca = num1 - num2
produto = num1 * num2
divisao = num1 / num2

print(f"Soma: {soma:.2f}")
print(f"Diferença: {diferenca:.2f}")
print(f"Produto: {produto:.2f}")
print(f"Divisão: {divisao:.2f}")

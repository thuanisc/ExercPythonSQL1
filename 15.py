#15.Escreva um programa que receba dois números inteiros e uma operação (+, -, *, /) como string. Use if-elif-else para realizar a operação escolhida e imprimir o resultado. Trate divisão por zero.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} é: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} é: {resultado}")
elif operacao == "/":
    if num2 == 0:
        print("Erro! Divisão por zero não é permitida.")
    else:
        resultado = num1 / num2
        print(f"O resultado de {num1} / {num2} é: {resultado}")
else:
    print("Operação inválida! Digite uma operação válida (+, -, *, /).")

# 18.Crie um while que peça números inteiros até que o usuário digite um número negativo. Armazene os números pares em uma lista e imprima a lista e a média dos números pares

numeros_pares = []

numero = 0
while numero >= 0:
    numero = int(input("Digite um número inteiro (ou um número negativo para sair): "))

    if numero>=0 and numero%2 == 0:
        numeros_pares.append(numero)

print("Lista de números pares:", numeros_pares)

if numeros_pares:
    media = sum(numeros_pares)/len(numeros_pares)
    print(f"A média dos números pares é: {media}")
else:
    print("Nenhum número par foi inserido. Saindo.")


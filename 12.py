#12.Escreva um programa que crie uma lista de 3 números (inseridos pelo usuário), ordene-os e imprima a lista ordenada.

numeros = []

for i in range(3): #loopings de 3 repetições
    numero_posicao = i+1
    numero = float(input(f"Digite o {numero_posicao}º número: "))
    numeros.append(numero)

numeros.sort() #ordem crescente
print("Lista ordenada:", numeros)

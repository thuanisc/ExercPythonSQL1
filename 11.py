#11.Crie uma tupla com as 4 estações do ano e imprima cada estação com seu índice.

estacoes = ("Primavera", "Verão", "Outono", "Inverno")

for indice, estacao in enumerate(estacoes):
    print(f"A estação {estacao} está no índice {indice}")

#opção 2 - usando range
for i in range(4):
    print(estacoes[i])
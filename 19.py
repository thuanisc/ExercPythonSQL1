#19.Use um for para iterar sobre um dicionário com 5 produtos e seus preços. Imprima apenas os produtos com preço maior que 20 em uma frase como "[Produto] custa [preço]."

produtos = {"Arroz": 18.50, "Feijão": 25.00, "Camiseta": 35.90, "Celular": 1200.00, "Caderno": 15.00}

for produto, preco in produtos.items():
     if preco>20:
        print(f"{produto} custa {preco}.")

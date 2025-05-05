#16.Use match case para receber o nome de um mês (janeiro, fevereiro, etc.) e imprimir o número de dias (considere 28 para fevereiro). Para meses inválidos, imprima "Mês inválido".

mes = input("Digite algum mês do ano: ")
mes = mes.lower()

match mes:
    case "janeiro" | "março" | "maio" | "julho" | "agosto" | "outubro" | "dezembro":
        print(f"{mes.capitalize()} tem 31 dias.")
    case "fevereiro":
        print(f"Fevereiro tem 28 dias.")
    case "abril" | "junho" | "setembro" | "novembro":
        print(f"{mes.capitalize()} tem 30 dias.")
    case _:
        print("Mês inválido.")

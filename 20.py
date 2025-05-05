#20.Escreva um while que simule um jogo onde o usuário tenta adivinhar um número entre 1 e 10 (fixo, como 7). Dê dicas ("Muito alto" ou "Muito baixo") e pare quando acertar, imprimindo o número de tentativas.

numero_correto = 7
tentativas = 0

while True:
    palpite = int(input("Tente adivinhar o número entre 1 e 10: "))
    tentativas += 1

    if palpite == numero_correto:
        print(f"Parabéns! Você acertou o número {numero_correto} em {tentativas} tentativas.")
        break  # Sai do laço quando acertar
    elif palpite < numero_correto:
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")

#8. Escreva um programa que receba uma string como entrada e verifique se seu tamanho é maior que 5, armazenando o resultado em uma variável booleana, depois imprima a string e o booleano

texto = input("Digite algo: ")
tem_mais_de_5 = len(texto)>5

print(f"Você digitou: {texto}")
print(f"A string tem mais de 5 caracteres? {tem_mais_de_5}")

#opção 2 - se quiser especificar mais
tamanho_texto = len(texto)
tem_mais_de_5 = None

if tamanho_texto > 5:
    tem_mais_de_5 = True
else:
    tem_mais_de_5 = False

print("O texto é", texto, " e o boolean é", tem_mais_de_5)
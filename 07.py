#7. Declare uma variável booleana que verifica se um número (entrada como inteiro) é par, depois imprima o número e o resultado booleano.

numero = int(input("Digite um número inteiro: "))
eh_par = (numero % 2 == 0)

print(f"O número digitado foi: {numero}")
print(f"O número é par? {eh_par}")

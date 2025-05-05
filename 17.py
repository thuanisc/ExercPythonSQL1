#17.Escreva um programa que use um for para encontrar e imprimir todos os números de 1 a 50 que são divisíveis por 3 e 5 ao mesmo tempo.

for num in range(1, 51):
   if num%3==0 and num%5==0:
        print(num)

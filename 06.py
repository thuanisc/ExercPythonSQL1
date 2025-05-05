#6. Crie um programa que converta uma temperatura de Celsius (entrada como float) para Fahrenheit usando a fórmula F = C * 9/5 + 32 e imprima o resultado.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius * 9 / 5 + 32

print(f"{celsius:.1f}°C equivalem a {fahrenheit:.1f}°F")

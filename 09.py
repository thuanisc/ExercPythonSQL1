#9. Crie uma lista com 5 frutas, adicione uma nova fruta, remova uma e imprima a lista final.

frutas = ["maçã", "banana", "laranja", "uva", "melancia"]


frutas.append("abacaxi")
frutas.remove("banana") #ou frutas.pop(1)

print("Lista final de frutas:")
print(frutas)

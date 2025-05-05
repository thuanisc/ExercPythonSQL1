#14.Crie um programa que receba um código de produto (1 a 5) e imprima a categoria usando match case: 1 = Eletrônicos, 2 = Roupas, 3 = Alimentos, 4 = Livros, 5 = Brinquedos, outros = "Código inválido"

codigo_produto = int(input("Digite o código do produto (1 a 5): "))

match codigo_produto:
    case 1:
        print("Categoria: Eletrônicos")
    case 2:
        print("Categoria: Roupas")
    case 3:
        print("Categoria: Alimentos")
    case 4:
        print("Categoria: Livros")
    case 5:
        print("Categoria: Brinquedos")
    case _:
        print("Código inválido")

#5. Declare uma variável string com o nome da sua cidade, um inteiro com seu ano de nascimento, um float com sua altura em metros e um booleano indicando se você gosta de programar. Imprima todas as variáveis com mensagens descritivas

cidade = "Biguaçu"
ano_nascimento = 1995
altura = 1.73
gosta_de_programar = True

print(f"Moro na cidade de {cidade}. \n"
      f"Nasci no ano de {ano_nascimento}. \n"
      f"Minha altura é de {altura} metros. \n"
      f"É verdade que gosto de programar? {'Gosto' if gosta_de_programar else 'Não gosto'}.")

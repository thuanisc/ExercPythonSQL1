#10.Faça um dicionário com 3 nomes de alunos como chaves e suas notas como valores. Imprima cada aluno e sua nota em uma frase.

notas_alunos = {"Ana": 8.5, "Bruno": 7.0, "Carla": 9.2}

for aluno, nota in notas_alunos.items():
    print(f"O aluno {aluno} tirou nota {nota}")

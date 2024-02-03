def main():
    num_alunos = int(input("Quantos alunos você quer inserir? "))

    alunos = []
    for _ in range(num_alunos):
        nome = input("Digite o nome do aluno: ")
        notas = [float(input(f"Digite a nota {j + 1} de {nome}: ")) for j in range(3)]
        media_aluno = sum(notas) / 3
        alunos.append({"nome": nome, "media": media_aluno})

    media_turma = sum(aluno["media"] for aluno in alunos) / num_alunos

    print("\nResultados:")
    for aluno in alunos:
        print(f"\nNome: {aluno['nome']} | Média do Aluno: {aluno['media']}")

    print(f"\nMédia da Turma: {media_turma}")

if __name__ == "__main__":
    main()
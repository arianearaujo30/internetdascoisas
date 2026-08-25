notas = []

# Leitura das 8 notas
print("Digite a nota dos 8 alunos:")
for i in range(8):
    nota = float(input(f"Nota do aluno {i + 1}: "))
    notas.append(nota)

# 1. Cálculo da média da turma
media = sum(notas) / len(notas)
print(f"\nMédia da turma: {media:.2f}")

# 2. Criação da lista com notas acima da média
notas_acima_media = [nota for nota in notas if nota > media]

print(f"Notas acima da média: {notas_acima_media}")
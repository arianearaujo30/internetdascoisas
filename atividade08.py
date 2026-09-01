notas = []

print("--- CADASTRO DE NOTAS ---")
print("Digite as notas uma por uma. Digite -1 para finalizar.\n")

while True:
    nota = float(input("Digite a nota (ou -1 para encerrar): "))
    
    if nota == -1:
        break
        
    notas.append(nota)

    if len(notas) > 0:
    
     print("\n--- NOTAS CADASTRADAS ---")
    for i, n in enumerate(notas, start=1):
        print(f"Nota {i}: {n}")
        quantidade = len(notas)
    soma = sum(notas)
    media = soma / quantidade
    maior_nota = max(notas)
    menor_nota = min(notas)

    notas.sort(reverse=True)

    print("\n--- RESULTADOS FINAIS ---")
    print(f"Quantidade de notas cadastradas: {quantidade}")
    print(f"Média da turma: {media:.2f}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")
    print(f"Notas em ordem decrescente: {notas}")
else:
    print("\nNenhuma nota foi cadastrada.")
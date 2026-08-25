nomes = []

# Leitura dos 10 nomes
print("Digite 10 nomes:")
for i in range(10):
    nome = input(f"Nome {i + 1}: ")
    nomes.append(nome)

# Sorteio do nome
nome_sorteado = random.choice(nomes)

print(f"\nO nome sorteado foi: {nome_sorteado}")
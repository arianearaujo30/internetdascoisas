nomes = []

# Leitura dos 5 nomes
print("Digite 5 nomes:")
for i in range(5):
    nome = input(f"Nome {i + 1}: ")
    nomes.append(nome)

# Ordenação da lista
nomes.sort()

# Exibição dos nomes ordenados
print("\nNomes em ordem alfabética:")
for nome in nomes:
    print(f"- {nome}")
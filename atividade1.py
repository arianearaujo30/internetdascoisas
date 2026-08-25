numeros = []
negativos = []
soma_positivos = 0
qtd_positivos = 0
qtd_negativos = 0

# Leitura dos 10 números
print("Digite 10 números:")
for i in range(10):
    num = float(input(f"Número {i + 1}: "))
    numeros.append(num)
    
    if num > 0:
        qtd_positivos += 1
        soma_positivos += num
    elif num < 0:
        qtd_negativos += 1
        negativos.append(num)

# Exibição dos resultados
print("\n--- Resultados ---")
print(f"Quantidade de números positivos: {qtd_positivos}")
print(f"Quantidade de números negativos: {qtd_negativos}")
print(f"Vetor com os números negativos: {negativos}")
print(f"Soma dos números positivos: {soma_positivos}")
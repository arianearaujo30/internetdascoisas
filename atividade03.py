numeros=[]

for i in range(6):
    numeros=int(input(f"Digite o {i+1}° número inteiro:"))
    numeros.append(numeros)

    numeros.sort()

    print("\n---Resultados---")
    print("Soma de todos os números:", sum(numeros))
    print("Maior valor:", max(numeros))
    print("Menor valor:", min(numeros))
    print("Números em ordem crescente:", numeros)
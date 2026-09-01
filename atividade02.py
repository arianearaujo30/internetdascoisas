produto=[]

for i in range(5):
    produto=input(f"Digite o nome do produto{i+1}: ")
    produto.append(produto)

    print("\nLista de produtos cadastrados:", produto)
    print("Quantidade total de produtos:", len(produto))
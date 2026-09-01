convidados=[]

while True:
    nome = input("Digite o nome do convidado(ou 'fim' para encerrar):")
    if nome.lower()=='fim':
        break
    convidados.append(nome)

    convidados.sort()

    print("\n---Lista de convidados---")
    print("Convidados(ordem alfabética):", convidados)
    print("quantidade total de convidados:",len(convidados))
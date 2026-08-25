while True:
    senha = input("Digite uma senha de 4 dígitos numéricos: ")
    
    # Verifica se tem exatamente 4 caracteres e se é formada apenas por números
    if len(senha) == 4 and senha.isdigit():
        print("Senha cadastrada com sucesso!")
        break
    else:
        print("Senha Inválida. Tente novamente.\n")
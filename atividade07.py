import random

# 1. Sorteio do número secreto entre 1 e 20
numero_secreto = random.randint(1, 20)
tentativas = 0

print("--- JOGO DE ADIVINHAÇÃO ---")
print("Tente adivinhar o número entre 1 e 20!")

# 2. Laço para pedir palpites
while True:
    palpite = int(input("\nDigite o seu palpite: "))
    tentativas += 1  # Incrementa o contador de tentativas
    
    if palpite == numero_secreto:
        print(f" Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativa(s)!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é MAIOR.")
    else:
        print("O número secreto é MENOR.")
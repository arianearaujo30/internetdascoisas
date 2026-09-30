import customtkinter as ctk

ctk.set_appearance_mode("dark")


# Função para calcular a média
def calcular_media():
    try:
        nota_1 = float(nota1.get())
        nota_2 = float(nota2.get())
        nota_3 = float(nota3.get())

        media_final = (nota_1 + nota_2 + nota_3) / 3

        if media_final > 5.0:
            resultado_final = "Aprovado"
        else:
            resultado_final = "Recuperação"

        media.configure(text=f"Média Final: {media_final:.2f}")
        resultado.configure(text=f"Resultado: {resultado_final}")

    except ValueError:
        media.configure(text="Média Final: -")
        resultado.configure(text="Digite apenas números!")


# Criando a janela
janela = ctk.CTk()
janela.title("Sistema Escolar 2026")
janela.geometry("600x450")

# Se o arquivo do ícone estiver na mesma pasta:
# janela.iconbitmap("ic_school_128_28729.ico")


# Título
titulo = ctk.CTkLabel(
    janela,
    text="Sistema Escolar",
    text_color="#d6e41d",
    font=("Arial", 30)
)
titulo.pack(pady=20)


# Campo da 1ª unidade
nota1 = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    placeholder_text="Digite a sua nota da 1ª Unidade"
)
nota1.pack(pady=10)


# Campo da 2ª unidade
nota2 = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    placeholder_text="Digite a sua nota da 2ª Unidade"
)
nota2.pack(pady=10)


# Campo da 3ª unidade
nota3 = ctk.CTkEntry(
    janela,
    width=400,
    height=40,
    placeholder_text="Digite a sua nota da 3ª Unidade"
)
nota3.pack(pady=10)


# Botão
botao = ctk.CTkButton(
    janela,
    width=200,
    height=40,
    text="Calcular Média",
    fg_color="#d6e41d",
    text_color="black",
    font=("Arial", 12),
    command=calcular_media
)
botao.pack(pady=15)


# Exibe a média
media = ctk.CTkLabel(
    janela,
    text="Média Final:",
    text_color="white",
    font=("Arial", 20)
)
media.pack(pady=5)


# Exibe o resultado
resultado = ctk.CTkLabel(
    janela,
    text="Resultado:",
    text_color="white",
    font=("Arial", 20)
)
resultado.pack(pady=5)


# Inicia o programa
janela.mainloop()  ,
  
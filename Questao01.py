import customtkinter as ctk

ctk.set_appearance_mode('dark')

#Media = (nota1+nota2)/2
#media < 5 = Reprovado
#media >= 5 e < 6.9 = Recuperação
#media >= 7 = Aprovado
#O cálculo deverá ser realizado dentro de u8ma função chamada botão
def calcular_media():
    try:
        nota1 = float(nota1_entry.get())
        nota2 = float(nota2_entry.get())
        
        media = (nota1 + nota2) / 2
        
        if media < 5:
            resultado = f"Reprovado! Média: {media:.2f}"
        elif media < 7:
            resultado = f"Recuperação! Média: {media:.2f}"
        else:
            resultado = f"Aprovado! Média: {media:.2f}"
        
        resultado_label.configure(text=f"Resultado Final: {resultado}")
        
    except ValueError:
        resultado_label.configure(text="Erro: Digite notas numéricas válidas.")
        
        #Criando a janela principal
janela = ctk.CTk()
janela.title("Resultado Acadêmico 2026")
janela.geometry("600x550")
janela.iconbitmap("ic_school_128_28729.ico")

# Título
titulo = ctk.CTkLabel(
    janela,
    text="Resultado Acadêmico",
    text_color="#1da8e4",
    font=("Arial", 30)
)
titulo.pack(pady=20)

# Entrada: Nome do Aluno
nome_label = ctk.CTkLabel(
    janela,
    text="Nome do Aluno:",
    text_color="#1da8e4",
    font=("Arial", 30)
)
nome_label.pack(pady=10)
nome_entry = ctk.CTkEntry(
    janela,
    placeholder_text="Digite o nome do aluno"
)
nome_entry.pack(pady=10)

# Entrada: Primeira Nota
nota1_label = ctk.CTkLabel(
    janela,
    text="Primeira Nota:",
    text_color="#1da8e4",
    font=("Arial", 30)
)
nota1_label.pack(pady=10)
nota1_entry = ctk.CTkEntry(
    janela,
    placeholder_text="Digite a primeira nota"
)
nota1_entry.pack(pady=10)

# Entrada: Segunda Nota
nota2_label = ctk.CTkLabel(
    janela,
    text="Segunda Nota:",
    text_color="#1da8e4",
    font=("Arial", 30)
)
nota2_label.pack(pady=10)
nota2_entry = ctk.CTkEntry(
    janela,
    placeholder_text="Digite a segunda nota"
)
nota2_entry.pack(pady=10)

# Botão de Ação
botao = ctk.CTkButton(  
    janela,
    text="Calcular Resultado",
    fg_color="#1da8e4",
    text_color="white",
    font=("Arial", 18),
    command=calcular_media
)
botao.pack(pady=20) 

#Exibir media
media= ctk.CTkLabel(
    janela,
    text="Média: -",
    text_color="#1da8e4",
    font=("Arial", 30)
)
media.pack(pady=10)

# Exibição de Resultados
resultado_label = ctk.CTkLabel(
    janela,
    text="Resultado Final: -",
    text_color="#1da8e4",
    font=("Arial", 30)
)
resultado_label.pack(pady=10)

# Inicia o loop principal da interface
janela.mainloop()
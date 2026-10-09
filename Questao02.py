import customtkinter as ctk

ctk.set_appearance_mode("dark")

def calcular_hospedagem():
    try:
        quantidade_diarias = int(diarias_entry.get())
        valor_diaria = float(valor_entry.get())
        
        valor_hospedagem = quantidade_diarias * valor_diaria
        
        if quantidade_diarias > 5:
            desconto = valor_hospedagem * 0.10
        else:
            desconto = 0.0
        
        total_a_pagar = valor_hospedagem - desconto
        
        resultado_label.configure(text=f"Valor da Hospedagem: R${valor_hospedagem:.2f}\nDesconto: R${desconto:.2f}\nTotal a Pagar: R${total_a_pagar:.2f}")
        
    except ValueError:
        resultado_label.configure(text="Erro: Digite valores numéricos válidos para diárias e valor da diária.")
        
#Criando a janela
janela = ctk.CTk()
janela.title("Cálculo de Hospedagem")
janela.geometry("600x400")
janela.iconbitmap("1497618989-3_85123.ico")

# Título
titulo = ctk.CTkLabel(
    janela,
    text="Cálculo de Hospedagem",
    text_color="#1da8e4",
    font=("Verdana", 28)
)
titulo.pack()

# Entrada: Quantidade de Diárias
diarias_label = ctk.CTkLabel(
    janela,
    text="Quantidade de Diárias:",
    text_color="#1da8e4",
    font=("Verdana", 16)
)
diarias_label.pack(pady=10)
diarias_entry = ctk.CTkEntry(
    janela,
    width=200,
    height=30,
    placeholder_text="Digite a quantidade de diárias"
)
diarias_entry.pack(pady=5)

# Entrada: Valor da Diária
valor_label = ctk.CTkLabel(
    janela,
    text="Valor da Diária (R$):",
    text_color="#1da8e4",
    font=("Verdana", 16)
)
valor_label.pack(pady=10)
valor_entry = ctk.CTkEntry(
    janela,
    width=200,
    height=30,
    placeholder_text="Digite o valor da diária"
)
valor_entry.pack(pady=5)

# Botão de Ação]
botao = ctk.CTkButton(
    janela,
    text="Calcular",
    fg_color="#1da8e4",
    text_color="white",
    font=("Verdana", 16),
    command=calcular_hospedagem
)
botao.pack(pady=20)

# Exibição de Resultados
resultado_label = ctk.CTkLabel(
    janela,
    text="",
    text_color="#1da8e4",
    font=("Verdana", 16)
)
resultado_label.pack(pady=10)


# Inicia o loop principal da interface
janela.mainloop()
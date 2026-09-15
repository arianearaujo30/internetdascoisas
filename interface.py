import customtkinter as ctk
ctk.set_appearance_mode('dark')


#janela ---------
janela = ctk.CTk()
janela.geometry('500x500')
janela.title('Sistema de Acesso-2026')
janela.iconbitmap('cslogin_104358.ico')

#------------------------------------

# corpo da janela --------------------------------

titulo = ctk.CTkLabel(janela,
    text='Sistema de login',
    text_color='#8cc5e6',
    font=('Arial',50)
)
titulo.pack()


login=ctk.CTkEntry(janela,
                width=400,
                height=40,
                border_color='#8cc5e6',
                placeholder_text='Digite o seu Login')
login.pack(pady=30)





senha=ctk.CTkEntry(janela,
                width=400,
                height=40,
                border_color='#8cc5e6',
                placeholder_text='Digite a sua Senha',
                show='•')
senha.pack()

botao = ctk.CTkButton(janela,
                width= 200,
                height=40,
                text ='Acessar',
                fg_color='#8cc5e6',
                text_color='black',
                cursor = 'spider',
                font=('arial',30))

botao.pack(pady=30)







janela.mainloop()


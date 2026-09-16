import customtkinter as ctk
ctk.set_appearance_mode('dark')



#funções-------------------

def calcular():
    d= int(distancia.get())
    v= float(veiculo.get())
    c= float(combustivel.get())

    formula= (d/v)*c
    resultado.configure(text=f'O valor para a viagem é de R$ {formula:.2f}')


#janela-------------
janela= ctk.CTk()
janela.geometry('500x500')
janela.title('Calculadora de Viagem')
janela.iconbitmap('world_travel_icon_134812.ico')

#-----------------------------------

#Corpo da janela-----------------------


titulo= ctk.CTkLabel(janela,
                    text='APP DE VIAGEM',
                    text_color='#bc75eb',
                    font=('Verdana',30)
                    )
titulo.pack()


distancia=ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#bc75eb',
                    placeholder_text='Digite a distância da viagem em KM')
distancia.pack(pady=30)




veiculo=ctk.CTkEntry(janela,
                    width=400,
                    height=40,
                    border_color='#bc75eb',
                    placeholder_text='Digite o consumo do seu veiculo')
veiculo.pack()



combustivel=ctk.CTkEntry(janela,
                        width=400,
                        height=40,
                        border_color='#bc75eb',
                        placeholder_text='Digite o preço atual do combustivel')
combustivel.pack(pady=30)


botao = ctk.CTkButton(janela,
                width= 200,
                height=20,
                text ='Calcular Gasto',
                fg_color='#bc75eb',
                text_color='black',
                cursor = 'spider',
                font=('Verdana',10),
                command=calcular)
botao.pack(pady=10)


resultado=ctk.CTkLabel(janela,
                        text='',
                        text_color='white',
                        font=('Arial',20))
resultado.pack(pady=10)

janela.mainloop()

for x in range(60):
    
    if(x%2==0): 
        print(x)
        


while true: 
    print('Lucas')
    
    
carrinho = []

while true:
    produto = float(input('Digite o valor do produto:'))
    if(produto == 0):
        break
    else:
        carrinho.append(produto)
        
total = sum(carrinho)
print(f'O valor total da compra é R$ {total:.2f}')

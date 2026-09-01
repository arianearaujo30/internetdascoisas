tarefas=[]

while True:
    print("\n--Menu de tarefas---")
    print("1-Adicionar tarefas")
    print("2-Remover tarefas")
    print("4-Mostrar tarefas")
    print("0-Sair")

    opcao=input("Escolha uma opção:")
    if opcao == '1':
        nova_tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")
        
    elif opcao == '2':
        if len(tarefas) == 0:
            print("A lista está vazia! Nenhuma tarefa para remover.")
        else:
            tarefa_remover = input("Digite o nome exato da tarefa a ser removida: ")
            if tarefa_remover in tarefas:
                tarefas.remove(tarefa_remover)
                print(f"Tarefa '{tarefa_remover}' removida com sucesso!")
            else:
                print("Tarefa não encontrada na lista!")
                
    elif opcao == '3':
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada até o momento.")
        else:
            print("\nLista de Tarefas:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")
                
    elif opcao == '0':
        print("Saindo do gerenciador de tarefas... Até logo!")
        break
        
    else:
        print("Opção inválida! Tente novamente.")

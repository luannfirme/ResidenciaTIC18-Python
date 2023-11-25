import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_path = os.path.join(diretorio_atual, "tarefas.txt")

def carregar_tarefas():
    try:
        with open(arquivo_path, "r") as arquivo:
            linhas = arquivo.readlines()
            tarefas = []
            for linha in linhas:
                id_tarefa, descricao, concluida = linha.strip().split("|")
                tarefa = {"ID": int(id_tarefa), "Descricao": descricao, "Concluida": concluida == "True"}
                tarefas.append(tarefa)
            return tarefas
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas):
    with open(arquivo_path, "w") as arquivo:
        for idx, tarefa in enumerate(tarefas, start=1):
            checkbox = "[x]" if tarefa["Concluida"] else "[ ]"
            arquivo.write(f"{tarefa['ID']}   |   {tarefa['Descricao']}   |   {checkbox}\n")
            


tarefas = carregar_tarefas()
proximo_id = len(tarefas) + 1 if tarefas else 1


def adicionar_tarefa(descricao):
    if descricao[0].islower():
        descricao = descricao.capitalize()

    for tarefa in tarefas:
        if tarefa["Descricao"].lower() == descricao.lower():
            print("\nEsta tarefa já está cadastrada!")
            return

    tarefas.append({"ID": proximo_id, "Descricao": descricao, "Concluida": False})
    salvar_tarefas(tarefas)
    print("\nTarefa registrada!!!")
    


def marcar_tarefa_realizada(id):
    if id > len(tarefas) or id <= 0:
        print("\nTarefa não encontrada ou identificador invalido.")
    else:
        index = id - 1
        if not tarefas[index]["Concluida"]:
            tarefas[index]["Concluida"] = True
            tarefa_concluida = tarefas.pop(index)
            tarefas.insert(0, tarefa_concluida)
            salvar_tarefas(tarefas)
            print("\nTarefa marcada como realizada!!!")
        else:
            print("\nEsta tarefa ja foi realizada anteriormente.")


def editar_tarefa(id):
    if id > len(tarefas) or id <= 0:
        print("\nTarefa não encontrada ou identificador invalido.")
    else:
        index = id - 1
        nova_descricao = input("Digite a nova descricao da tarefa: ").capitalize()
        tarefas[index]["Descricao"] = nova_descricao
        salvar_tarefas(tarefas)
        print(f"\nTarefa {id} editada !!!")


def exibir_tarefas():
    print("\nLista de Tarefas:")
    for idx, tarefa in enumerate(tarefas, start=1):
        checkbox = "[x]" if tarefa["Concluida"] else "[ ]"
        print(f"{idx} => |   {tarefa['ID']}   |   {tarefa['Descricao']}   |   {checkbox}    |\n")

while True:
    print("\n== Menu ==")
    print("1. Adicionar tarefa")
    print("2. Marcar tarefa como realizada")
    print("3. Editar tarefa")
    print("4. Exibir tarefas")
    print("0. Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        descricao = input("Digite a descricao da tarefa: ")
        adicionar_tarefa(descricao)
    elif opcao == "2":
        id_tarefa = int(input("Digite o ID da tarefa realizada: "))
        marcar_tarefa_realizada(id_tarefa)
    elif opcao == "3":
        id_tarefa = int(input("Digite o ID da tarefa que sera editada: "))
        editar_tarefa(id_tarefa)
    elif opcao == "4":
        exibir_tarefas()
    elif opcao == "0":
        break
    else:
        print("Opcao invalida. Por favor, escolha uma opcao valida.")
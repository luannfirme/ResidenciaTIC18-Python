produtos = []

def inserir_produto():
    while True:
        codigo = input("Digite o código do produto (13 caracteres numéricos): ")
        if codigo.isdigit() and len(codigo) <= 13 and len(codigo) > 0:
            break
        print("O código deve ter aé 13 caracteres numéricos.")

    nome = input("Digite o nome do produto: ").capitalize()

    while True:
        try:
            preco = float(input("Digite o preço do produto: ").replace(',', '.'))
            break
        except ValueError:
            print("Formato de preço inválido. Use números.")

    produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": f'{preco:.2f}'
    }

    produtos.append(produto)
    print("Produto inserido com sucesso!")

def excluir_produto():
    codigo = input("Digite o código do produto a ser removido: ")

    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            return

    print("Produto não encontrado.")

def listar_produtos():
    produtos_ordenados = sorted(produtos, key=lambda x: float(x['preco']))
    itens_por_pagina = 10
    pagina_atual = 0

    while True:
        pagina = produtos_ordenados[pagina_atual * itens_por_pagina:(pagina_atual + 1) * itens_por_pagina]
        for produto in pagina:
            print(f"Código: {produto['codigo']} | Nome: {produto['nome']} | Preço: R${produto['preco']}")

        print("\nOpções:")
        print("1. Próxima página")
        print("2. Página anterior")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            if (pagina_atual + 1) * itens_por_pagina < len(produtos_ordenados):
                pagina_atual += 1
            else:
                print("Você está na última página.")
        elif opcao == "2":
            if pagina_atual > 0:
                pagina_atual -= 1
            else:
                print("Você está na primeira página.")
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")


def consultar_preco():
    codigo = input("Digite o código do produto para consultar o preço: ")

    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"O preço do produto {produto['nome']} é R${produto['preco']}")
            return

    print("Produto não encontrado.")
    
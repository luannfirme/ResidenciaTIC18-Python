from Supermecado.supermercado import inserir_produto, excluir_produto, listar_produtos, consultar_preco

def main():
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1. Inserir novo produto")
        print("2. Excluir produto")
        print("3. Listar produtos")
        print("4. Consultar preço")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            inserir_produto()
        elif opcao == "2":
            excluir_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            consultar_preco()
        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
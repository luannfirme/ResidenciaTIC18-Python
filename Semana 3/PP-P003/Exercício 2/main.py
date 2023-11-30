from Empregados.empregado import carregar_funcionarios, Reajusta_dez_porcento, adicionar_funcionario

def main():
    
    while True:
        print("\n==== MENU PRINCIPAL ====")
        print("1. Cadastrar Funcionário")
        print("2. Reajustar Salários (10%)")
        print("3. Listar Funcionários")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            adicionar_funcionario()
            
        elif opcao == "2":
            lista_empregados = carregar_funcionarios()
            Reajusta_dez_porcento(lista_empregados)
            print("\nSalários depois do reajuste:")
            for empregado in lista_empregados:
                print(f"Nome: {empregado['nome']} {empregado['sobrenome']} RG: {empregado['RG']}  Nascido em: {empregado['ano_nascimento']} Admitido em: {empregado['ano_admissao']}  : R$ {empregado['salario']:.2f}")
                
        elif opcao == "3":
            print("Funcionários cadastrados:")
            lista_empregados = carregar_funcionarios()
            for empregado in lista_empregados:
                print(f"Nome: {empregado['nome']} {empregado['sobrenome']} RG: {empregado['RG']}  Nascido em: {empregado['ano_nascimento']} Admitido em: {empregado['ano_admissao']}  : R$ {empregado['salario']:.2f}")

        elif opcao == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_path = os.path.join(diretorio_atual, 'dados_empregados.txt')

def carregar_funcionarios():
    lista_empregados = []
    with open(arquivo_path, 'r') as file:
        for line in file:
            dados = line.strip().split(',')
            empregado = {
                'nome': dados[0],
                'sobrenome': dados[1],
                'ano_nascimento': int(dados[2]),
                'RG': dados[3],
                'ano_admissao': int(dados[4]),
                'salario': float(dados[5])
            }
            lista_empregados.append(empregado)
    return lista_empregados

def salvar_funcionarios(funcionarios):
    with open(arquivo_path, "w") as arquivo:
        for idx, funcionario in enumerate(funcionarios, start=1):
            arquivo.write(f"{funcionario['nome']},{funcionario['sobrenome']},{funcionario['ano_nascimento']},{funcionario['RG']},{funcionario['ano_admissao']},{funcionario['salario']}\n")
            


funcionarios = carregar_funcionarios()

def adicionar_funcionario():
    
    nome = input("Digite o nome: ").capitalize()
    sobrenome = input("Digite o sobrenome: ").capitalize()
    
    while True:
        anoNascimento = input("Digite o ano de nascimento: ")
        if anoNascimento.isdigit():
            break
        print("O ano de nascimento deve ser caracteres numéricos.")
          
    while True:
        rg = input("Digite o RG: ")
        if rg.isdigit():
            break
        print("O RG deve ser caracteres numéricos.")
    
    while True:
        anoAdimisao = input("Digite o ano de admissão: ")
        if anoAdimisao.isdigit():
            break
        print("O ano de admissão deve ser caracteres numéricos.")
    
    while True:
        try:
            salario = float(input("Digite o salário: ").replace(',', '.'))
            break
        except ValueError:
            print("Formato de salário inválido. Use números.")
            
    funcionario = {
        "nome": nome,
        "sobrenome": sobrenome,
        "ano_nascimento": anoNascimento,
        "RG": rg,
        "ano_admissao": anoAdimisao,
        "salario": salario
    }
            
    funcionarios.append(funcionario)
    salvar_funcionarios(funcionarios)
    print("\nfuncionario registrado!!!")

def Reajusta_dez_porcento(lista_empregados):
    for empregado in lista_empregados:
        empregado['salario'] *= 1.1
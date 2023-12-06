
from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        while True:
            try:
                nElementos = int(input("Quantos elementos vao existir na lista? "))
                for elemento in range(nElementos):
                    elemento = input("Digite um nome: ")
                    self.__lista.append(elemento)
                    print(self.__lista)
                break
            except Exception as e:
                print(f"Erro: {e}")

    def mostraMediana(self):
        tamanho = len(self.__lista)
        
        if tamanho == 0 :
            print("A lista está vazia. Não é possivel calcular a mediana")
        else :
            listaOrdenada = sorted(self.__lista, key=len)
            tamanhoOrdenado = len(listaOrdenada)
            
            if tamanhoOrdenado % 2 == 0:
                mediana1 = self.__lista[tamanhoOrdenado // 2 - 1]
                mediana2 = self.__lista[tamanhoOrdenado // 2]
                print("Mediana: " + mediana1 + "," + mediana2)
                
            else :
                mediana = self.__lista[tamanho // 2]
                print(f"Mediana:  {mediana}")
         

    def mostraMenor(self):
        if len(self.__lista) == 0 :
            print("A lista está vazia. Não é possivel calcular o menor elemento")
        else :
            print(f"Menor elemento nessa lista:  {min(self.__lista,  key=len)}")
            
            

    def mostraMaior(self):
        if len(self.__lista) == 0:
            print("A lista está vazia. Não é possivel calcular o maior elemento")
        else :
            print(f"Maior elemento na lista:  {(max(self.__lista, key=len))}")

    def listarEmOrdem(self):
        print("Lista de nomes ordenada:")
        for nome in sorted(self.__lista, key=len):
            print(nome)
        print()

    def mostrarNomeSalario(self, salarios):
        print("Nome e Salário:")
        for nome, salario in zip(self.__lista, salarios):
            print(f'{nome}: R${salario:.2f}')
        print()

    def __str__(self):
        return f"Lista de nomes: {', '.join(self.__lista)}"
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        while True:
            try:
                quantidade = int(input("Insira a quantidade de elementos da lista de Datas: \n"))
                for i in range(quantidade):
                    while True:
                        try:
                            print(f"Data {i + 1}:")
                            dia = int(input("Insira o dia: "))
                            mes = int(input("Insira o mês: "))
                            ano = int(input("Insira o ano: "))
                            data = Data(dia, mes, ano)
                            self.__lista.append(data)
                            break
                        except Exception as e:
                            print(f"Erro: {e}")
                break
            except Exception as e:
                print(f"Erro: {e}")
    
    def mostraMediana(self):
        lista_ordenada = sorted(self.__lista)
        meio = len(lista_ordenada) // 2
        if (len(lista_ordenada) % 2 == 0):
            print(f"\nMediana das datas: {lista_ordenada[meio-1]}")
        else:
            print(f"Mediana das datas: {lista_ordenada[meio]}")
     
    def mostraMenor(self):
        print(f"\nMenor data: {min(self.__lista)}")
        pass
    
    def mostraMaior(self):
        print(f"Maior data: {max(self.__lista)}")
        pass

    def listarEmOrdem(self):
        print("Lista de datas ordenada:")
        for data in sorted(self.__lista):
            print(data)
        print()

    def modificarDatas(self):
        ano_limite = 2019
        self.__lista = list(map(lambda data: data.replace(day=1) if data.year < ano_limite else data, self.__lista))
        print("Datas modificadas:")
        for data in self.__lista:
            print(data)
        print()
    
    def __str__(self):
        return f"Lista de Datas: {', '.join(map(str, self.__lista))}"

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []      

    def getLista(self):
        return self.__lista      

    def entradaDeDados(self):
        while True:
            try:
                quantidade = int(input("Insira a quantidade de elementos da lista de Salários: "))
                for i in range(quantidade):
                    salario = float(input("Digite o salario: "))
                    self.__lista.append(salario)
                break
            except Exception as e:
                print(f"Erro: {e}")

    def mostraMediana(self):
        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)
        if len(lista_ordenada) % 2 == 0:
            print(f"\nMediana dos salarios: {(lista_ordenada[tamanho // 2 - 1] + lista_ordenada[tamanho // 2]) / 2}")
        else:
            print(f"Mediana dos salarios: {lista_ordenada[tamanho // 2]}")

    def mostraMenor(self):
        print(f"\nMenor salario: {min(self.__lista)}")

    def mostraMaior(self):
        print(f"Maior salario: {max(self.__lista)}")

    def listarEmOrdem(self):
        print("Lista de salários ordenada:")
        for salario in sorted(self.__lista):
            print(salario)
        print()

    def custoDeFolhaReajustada(self, percentual):
        self.__lista = list(map(lambda salario: salario * (1 + percentual / 100), self.__lista))
        print("Custo de folha reajustada:")
        for salario in self.__lista:
            print(salario)
        print()
    
    def __str__(self):
        return f"Lista de salarios: {self.__lista}"

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        while True:
            try:
                quantidade = int(input("Insira a quantidade de elementos da lista de Idades: "))
                for i in range(quantidade):
                    idade = int(input("Digite a idade: "))
                    self.__lista.append(idade)
                break
            except Exception as e:
                print(f"Erro: {e}")
    
    def mostraMediana(self):
        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)
        if len(lista_ordenada) % 2 == 0:
            print(f"\nMediana das idades: {(lista_ordenada[tamanho // 2 - 1] + lista_ordenada[tamanho // 2]) / 2}")
        else:
            print(f"Mediana das idades: {lista_ordenada[tamanho // 2]}") 
    
    def mostraMenor(self):
        print(f"\Menor idade: {min(self.__lista)}")
    
    def mostraMaior(self):
        print(f"Maior idade: {max(self.__lista)}")

    def listarEmOrdem(self):
        print("Lista de idades ordenada:")
        for idade in sorted(self.__lista):
            print(idade)
        print()

    def __str__(self):
        return f"Lista de idades: {self.__lista}"

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [datas]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print(lista)
        print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()


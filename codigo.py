class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id  
        self.nome = nome 
        self.endereco = endereco  

    def cadastrar(self):
        print(f"Torre {self.nome} cadastrada.")

    def imprimir(self):
        print(f"Torre ID: {self.id}, Nome: {self.nome}, Endereço: {self.endereco}")

class Apartamento:
    def __init__(self, id, numero_apartamento, numero_vaga, torre):
        self.id = id  
        self.numero_apartamento = numero_apartamento 
        self.numero_vaga = numero_vaga  
        self.torre = torre 
        self.proximo = None 

    def cadastrar(self):
        print(f"Apartamento {self.numero_apartamento} cadastrado.")

    def imprimir(self):
        print(f"Apartamento ID: {self.id}, Número: {self.numero_apartamento}, Vaga: {self.numero_vaga}, Torre: {self.torre.nome}")


class No:
    def __init__(self, apartamento):
        self.apartamento = apartamento  
        self.proximo = None 


class ListaEncadeada:
    def __init__(self):
        self.inicio = None  
        self.fim = None  

    def adicionar_apartamento(self, apartamento):
        novo_no = No(apartamento)
        if self.fim is None: 
            self.inicio = novo_no  
            self.fim = novo_no
        else:
           
            self.fim.proximo = novo_no
            self.fim = novo_no

    def liberar_vaga(self, numero_vaga):
        if self.inicio is None:  
            return None
        if self.inicio.apartamento.numero_vaga == numero_vaga:  
            liberado = self.inicio.apartamento
            self.inicio = self.inicio.proximo
            if self.inicio is None:  
                self.fim = None
            return liberado
        anterior = None
        atual = self.inicio
        while atual is not None and atual.apartamento.numero_vaga != numero_vaga:
            anterior = atual
            atual = atual.proximo
        if atual is not None:
            liberado = atual.apartamento
            if anterior is not None:
                anterior.proximo = atual.proximo
            if atual == self.fim:  
                self.fim = anterior
            return liberado
        return None

    def imprimir_lista(self):
        atual = self.inicio
        while atual is not None:
            print(f"Apartamento {atual.apartamento.numero_apartamento} está na vaga {atual.apartamento.numero_vaga}.")
            atual = atual.proximo


class FilaEspera:
    def __init__(self):
        self.inicio = None  
        self.fim = None  

    def adicionar_apartamento(self, apartamento):
        novo_no = No(apartamento) 
        if self.fim is None:  
            self.inicio = novo_no  
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def retirar_apartamento(self, numero_vaga):
        if self.inicio is None:  
            return None
        apartamento_retirado = self.inicio.apartamento
        self.inicio = self.inicio.proximo
        if self.inicio is None:  
            self.fim = None
        return apartamento_retirado

    def imprimir_fila(self):
        atual = self.inicio
        if atual is None:  
            print("FILA DE ESPERA POR VAGA está vazia.")
        else:
            print("FILA DE ESPERA POR VAGA:")
            while atual is not None:
                print(f"Apartamento {atual.apartamento.numero_apartamento} está esperando vaga de garagem.")
                atual = atual.proximo

# Função principal para gerenciar apartamentos e vagas
def main():
    fila_espera = FilaEspera() 
    lista_apartamentos = ListaEncadeada() 
    vagas_disponiveis = 10 

    while True:
        print("\nMENU:")
        print("a) Cadastrar apartamento")
        print("b) Liberar vaga")
        print("c) Imprimir lista de apartamentos com vaga")
        print("d) Imprimir fila de espera por vaga")
        print("x) Sair")

        opcao = input("Escolha uma opção: ").lower()

        if opcao == 'a':
            if vagas_disponiveis > 0:
                id_apartamento = input("Informe o ID do apartamento: ")
                numero_apartamento = input("Informe o número do apartamento: ")
                numero_vaga = int(input("Informe o número da vaga de garagem: "))
                torre = input("Informe a torre: ")

                apartamento = Apartamento(id_apartamento, numero_apartamento, numero_vaga, torre)
                lista_apartamentos.adicionar_apartamento(apartamento)
                vagas_disponiveis -= 1
                print("Apartamento cadastrado com sucesso!")
            else:
                print("Não há vagas disponíveis. O apartamento será adicionado à fila de espera.")
                id_apartamento = input("Informe o ID do apartamento: ")
                numero_apartamento = input("Informe o número do apartamento: ")
                numero_vaga = int(input("Informe o número da vaga de garagem: "))
                torre = input("Informe a torre: ")

                apartamento = Apartamento(id_apartamento, numero_apartamento, numero_vaga, torre)
                fila_espera.adicionar_apartamento(apartamento)

        elif opcao == 'b':
            numero_vaga = int(input("Informe o número da vaga a ser liberada: "))
            liberado = lista_apartamentos.liberar_vaga(numero_vaga)
            if liberado:
                print(f"A vaga {numero_vaga} foi liberada. Apartamento {liberado.numero_apartamento} foi removido.")
                fila_espera.adicionar_apartamento(liberado)
                if not fila_espera.inicio:  # Se a fila de espera está vazia
                    vagas_disponiveis += 1
                else:
                    proximo = fila_espera.retirar_apartamento(numero_vaga)
                    if proximo:
                        lista_apartamentos.adicionar_apartamento(proximo)
                        print(f"Apartamento {proximo.numero_apartamento} da fila de espera ocupou a vaga.")

        elif opcao == 'c':
            print("\nLISTA DE APARTAMENTOS COM VAGA:")
            lista_apartamentos.imprimir_lista()

        elif opcao == 'd':
            print("\nFILA DE ESPERA POR VAGA:")
            fila_espera.imprimir_fila()

        elif opcao == 'x':
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
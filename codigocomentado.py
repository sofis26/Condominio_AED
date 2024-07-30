class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id  
        self.nome = nome 
        self.endereco = endereco  

    def cadastrar(self):
        print(f"Torre {self.nome} cadastrada.")

    def imprimir(self):
        print(f"Torre ID: {self.id}, Nome: {self.nome}, Endereço: {self.endereco}")
        

# 1. Construindo a Torre:
# __init__: Essa palavra estranha é como um botão mágico que você aperta para construir uma nova torre. Quando você constrói a torre,
# você dá a ela:
# id: Um número especial, como um código de barras, que só aquela torre tem.
# nome: O nome da torre, como se fosse o nome de um prédio de brinquedo, tipo "Torre Azul".
# endereco: O endereço de onde essa torre fica na sua cidade de brinquedo, como "Rua dos Brinquedos, nº 5".

# 2. Cadastrando a Torre:
# cadastrar: Quando você termina de construir a torre, você pode dizer "Torre [nome da torre] cadastrada!" É como se estivesse dizendo:
# "Pronto, essa torre está oficialmente na nossa cidade!"

# 3. Mostrando a Torre:
# imprimir: Se você quiser mostrar para alguém as informações sobre a torre, você pode usar essa função para dizer:
# "Torre ID: [número especial], Nome: [nome], Endereço: [endereço]". É como se você estivesse mostrando uma ficha com todos os detalhes da torre!
# Então, essa parte do código é como construir e apresentar torres em uma cidade de brinquedo, com um nome, um número especial, e um endereço!


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
        
# 1. Criando um Apartamento:
# __init__: Este é o botão mágico que cria um novo apartamento dentro de uma torre. Quando você cria um apartamento, você dá a ele:
# id: Um número especial, como um código de barras, que só aquele apartamento tem.
# numero_apartamento: O número do apartamento, como se fosse o número de uma porta, tipo "101" ou "202".
# numero_vaga: Um número que diz onde o carrinho de brinquedo pode estacionar. É como um espaço de estacionamento.
# torre: A torre onde o apartamento está. É como dizer em qual prédio de brinquedo o apartamento fica.
# proximo: Um lugarzinho que guarda qual é o próximo apartamento da fila. No começo, ele não sabe quem é o próximo, por isso é "None" (nenhum).

# 2. Cadastrando o Apartamento:
#cadastrar: Quando você termina de criar o apartamento, você pode dizer "Apartamento [número do apartamento] cadastrado!". É como anunciar:
# "Este apartamento está pronto e registrado!"

# 3. Mostrando o Apartamento:
# imprimir: Se você quiser mostrar as informações do apartamento para alguém, você pode usar essa função para dizer:
# "Apartamento ID: [número especial], Número: [número do apartamento], Vaga: [número da vaga], Torre: [nome da torre]".
# É como se estivesse mostrando um cartão de identidade do apartamento!
        


class No:
    def __init__(self, apartamento):
        self.apartamento = apartamento  
        self.proximo = None 

# 1. Criando um "No":
# __init__: Esse é o botão mágico que cria um "No". Um "No" é como um marcador ou um bloquinho de notas onde a gente anota as informações de
# um apartamento e o próximo na fila.

# 2. apartamento: Aqui, colocamos o apartamento que queremos lembrar. É como escrever no bloquinho de notas "Este No é para o Apartamento 101".

# 3. proximo: Esse espaço é para guardar o próximo "No" na fila. No começo, ele não sabe qual é o próximo, então colocamos "None" (nenhum)
# até decidirmos quem vem depois.

# Então, um "No" é como um bloquinho de notas que guarda informações sobre um apartamento e também ajuda a organizar a fila,
# dizendo quem é o próximo na fila!


class ListaEncadeada:
    def __init__(self):
        self.inicio = None  
        self.fim = None  
        
# 1. Criando a Lista Encadeada:

# __init__: Esse é o botão mágico que cria uma nova lista. A lista é como uma fila de apartamentos que têm vagas de estacionamento. Quando
# criamos a lista, ela começa vazia, por isso:
# inicio: Fica como "None" (nenhum), porque não tem nenhum apartamento no começo da fila.
# fim: Também é "None" (nenhum), porque não tem nenhum apartamento no final da fila.

    def adicionar_apartamento(self, apartamento):
        novo_no = No(apartamento)
        if self.fim is None: 
            self.inicio = novo_no  
            self.fim = novo_no
        else:
           
            self.fim.proximo = novo_no
            self.fim = novo_no
            
#'adicionar_apartamento': Quando queremos adicionar um apartamento à fila, fazemos um novo "No" para ele.
# Se a fila estiver vazia (ou seja, se fim for "None"), colocamos o novo "No" tanto no inicio quanto no fim, porque ele é o único na fila.
# Se já tiver algum apartamento na fila, colocamos o novo "No" depois do último (o fim). Assim, o último "No" agora aponta para o novo "No"
# e o novo "No" se torna o novo fim da fila.


    def liberar_vaga(self, numero_vaga):
        if self.inicio is None:  # Verifica se a fila está vazia
            return None # Retorna None se a fila estiver vazia
        if self.inicio.apartamento.numero_vaga == numero_vaga:  # Verifica se o primeiro apartamento na fila tem o número da vaga que queremos liberar, se sim, 
            liberado = self.inicio.apartamento # Aqui pega o apartamento para liberar e armazena na variável?
            self.inicio = self.inicio.proximo # o próximo apartamento vai se tornar o primeiro agora (pois o outro foi embora)
            if self.inicio is None:  # Verifica se a fila está vazia
                self.fim = None # Se estiver, o fim da fila ficou como None
            return liberado # Retorna o apartamento que foi liberado
        anterior = None # Se o primeiro apartamento não é o que queremos, começamos a procurar na fila
        atual = self.inicio # O que começarmos a checar vai ser o primeiro da fila
        while atual is not None and atual.apartamento.numero_vaga != numero_vaga: # Continua a procura enquanto há apartamentos e não encontramos o apartamento com a vaga que queremos
            anterior = atual # o apartamento atual se torna o anterior
            atual = atual.proximo # passamos para o proximo apartamento da fila
        if atual is not None: # Se encontrarmos o apartamento com a vaga que queremos
            liberado = atual.apartamento # Aqui pega o apartamento para liberar a vaga
            if anterior is not None: # Se o carrinho anterior existe...  
                anterior.proximo = atual.proximo #... ele agora aponta para o próximo carrinho depois do que foi liberado
            if atual == self.fim: # Se o apartamento que liberamos era o último da fila 
                self.fim = anterior # ajustamos o final da fila para o carrinho anterior
            return liberado # aí devolvemos o apartamento que liberou a vaga
        return None # Se não encontrarmos o apartamento, devolvemos None (quer dizer que não tem vaga para liberar)
    
# Resumindo esse código é onde se o apartamento que queremos está na fila e, se encontrarmos, tiramos da fila e liberamos a vaga de estacionamento


    def imprimir_lista(self):
        atual = self.inicio
        while atual is not None:
            print(f"Apartamento {atual.apartamento.numero_apartamento} está na vaga {atual.apartamento.numero_vaga}.")
            atual = atual.proximo

#imprimir_lista: Essa função é usada para mostrar todos os apartamentos que estão na fila com suas vagas. Começamos do inicio e vamos
# passando de um "No" para o próximo, até o fim da fila.

class FilaEspera:
    def __init__(self):
        self.inicio = None  
        self.fim = None  
        
# __init__: Esse é o botão mágico que cria uma nova fila de espera. No começo, a fila está vazia, então:
# inicio: Não tem nenhum carrinho no começo da fila, então colocamos "None" (nenhum).
# fim: Também não tem nenhum carrinho no final da fila, então colocamos "None" (nenhum).

    def adicionar_apartamento(self, apartamento):
        novo_no = No(apartamento) 
        if self.fim is None:  
            self.inicio = novo_no  
            self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

# adicionar_apartamento: Quando queremos colocar um novo carrinho na fila de espera, fazemos um novo "No" para ele.
# Se a fila estiver vazia (fim é "None"), colocamos o novo carrinho tanto no inicio quanto no fim, porque ele é o único na fila.
# Se já houver carrinhos na fila, colocamos o novo carrinho depois do último. Então, o último carrinho aponta para o novo,
# e o novo carrinho se torna o fim da fila.

    def retirar_apartamento(self, numero_vaga):
        if self.inicio is None: # Se a fila estiver vazia, não tem nenhum apartamento para retirar...
            return None # ...então retornamos None (nenhum)
        apartamento_retirado = self.inicio.apartamento # Se decidirmos retirar o primeiro apartamento da fila, pegamos ele e guardamos na variável 'apartamento_retirado'
        self.inicio = self.inicio.proximo # depois de pegar aquele, o próximo se torna o primeiro (ocupando o lugar)
        if self.inicio is None:  # Se depois de tirar aquele e não tiver mais apartamento na fila...
            self.fim = None # ...a fila fica vazia
        return apartamento_retirado # devolvemos o apartamento que foi retirado/que saiu para estacionar
    


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
            if vagas_disponiveis > 0: # Verifica se tem vaga na garagem
                id_apartamento = input("Informe o ID do apartamento: ")
                numero_apartamento = input("Informe o número do apartamento: ")
                numero_vaga = int(input("Informe o número da vaga de garagem: "))
                torre = input("Informe a torre: ")

                apartamento = Apartamento(id_apartamento, numero_apartamento, numero_vaga, torre)
                lista_apartamentos.adicionar_apartamento(apartamento)
                vagas_disponiveis -= 1 # Como já se tem um apartamento cadastrado, diminui-se uma vaga
                print("Apartamento cadastrado com sucesso!")
            else:
                print("Não há vagas disponíveis. O apartamento será adicionado à fila de espera.")
                id_apartamento = input("Informe o ID do apartamento: ")
                numero_apartamento = input("Informe o número do apartamento: ")
                numero_vaga = int(input("Informe o número da vaga de garagem: "))
                torre = input("Informe a torre: ")

                apartamento = Apartamento(id_apartamento, numero_apartamento, numero_vaga, torre)
                fila_espera.adicionar_apartamento(apartamento) # Se não tiver vagas, o apartamento vai ser adicionado na fila de espera

        elif opcao == 'b':
            numero_vaga = int(input("Informe o número da vaga a ser liberada: "))
            liberado = lista_apartamentos.liberar_vaga(numero_vaga) # Chamamos a função liberar_vaga da lista_apartamentos para tirar o
            #apartamento que está na vaga numero_vaga. A função devolve o apartamento que foi liberado e guardamos ele na variável liberado.
            if liberado:
                print(f"A vaga {numero_vaga} foi liberada. Apartamento {liberado.numero_apartamento} foi removido.") # Se liberado não for None,
                # isso significa que realmente liberamos um apartamento. Então, imprimimos uma mensagem dizendo qual vaga foi liberada e qua
                # apartamento saiu.
                fila_espera.adicionar_apartamento(liberado) # Se o apartamento foi liberado, adicionamos ele na fila de espera
                if not fila_espera.inicio:  # Se a fila de espera estiver vazia... / Aqui, verificamos se o começo da fila de espera
                    # (fila_espera.inicio) é None, o que significa que a fila está vazia. 
                    vagas_disponiveis += 1 # Se estiver vazia, aumentamos o número de vagas
                    # disponíveis em 1 (vagas_disponiveis += 1).
                else:
                    proximo = fila_espera.retirar_apartamento(numero_vaga)
                    if proximo:
                        lista_apartamentos.adicionar_apartamento(proximo)
                        print(f"Apartamento {proximo.numero_apartamento} da fila de espera ocupou a vaga.")
                    
            

# Se a fila de espera não estiver vazia, chamamos fila_espera.retirar_apartamento(numero_vaga) para pegar o próximo apartamento da fila.
# Guardamos esse apartamento na variável proximo.
# Se proximo não for None, significa que realmente retiramos um apartamento da fila de espera. Então, adicionamos esse apartamento à lista de
# apartamentos (lista_apartamentos.adicionar_apartamento(proximo)).
# Por fim, imprimimos uma mensagem dizendo que o apartamento da fila de espera ocupou a vaga liberada.


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
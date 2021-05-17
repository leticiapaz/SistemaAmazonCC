#biblioteca pela limpar o console
import os

#Lista de produtos, querendo aumentar é só cadastrar
lista_de_produtos = [{"codigo": "1", "nome": "Pasta de Dente", "preco": int(5.00)}, {"codigo": "2", "nome": "Arroz 5Kg", "preco": int(10)},{"codigo": "3", "nome": "Feijão", "preco": int(4.00)}, {"codigo": "4", "nome": "Açucar 1Kg", "preco": int(2.00)}, {"codigo": "5", "nome": "Sabonete", "preco": int(1.50)}, {"codigo":"6", "nome": "Shampoo", "preco": int(5.00)}, {"codigo":"7", "nome": "Mortadela", "preco": int(15.00)}, {"codigo":"8", "nome": "Café", "preco": int(4.50)}, {"codigo":"9", "nome": "Iogurte", "preco": int(6.00)}, {"codigo":"10", "nome": "Detergente", "preco": int(2.00)}, {"codigo":"11", "nome": "Bolacha Salgada", "preco": int(5.50)}, {"codigo":"12", "nome": "Fermento", "preco": int(4.00)}, {"codigo":"13", "nome": "Fraldas", "preco": int(25.00)}, {"codigo":"14", "nome": "Escova de dente", "preco": int(8.00)}, {"codigo":"15", "nome": "Sal", "preco": int(3.00)}, {"codigo":"16", "nome": "Farinha de Trigo 5 KG", "preco": int(15.00)}, {"codigo":"17", "nome": "Amaciante 5L", "preco": int(20.00)}, {"codigo":"18", "nome": "lâmpada", "preco": int(5.00)}, {"codigo":"19", "nome": "Molho de tomate", "preco": int(1.50)}, {"codigo":"20", "nome": "Macarrão 500g", "preco": int(3.50)}]

lista_de_clientes = []

#variavel para quebrar o while
sistema = True

usuario_sessao_cpf = str

#Veificar o tamanho da senha
def validaSenha(senha):
    if len(senha) != 6:
        return False
    return True

def cpf_valido(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

#Verifica se o cpf já não existe no sistema
def existeCpf(cpf):
    #Foreach em python
    for cpfs in lista_de_clientes:
        if cpfs["cpf"] == cpf:
            return False
    return True

def clienteInsert():
    #Captura os valores para um cadastro do cliente, separados por virgula
    nome, cpf, senha, email = map(str,input("Digite o Nome, CPF, Senha de 6 Digitos e Email separados por virgula: \n").split(","))
    #Verifica se não existe no sistema este cpf
    if(not existeCpf(cpf)):
        return input("CPF Já cadastrado no Sistema\n")
    elif (not cpf_valido(cpf)):
        return input("CPF Inválido, por favor digite um válido\n")
    elif(not validaSenha(senha)):
        return input("A senha precisa ter 6 digitos\n")
    cliente = {'nome': str, 'cpf': str, 'senha': str, 'email': str, "limite": int(1000), "compras": list()}
    cliente['nome'] = nome
    cliente['cpf'] = cpf
    cliente['senha'] = senha
    cliente['email'] = email
    lista_de_clientes.append(cliente)
    return input("Cliente Adicionado pressione enter para prosseguir:")

def buscarCliente(cpf):
    #Percorre a Lista de Clientes em busca do CPF Em questão.
    for cliente in lista_de_clientes:
        if(cliente["cpf"] == cpf):
            return input("Nome: "+cliente["nome"]+". Email: " + cliente["email"]+"\nPrecione enter para voltar para o menu de opções:")
    return input("Cliente não Encontrado")

def retornaCliente(cpf):
    for cliente in lista_de_clientes:
        if(cliente["cpf"] == cpf):
            return cliente

def mostrarCarrinho(cpf):
    total = 0
    #Encontra o Cliente
    cliente = retornaCliente(cpf)
    #Verifica Se tem itens no carrinho
    if(len(cliente["compras"]) == 0):
        return input("Carrinho Vazio \nPressione enter para voltar para o menu de opções:")
    #Mostrar todos os itens do carrinho e soma o total
    for compra in cliente["compras"]:
        total +=compra["preco"]
        print(compra["codigo"]+" - "+compra["nome"]+" -R$ = "+str(compra["preco"])+".\n") 
    print("Total:R$= "+str(total)+"\nPressione enter para voltar para o menu de opções:")
    return input()

#Valida se o usuário tem limite para adicioar o produto ao carrinho
def validaLimite(cliente, produtoCompra):
    if(cliente["limite"] - produtoCompra["preco"] < 0):
        return False
    if(cliente["limite"] <= 0):
        return False
    return True

def compraProduto(cpf, codigo, quantidade):
    clienteSessao = retornaCliente(cpf)
    #Percorrer a lista de produtos para achar o produto a entrar no carrinho
    for produto in  lista_de_produtos:
        if(produto["codigo"] == codigo):
            produtoCompra = produto
    #Vai adicionar a quantidade X daquele produto ao carrinho
    for i in range(1, int(quantidade) +1):
        #Valida se tem saldo para adicionar ao carrinho
        if(not validaLimite(clienteSessao, produtoCompra)):
            return input("Não foi possível adicionar todos os itens ao carrinho. Verifique seu Carrinho para saber quantos puderam entrar por conta do seu Limite")
        clienteSessao["compras"].append(produtoCompra)
        clienteSessao["limite"] -= produtoCompra["preco"]
    return input("Produto adicionado ao carrinho pressione enter para prosseguir:")

def mostraProdutos(cpf):
    print("\n Lista de Compras \n")
    #Percorre a Lista de Compras e Mostra os dados de cada Produto
    for produto in lista_de_produtos:
        print(produto["codigo"]+" - "+produto["nome"]+" -R$ "+str(produto["preco"])+".\n")
    #Verifica se o usuário quer realizar alguma compra
    comprar = input("Deseja Comprar algum produto [S ou N]? ")
    if(comprar == "S" or comprar == "s"):
        codigo,quantidade = map(str, input("Digite o Codigo do produto e a quantidade separados por Virgula.\n").split(","))
        compraProduto(cpf, codigo, quantidade)
    print("Obrigado pela Preferência:\n\nPressione enter para voltar para o menu de opções:")   
    return input()

def listaUsuarios():
    #Retorna todos os usuário do sistema, informando Nome e Email
    for usuario in lista_de_clientes:
        print("Nome: "+usuario["nome"]+". Email: "+usuario["email"]+".\n")
    return input("Pressione Enter para voltar ao menu de opções")

def pagarFatura(cpf):
    total = 0
    clienteFatura = retornaCliente(cpf)
    #Calcula o total da fatura
    for compra in clienteFatura["compras"]:
        total +=compra["preco"]
    pagar = input("Total da compra: "+str(total)+"\n Desejar pagar a fatura? [S ou N]")
    #Limpa o carriho e retorna o limite para 1000
    if(pagar == "S" or pagar == "s"):
        clienteFatura["compras"] = list()
        clienteFatura["limite"] = int(1000)
        return input("Pagamento realizado, limite liberado\nPressione enter para voltar para o menu de opções:")    

#Valida A troca de usuário da Sessão
def trocaUsuario(cpf, senha):
    cliente = retornaCliente(cpf)
    if(cliente["senha"] == senha):
        return cliente;
    return input("Senha incorreta")

#acões do sistema
def acoes(cpf):
    #Limpa o console para ele não ficar poluido. Função valida para windows
    os.system("clear")

    #Mostra as opçoes de ações do sistema
    escolha = int(input("Escolha uma Opção: \n 1 - Mostrar Lista de Produtos. \n 2 - Cadastrar Novo Cliente. \n 3 - Verificar Carrinho de Compras.\n 4 - Lista de usuários.\n 5 - Pagar a Fatura. \n 6 - Buscar Cliente Por CPF.\n 7 - Trocar Usuário \n 0 - Sair do Sistema \n"))
    if(escolha == 1):
        mostraProdutos(cpf)
    elif(escolha == 2):
        clienteInsert()
    elif(escolha == 3):
        mostrarCarrinho(cpf)
    elif(escolha == 4):
        listaUsuarios()
    elif(escolha == 5):
        pagarFatura(cpf)
    elif(escolha == 6):
        cpfBuscar = input("Digite o CPF a ser consultado: \n")
        buscarCliente(cpfBuscar)
    elif(escolha == 7):
        return 1
    elif(escolha == 0):
        return -1
    else:
        return input("Escolha uma Opção Válida")
    return 0

#primeiro Acesso, obrigatrório a criação de um usuário
while(len(lista_de_clientes)== 0):
        print("Primeiro Cliente, por favor se cadastre.")
        clienteInsert()
        os.system("clear")

usuario_sessao_cpf = lista_de_clientes[0]["cpf"]

while(sistema):
    #Verifica se o usuário quer continuar usando
    if(acoes(usuario_sessao_cpf) == -1):
        input("Sessão Finalizada, Volte Sempre:")
        break
    #troca o cliente da sessão
    elif(acoes(usuario_sessao_cpf) == 1):
        cpfTroca, senha = map(str, input("Digite o CPF do usuário a entrar na Sessão, e Senha separados por virgula: \n").split(","))
        cliente = trocaUsuario(cpfTroca, senha)
        usuario_sessao_cpf = cliente["cpf"]
        input("Cliente Trocado\nPressione enter para voltar para o menu de opções")

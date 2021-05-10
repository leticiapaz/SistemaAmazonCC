import os

lista_de_produtos = [{"codigo": "1", "nome": "Pasta de Dente", "preco": int(5.00)}, {"codigo": "2", "nome": "Arroz 5Kg", "preco": int(10)},{"codigo": "3", "nome": "Feijão", "preco": int(4.00)}, {"codigo": "4", "nome": "Açucar 1Kg", "preco": int(2.00)}]

clientes = {'nome': str, 'cpf': str, 'senha': str, 'email': str, "limite": int(1000), "compras": list()}
lista_de_clientes = list()

usuario_cpf = str

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
    print(lista_de_clientes)
    #Captura os valores para um cadastro do cliente
    nome, cpf, senha, email = map(str,input("Digite o Nome, CPF, Senha de 6 Digitos e Email separados por virgula: \n").split(","))
    #Verifica se não existe no sistema este cpf
    if(not existeCpf(cpf)):
        return input("CPF Já cadastrado no Sistema\n")
    elif (not cpf_valido(cpf)):
        return input("CPF Inválido, por favor digite um válido\n")
    elif(not validaSenha(senha)):
        return input("A senha precisa ter 6 digitos\n")
    cliente = clientes
    cliente['nome'] = nome
    cliente['cpf'] = cpf
    cliente['senha'] = senha
    cliente['email'] = email
    lista_de_clientes.append(cliente)
    return input()

def mostrarCarrinho(cpf):
    total = 0
    for cliente in lista_de_clientes:
        if(cliente["cpf"] == cpf):
            if(len(cliente["compras"]) == 0):
                return input("Carrinho Vazio \n")
            for compra in cliente["compras"]:
                total +=compra["preco"]
                print(compra["codigo"]+" - "+compra["nome"]+" - "+str(compra["preco"])+".\n")
    print("Total: "+str(total)+"\n")
    return input()

def compraProduto(cpf, codigo, quantidade):
    for cliente in lista_de_clientes:
        if(cliente["cpf"] == cpf):
            clienteSessao = cliente
    for produto in  lista_de_produtos:
        if(produto["codigo"] == codigo):
            produtoCompra = produto
    for i in range(1, quantidade +1):
        clienteSessao["compras"].append(produtoCompra)
    return input("Produto adicionado ao carrinho")

def mostraProdutos(cpf):
    print("\n Lista de Compras \n")
    for produto in lista_de_produtos:
        print(produto["codigo"]+" - "+produto["nome"]+" - "+str(produto["preco"])+".\n")
    comprar = input("Deseja Comprar algum produto [S ou N]? ")
    if(comprar == "S" or comprar == "s"):
        codigo,quantidade = map(str, input("Digite o Codigo do produto e a quantidade separados por Virgula.\n").split(","))
        compraProduto(cpf, codigo, quantidade)
    print("Obrigado pela Preferência")   
    return input()

def listaUsuarios():
    for usuario in lista_de_clientes:
        print("Nome: "+usuario["nome"]+". Email: "+usuario["email"]+".\n")
    return input("Pressione Enter para voltar ao menu de ações")
    
def acoes(cpf):
    os.system("clear")
    escolha = int(input("Escolha uma Opção: \n 1 - Mostrar Lista de Produtos. \n 2 - Cadastrar Novo Cliente. \n 3 - Verificar Carrinho de Compras.\n 4 - Lista de usuários.\n"))
    if(escolha == 1):
        mostraProdutos(cpf)
    elif(escolha == 2):
        clienteInsert()
    elif(escolha == 3):
        mostrarCarrinho(cpf)
    elif(escolha == 4):
        listaUsuarios()
    else:
        return input("Escolha uma Opção Válida")
    return 0

while(len(lista_de_clientes)== 0):
        print("Primeiro Cliente, por favor se cadastre.")
        clienteInsert()
        os.system("clear")

usuario_cpf = lista_de_clientes[0]["cpf"]

while(True):
    acoes(usuario_cpf)

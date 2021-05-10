import os

lista_de_produtos = [{"codigo": "1", "nome": "Pasta de Dente", "preco": int(5.00)}, {"codigo": "2", "nome": "Arroz 5Kg", "preco": int(10)},{"codigo": "3", "nome": "Feijão", "preco": int(4.00)}, {"codigo": "4", "nome": "Açucar 1Kg", "preco": int(2.00)}]

clientes = {'nome': str, 'cpf': str, 'senha': str, 'email': str, "limite": int(1000), "compras": list()}
lista_de_clientes = list()

usuario_cpf = str

def validaSenha(senha):
    if len(senha) != 6:
        return False
    return True
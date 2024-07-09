from operator import contains


menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Criar usuário
    [lu] Listar usuários
    [c] Criar conta corrente
    [lc] Listar contas correntes
    [q] Sair

  => """

def depositar(*, saldo, valor, extrato):
    if(valor <= 0):
        print("Valor inválido! Tente novamente.")
        return saldo, extrato
    else:
        saldo += valor
        extrato += f"Depositado: R$ {valor:.2f}\n"
        return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques, /):
    if(saldo <= 0):
        print("Saldo insuficiente! Tente novamente.")
    
    elif(numero_saques == 3):
        print("Limite de saques atingido! Tente novamente amanhã.")
    
    elif(valor > limite):
        print("Valor inválido! Superior ao limite.")

    elif(valor > saldo):
        print("Saldo insuficiente.")
    
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    return saldo, extrato, numero_de_saques

def exibir_extrato(saldo, /, *, extrato):
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Saldo da conta: R$ {saldo:.2f}")

def criar_usuario(lista):
    nome = input("Nome: ")
    nascimento = input("Data de nacimento: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")

    contador = 0
    for usuario in lista:
        for chave, valor in usuario.items():
            if(valor == cpf):
                contador = -1

    if(contador == -1):
        print("Usuário já cadastrado! Tente novamente.")
    else:
        new_client = {"Nome":nome, "Data":nascimento, "CPF":cpf, "Endereco":endereco}
        lista.append(new_client)
    return lista
    
def exibir_usuarios(lista):
    for usuario in lista:
        for chave, valor in usuario.items():
            print(chave, valor)
        print()

def criar_conta_corrente(lista_contas, lista_usuarios):
    agencia = "0001"
    numero = len(lista_contas)
    numero += 1
    x = int(input("Usuário: "))
    while (x > len(lista_usuarios)):
        x = int(input("""Usuário inválido!
Tente novamente: """))
    usuario = lista_usuarios[x]

    new_account = {"Agencia":agencia, "Numero da conta":numero, "Usuario":usuario}
    lista_contas.append(new_account)
    return lista_contas

def exibir_contas_correntes(lista):
    for conta in lista:
        for chave, valor in conta.items():
            print(chave, valor)
        print()
    

saldo = 0
LIMITE = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3
lista_de_clientes = []
lista_de_contas_correntes = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual valor deseja depositar? R$ "))
        saldo, extrato = depositar(saldo = saldo, valor = valor, extrato = extrato)

    elif opcao == "s":
        valor = float(input("Qual valor deseja sacar? R$ "))
        saldo, extrato, numero_de_saques = sacar(saldo, valor, extrato, LIMITE, 
                                                 numero_de_saques, LIMITE_DE_SAQUES)
        
    elif opcao == "e":
        exibir_extrato(saldo, extrato = extrato)

    elif(opcao == "u"):
        lista_de_clientes = criar_usuario(lista_de_clientes)
    elif(opcao == "lu"):
        exibir_usuarios(lista_de_clientes)

    elif(opcao == "c"):
        lista_de_contas_correntes = criar_conta_corrente(lista_de_contas_correntes, lista_de_clientes)
    elif(opcao == "lc"):
        exibir_contas_correntes(lista_de_contas_correntes)

    elif opcao == "q":
        break
    else:
        print("Opção inválida! Tente novamente.")

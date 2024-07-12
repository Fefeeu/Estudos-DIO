from abc import ABC, abstractmethod, abstractproperty

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_trasacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_trasacao(self)

class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = float(saldo)
        self._numero = int(numero)
        self._agencia = str(agencia)
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    def depositar(self, valor):
        if (valor > 0):
            self._saldo += valor
            return True
        else:
            print("Valor inválido")
        return False

    def sacar(self, valor):
        if(valor > self._saldo):
            print("Saldo insuficiente! Tente novamente.")

        elif(valor > 0):
            self._saldo -= valor
            return True
        
        else:
            print("Valor inválido! Tente novamente.")
        
        return False

class Cliente:
    def __init__(self, endereco):
        self._endereco = str(endereco)
        self._contas = []
    
    def realizar_trasacao(self, conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)

class ContaCorrete(Conta):
    def __init__(self, limite = 500, limite_saques = 3, **kw):
        super().__init__(**kw)  #numero, cliente
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("Limite excedido! Tente novamente.")
        elif excedeu_saques:
            print("Limite de saques excedido! Tente novamente.")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Títular:\t{self.cliente.nome}"""
    
class Historico:
    def __init__(self):
        self.transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_trasacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
        })

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, **kw):
        super().__init__(**kw)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

def menu():
    print("""

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair

  => """)
    return input().lower()
    
def recupera_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta! ")
        return
    
    # FIXEME: não permite o cliente escolher a conta, só para deixar o codigo mais facil, nada de mais
    return cliente.contas[0]

def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    
    return clientes_filtrados[0] if clientes_filtrados else None

def depositar(clientes):
    cpf = input("Informe o CPF do clente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recupera_conta_cliente(clientes)
    if not conta:
        return
    cliente.reliza_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do clente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = recupera_conta_cliente(clientes)
    if not conta:
        return
    cliente.reliza_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do clente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return
    
    conta = recupera_conta_cliente(clientes)
    if not conta:
        return
    
    print("Extrato")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações na conta."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\tR$ {conta.saldo:.2f}")

def criar_cliente (clientes):
    cpf = input("Informe o CPF do clente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if cliente:
        print("Cliente já cadastrado")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)
    print("Cliente criado com sucesso!")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado")
        return
    
    conta = ContaCorrete.nova_conta(cliente=cliente, numero = numero_conta)
    conta.append(conta)
    cliente.contas.append(conta)
    print("Conta criada com sucesso!")

def exibir_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(conta)

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas)+1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            exibir_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Opção inválida. Tente novamente.")
main()

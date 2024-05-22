menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

  => """

saldo = 0
LIMITE = 500
extrato = ""
numero_de_saques = 0
LMITE_DE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Qual valor deseja depositar? R$ "))
        if valor >= 0:
            saldo += valor
            extrato += f"Depositado: R$ {valor:.2f}\n"
        else:
            print("Valor inválido! Tente novamente.")

    elif opcao == "s":
        if saldo > 0:
            if numero_de_saques == 3:
                print("Limite de saques diarios atingido! Tente novamente amanhã.")
                continue
            valor = float(input("Qual valor deseja sacar? R$ "))
            if valor >= 0 and valor <= LIMITE and valor <= saldo:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_de_saques += 1
            else:
                if valor > LIMITE:
                    print("Valor inválido! Superior ao limite.")
                elif valor > saldo:
                    print("Saldo insuficiente.")
                else:
                    print("Valor inválido! Tente novamente.")
        else:
            print("Saldo insuficiente! Tente novamente.")
    elif opcao == "e":
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo da conta: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Opção inválida! Tente novamente.")-

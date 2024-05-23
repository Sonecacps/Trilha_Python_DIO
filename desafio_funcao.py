import textwrap

def menu ():
    menu = """

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Novo usuario
    [6] Listar contas
    [7] Sair

    Escolha uma opção: """

    return input (textwrap.dedent(menu))



def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor 
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print ("\n@@@Operacao falhou! O Valor informado é inválido. @@@") 
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação negada! Você não possui saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação Negada! Seu limite é inferior ao saque @@@")

    elif excedeu_saques:
        print("\n@@@ Operação negada! Você já atingiu o limite! @@@")

    elif valor > 0:
        saldo -= valor 
        extrato += f"Saque: \t\t R$ {valor:.2f}\n"
        numero_saques += 1
        print ("\n === Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é invalido @@@")

    return saldo, extrato

# Lógica para realizar o saque e atualizar o saldo e extrato
    novo_saldo = saldo - valor_saque
    novo_extrato = f"Saque de R${valor_saque}"
    
    return novo_saldo, novo_extrato
def exibir_extrato (saldo, /, *, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


def criar_usuario(usuarios):
     cpf = input("Informe seu cpf: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("\n@@@ Usuário já cadastrado @@@")
          return
     
     nome = input("Informe seu nome completo: ")
     data_nascimento = input("Informe a data de nascimento (dd-mmm-aaaa): ")
     endereco = input("Informe seu endereço: 4")

     usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

     print("=== Usuário cadastrado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe seu cpf: ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
          print("\n=== Conta criada com sucesso!")
          return{"agencia":agencia, "numero_conta":numero_conta,"usuario": usuario}
    print("\n @@@ Usuario não encontrado! @@@")
     
def listar_contas(contas):
     for conta in contas:
          linha = f"""\
          Agencia:\t{conta['agencia']}
          C\C:\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
          """
          print("=" * 100)
          print(textwrap.dedent(linha))

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuario = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
    
        elif opcao == "2":
                valor = float(input("Informe o valor do saque: "))

                saldo, extrato = sacar(
                    saldo = saldo,
                    valor = valor,
                    extrato = extrato,
                    limite = limite,
                    numero_saques = numero_saques,
                    limite_saques = LIMITE_SAQUES
                )

        elif opcao == "3":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "4":
            numero_conta = len(contas) +1
            conta = criar_conta(AGENCIA, numero_conta, usuario)
        
            if conta:
                contas.append(conta)


        elif opcao =="5":
            criar_usuario(usuario)

        elif opcao =="6":
            listar_contas(contas)
            if not contas:
                print("Sem contas") 
            
        elif opcao == "7":
             print("Saindo da operação")
             break

        else:
            print("Operação invalida, informe uma opção válida")
           


main()
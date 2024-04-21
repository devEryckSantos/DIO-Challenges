

def menu():
    menu = '''\n
    ============= MENU =============

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Novo usuário
    [5] Nova conta
    [6] Listar Contas
    [7] Sair
    ==> '''
    return input(menu)

def depositar(saldo, valor, extrato, depositos, /):
   if valor <= 0:
         print('Valores nulos ou negativos não são permitidos! Por favor, infome um valor positivo inteiro.')
   else:
       saldo += valor
       extrato += f"Depósito: R$ {valor:.2f}\n"
       depositos += 1
       print("Depósito realizado com sucesso!!!")

       return saldo, extrato, depositos

def sacar(*, saldo, valor_saque, extrato, saques, limite ,LIMITE_SAQUE):
    if saques >= LIMITE_SAQUE:
        print("Limite de saques excedido! Por favor, volte amanhã.")
    
    elif valor_saque > limite:
        print('LIMITE ATINGIDO! \nO valor do saque não pode ultrapassar os R$ 500,00.')

    elif valor_saque > saldo:
        print(f'VALOR EXCEDIDO! \nSeu saldo atual é de R$ {saldo:.2f}.')

    elif valor_saque <= 0:
        print('Valores nulos ou negativos não são permitidos. Por favor, informe um valor positivo inteiro.')

    else:
        saldo -= valor_saque
        saques += 1
        extrato += f'saque: R$ {valor_saque:.2f}\n'

    return saldo, extrato, saques

def exibir_extrato(saldo, /, *, extrato):
      print('\n-==-==-==-==-==-==- EXTRATO -==-==-==-==-==-==-')
      print('Nenhuma movimentação foi realizada.' if not extrato else extrato)
      print(f"\nSaldo atual: R$ {saldo:.2f}")
      print('-==-==-==-==-==-==--==-==-==-==-==-==--==-==-==')

def novo_cliente(clientes):
    cpf = int(input("Informe o CPF (somente números): "))
    cliente = filtrar_clientes(cpf, clientes)

    if cliente: # Verifica se o cliente foi encontrado
        print('CPF já cadastrado!')
        return # retorna pra função main

    nome = str(input('Nome completo: '))
    data_nascimento = int(input('Data de Nascimento (apenas números): '))
    endereço = {"logradouro": "", "numero": "", "bairro": "", "cidade": "", "estado": ""}
    endereço["logradouro"] = str(input('Endereço: '))
    endereço["numero"] = str(input('Número: '))
    endereço["bairro"] = str(input('Bairro: '))
    endereço["cidade"] = str(input('Cidade: '))
    endereço['estado'] = str(input('Estado: '))

    novo_cliente = dict(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereço=endereço)
    clientes.append(novo_cliente)
    
def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(agencia, numero_conta, clientes):
    cpf = int(input('Informe o CPF do usuário: '))
    cliente= filtrar_clientes(cpf, clientes)

    if cliente:
        print('Conta criada com sucesso!')
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
    
    print('CPF não cadastrado!')

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        """
        print('=' * 100)
        print(linha)

def main():

    LIMITE_SAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    depositos = 0
    saques = 0
    clientes = []
    contas = []


    while True:
        opcao = menu()

        if opcao == '1':
            valor = float(input("Informe o valor a ser depositado: "))

            saldo, extrato, depositos = depositar(saldo, valor, extrato, depositos)

        elif opcao == '2':
            valor_saque = float(input('Informe o valor do saque: '))

            saldo, extrato, saques = sacar(saldo=saldo, valor_saque=valor_saque, extrato=extrato, saques=saques, limite=limite, LIMITE_SAQUE=LIMITE_SAQUE,)    

        elif opcao == '3':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == '4':
            novo_cliente(clientes)

        elif opcao == '5':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)
            
        elif opcao == '6':
            listar_contas(contas)
        
        elif opcao == '7':
            break

        else: print(contas)

main()
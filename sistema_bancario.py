#  operação de depósito:

    # Perguntar o valor que será depositado.

    # verificar se o valor é positivo (valores negativos não são permitidos)

    # somar o valor deposito ao saldo.

    # armazenar o depósito em uma variável.

# operação de saque:

    # verificar quantos saques foram realizados (limite de 3).

    # Perguntar valor a ser sacado.

    # verificar se o valor excede o limite de 500 reais.

    # Verificar se há saldo o suficiente para realizar o saque. Caso não haja, informar.

    # Subtratir valor valor do saque do saldo.

    # Armazenar saque em uma variável.

# operação de extrato

    # Buscar a váriavel com a quatidade de saques e depósitos realizados.

    # listar as operações e informar os valores de cada saque e depósito.

    # no fim da listagem, exibir o saldo atual da conta.

    # os valores devem ser exibidos utilizando o formato R$ xxx.xx. Ex.: 1500.45 = R$ 1500.45

menu = '''
    ============= MENU =============

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
'''

saldo = 0
limite = 500
extrato = ""
depositos = 0
saques = 0
LIMITE_SAQUE = 3

while True: 
   opcao = (input(menu))

   if opcao == '1':
      print('Depósito')

      novo_deposito = (input('Informe o valor a ser depositado: R$ '))
      novo_deposito = int(novo_deposito)
      
      if novo_deposito <= 0:
         print('Valores nulos ou negativos não são permitidos! Por favor, infome um valor positivo inteiro.')

      saldo += novo_deposito
      extrato += f"Depósito: R$ {novo_deposito:.2f}\n"
      depositos += 1
    

   elif opcao == '2':
      print('Saque')

      if saques == LIMITE_SAQUE:
         print('Limite de saques diário atingido! Por favor, retorne amanhã.')
         
      valor_saque = input('Informe o valor do saque: R$ ')
      valor_saque = int(valor_saque)

      if valor_saque > limite:
            print('Limite excedido! O valor da saque não pode ultrapassar os R$ 500,00')

      elif valor_saque > saldo:
            print(f"Valor excedido! Seu saldo atual é de R$ {saldo:.2f}.")
      
      elif valor_saque < 0:
          print('Valores nulos ou negativos não são permitidos. Por favor, informe um valor positivo inteiro.')

      else:
         saldo -= valor_saque
         extrato += f"Saque: R$ {valor_saque:.2f}\n"
         saques += 1

   elif opcao == '3':
      print('\n-==-==-==-==-==-==- EXTRATO -==-==-==-==-==-==-')
      print('Nenhuma movimentação foi realizada.' if not extrato else extrato)
      print(f"\nSaldo atual: R$ {saldo:.2f}")
      print('-==-==-==-==-==-==--==-==-==-==-==-==--==-==-==')


   elif opcao == '4':
      print('saindo...')
      break
   
   
   else:
      print('Operação inválida! Por favor, digite uma opção válida.')
      print(saques)
menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':

        try:
            valor = float(input('Digite o valor que deseja depositar: '))

            if valor <= 0:
                print('O valor de depósito precisa ser positivo!')
            else:
                saldo += valor
                extrato += f'Depósito: R$ {valor:.2f}\n'
                print('Depósito realizado com sucesso')
                print(f'Saldo atual: R$ {saldo:.2f}')

        except:
            print('O valor do depósito precisa ser numérico!')


    elif opcao == 's':

        if numero_saques == LIMITE_SAQUES:
            print('Limite de saques atingido: Vocẽ já realizou 3 saques hoje.')
        else:
            try:
                valor = float(input('Digite o valor que deseja sacar: '))

                if valor <= 0:
                    print('O valor de saque precisa ser positivo!')
                elif valor > 500:
                    print('O valor máximo de saque é de R$ 500.00.')
                elif valor > saldo:
                    print('Saldo insuficiente para saque!')
                    print(f'Saldo atual: {saldo:.2f}')
                else:
                    saldo -= valor
                    extrato += f'Saque: R$ {valor:.2f}\n'
                    numero_saques += 1
                    print('Saque realizado com sucesso!')
                    print(f'Saldo atual: R$ {saldo:.2f}')

            except:
                print('O valor do saque precisa ser numérico!')


    elif opcao == 'e':

        print(extrato+f'Saldo atual: {saldo:.2f}' if extrato else 'Não foram realizadas movimentações')

    elif opcao == 'q':
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')

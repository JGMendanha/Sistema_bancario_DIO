import os

saldo = 0
extrato = []
saques = 0

while True:
    os.system('cls')
    print("==========BEM VINDO AO SISTEMA BANCÁRIO !!!!==========")
    print("VOCÊ TEM ALGUMAS OPÇÕES:\nOPÇÃO 1: DEPOSITAR\nOPÇÃO 2: SACAR\nOPÇÃO 3: EXTRATO\nOPÇÃO 4: SAIR")
    try:
        opcao = int(input("DIGITE SUA OPÇÂO "))
    except ValueError as e:
        pass
    print("======================================================")

    salva_extrato = ""

    if opcao == 1:
        os.system('cls')
        verifica_deposito = True
        while verifica_deposito:
            os.system('cls')
            try:
                add_saldo = float(input("Digite quanto quer depositar (Só será aceito valores positivos !) "))
            except ValueError as e:
                print("Digite um valor válido")
                os.system('pause')
            if add_saldo <= 0:
                print("Digite um valor válido")
                os.system('pause')
            else:
                saldo += add_saldo
                add_saldo = "{:.2f}".format(add_saldo)
                verifica_deposito = False
                salva_extrato = "Depósito: R$" + str(add_saldo)
                extrato.append(salva_extrato)
                os.system('pause')

    elif opcao == 2:
        os.system('cls')
        if saques < 3:
            verifica_saque = True
            saque = 0
            while verifica_saque:
                os.system('cls')
                try:
                    saque = float(input("Digite quanto quer sacar (Até 500 reais) "))
                except ValueError as e:
                    print("Digite um valor válido")
                    os.system('pause')
                if saque > 500 or saque < 0:
                    print("Digite um valor válido")
                    os.system('pause')
                elif saque > saldo:
                    print("Seu saldo é menor que o saque requerido. Favor digitar um valor menor")
                    os.system('pause')
                else:
                    saldo -= saque
                    saque = "{:.2f}".format(saque)
                    salva_extrato = "Saque: R$" + str(saque)
                    extrato.append(salva_extrato)
                    verifica_saque = False
                    saques += 1
                    os.system('pause')
        else:
            print("LIMITE DE SAQUES EXCEDIDO !!!")
            os.system('pause')
    
    elif opcao == 3:
        os.system('cls')
        exibir_saldo = "{:.2f}".format(saldo)
        print(f"EXTRATO:\nSALDO: R${exibir_saldo}\nOPERAÇÕES REALIZADAS:")
        for operacoes in extrato:
            print(operacoes)
        os.system('pause')
    
    elif opcao == 4:
        break

    else:
        os.system('cls')
        print("DIGITE UMA OPÇÃO VÁLIDA!!!!")
        os.system('pause')
        





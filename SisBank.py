# Sistema Bancário SisBank - Tela boas Vinda e Menu.

from time import sleep
from datetime import datetime

print('\n')
print('X'* 37)
print('\nSitema Bancário DIO - Seja Bem vindo!\n')
print('X' * 37, '\n')


 # Variáveis.


    
saldo = 0
limite = 500
extrato = list()
ext = dict()
numero_saques = 0
LIMITE_SAQUES = 3

sleep(1.5)

while True:

    print('='*37)
    print(f'\n{" "*14}***MENU***\n' 
        f'\n{" "*7}[1] Depositar'
        f'\n{" "*7}[2] Sacar'
        f'\n{" "*7}[3] Extrato'
        f'\n{" "*7}[q] Sair\n')
    print('='*37)



    #Selecionando transação.
    print(f'seu saldo é: R${saldo:.2f}'.upper())
    opcao = str(input('\nQual trasação deseja realizar?: ')).strip()[:1]
    print()

    #Tratando erros 1.
    if opcao in '':
        print('↓' * 40)
        print('FAVOR ESCOLHA SOMENTE AS OPÇÕES LISTADAS!')
        print('↑' * 40)
        sleep(2)
        continue

    #Opção 1 depósito.
    elif opcao == '1':
        print('_' * 40)
        dep = str(input('\n ☺☺☺ Qual valor deseja depositar?: R$'))
        if dep.replace('.', '').isnumeric() == False:
            print('X' * 40)
            print('\nerro! valores incorretos!\n'.title())
            print('X' * 40)
            sleep(2)

        #Deposito Realizado
        else:
            sld = float(dep) 
            saldo = saldo + sld
            print('↓' * 40)
            print(f'foi depositado o valor de R${sld:.2f}'.upper()) 
            print('↑' * 40) 
            ext['Depósito'] = f"Deposito => {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} => R${sld:.2f}" 
            extrato.append(ext.copy())
            ext.clear()
            sleep(2)
            
    #opção 2 saque.
    elif opcao == '2':
        print('_' * 40)
        sacar = str(input('\n ☻☻☻ Qual valor deseja sacar?: R$'))
        if sacar.replace('.', '').isnumeric() == False:
            print('X' * 40)
            print('\nerro! valores incorretos!\n'.title())
            print('X' * 40)
            sleep(2)

        #Limites de valores de saques
        elif float(sacar) > limite:
            print('♠' * 40)
            print('\nseu limite de saque é de R$500,00!\n'.upper())
            print('♠' * 40)
            sleep(2)
            continue 

        #Limites de quantidades de saques
        elif numero_saques >= LIMITE_SAQUES:
            print('♠' * 80)
            print('\nseus limites de saques foram excedidos, é possivel somente 03 saques por dia!\n'.upper())
            print('♠' * 80)
            sleep(2)
            continue 

        #Saldo negativo 
        elif float(sacar) > saldo :
            print('♣' * 40)
            print('você não tem saldo para realizar este saque!'.upper())
            print('♣' * 40)
            sleep(2)
            continue

        #Saque realizado
        else:
            sld = float(sacar)  
            saldo = saldo - sld
            numero_saques += 1         
            print('↓' * 60)
            print(f'o saque no valor de R${sld:.2f}, foi efetuado com sucesso!'.upper()) 
            print('↑' * 60) 
            ext['Saque'] = f"Saque => {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} => R${sld:.2f}"
            extrato.append(ext.copy())
            ext.clear()
            sleep(2)

    #Opção extrato
    elif opcao == '3':
        print('_' * 40)
        print('\nInformsções sobre movimentações:\n')
        for x, y in enumerate(extrato):
            for d in y.values():
                print(d)
        print(f'\nSaldo atual é R${saldo:.2f}\n')
        print('_' * 40)
        sleep(2)


    #Opção sair.
    elif opcao in 'qQ':
        print('♥' * 55)
        print('\nObrigado por usar nossos serviços, volte sempre!\n'.upper())
        print('♥' * 55)
        sleep(2)
        break
    else:
        print('►' * 40)
        print('FAVOR ESCOLHA SOMENTE AS OPÇÕES LISTADAS!')
        print('►' * 40)
        sleep(2)
        continue
        


    
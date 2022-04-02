import os
while True:

    
    operacao = input('Qual operação deseja fazer ? digite o respectivo sinal: (+, -, *, /, %) \nOu \'S\' para sair. \n')
    if operacao == 'S' or operacao == 's':
        break

    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/' or operacao == '%':
        
        x = int(input('Digite o primeiro valor: '))


        y = int(input('Digite o segundo valor: '))


        if operacao == '+':
            result = x + y

        elif operacao == '-':
            result = x - y

        elif operacao == '*':
            result = x * y

        elif operacao == '/':
            result = x / y

        elif operacao == '%':
            result = (x * (y/100))

        else:
            print('Operação Invalida')


        print(result)
        
        input('Precione ENTER')
        os.system('cls')
        
    else:
        print('Operação Invalida')
        input('Precione ENTER')
        os.system('cls')
import questionary

def ler_inteiro(mensagem):
    while True:
        try:
            return int(questionary.text(mensagem).ask())
        except ValueError:
            print('[ERRO] Digite um número inteiro válido.')


print('Calculadora Simples\n')

while True:
    op = questionary.select(
        'Qual operação deseja utilizar?',
        choices=[
            'Adição',
            'Subtração',
            'Multiplicação',
            'Divisão'
        ],
    instruction='(Use as setas do teclado)').ask()

    n1 = ler_inteiro('Digite o primeiro valor: ')
    n2 = ler_inteiro('Digite o segundo valor: ')

    match op:
        case 'Adição':
            print(f'\n{n1} + {n2} = {n1 + n2}\n')
        case 'Subtração':
            print(f'\n{n1} - {n2} = {n1 - n2}\n')
        case 'Multiplicação':
            print(f'\n{n1} * {n2} = {n1 * n2}\n')
        case 'Divisão':
            print(f'\n{n1} / {n2} = {n1 / n2:.1f}\n')

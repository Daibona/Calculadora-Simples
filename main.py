import questionary

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

    n1 = int(questionary.text('Digite o primeiro valor: ').ask())
    n2 = int(questionary.text('Digite o segundo valor: ').ask())

    match op:
        case 'Adição':
            print(f'\n{n1} + {n2} = {n1 + n2}\n')
        case 'Subtração':
            print(f'\n{n1} - {n2} = {n1 - n2}\n')
        case 'Multiplicação':
            print(f'\n{n1} * {n2} = {n1 * n2}\n')
        case 'Divisão':
            print(f'\n{n1} / {n2} = {n1 / n2:.1f}\n')

import random
import questionary

def jogar():

    while True:
        n_secreto = random.randint(1, 100)
        acertou = False
        tentativas = 0
        dificuldade = questionary.select(
            'Qual dificuldade deseja jogar?',
            choices=['Fácil', 'Médio', 'Difícil'],
            instruction='(Use as setas)'
        ).ask()

        qtd_tentativas = 0

        match dificuldade:
            case 'Fácil':
                qtd_tentativas += 60
            case 'Médio':
                qtd_tentativas += 30
            case 'Difícil':
                qtd_tentativas += 15

        while not acertou:
            print(f'Você tem {qtd_tentativas} tentativas.')
            while True:
                chute = input('Digite um número entre 1 e 100: ')
                print('\n')
                try:
                    tipo = int(chute)
                    qtd_tentativas -= 1
                    break
                except ValueError:
                    print('[ERRO] Digite um valor inteiro.')

            tentativas += 1

            if tipo == n_secreto:
                print(f'Parabéns o número é {tipo}, você acertou com {tentativas} tentativas!\n')
                break
            elif tipo > n_secreto:
                print('O número secreto é menor...')
            else:
                print('O número secreto é maior.')

            if qtd_tentativas == 0:
                print(f'Derrota! O número correto era {n_secreto}.\n')
                break


print('\nJogo da Adivinhação\n')

jogar()

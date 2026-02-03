import random
import questionary
import time
import sys

def animacao_carregando(tentativas):
    print('Rolando dado', end='')
    for _ in range(tentativas):
        for pontos in range(4):
            sys.stdout.write(f'\rRolando dado{'.' * pontos}')
            sys.stdout.flush()
            time.sleep(0.5)

print('Simulador de dado')
print('Role um dado de 6 lados!\n')

while True:
    dado = random.randint(1, 6)
    press = questionary.press_any_key_to_continue('Pressione qualquer tecla para rolar o dado').ask()
    animacao_carregando(1)
    print(f'\rNúmero {dado}!        ')


import random
import platform
import os
x = platform.system()

if x == 'Linux':
    cls = 'clear'
else:
    cls = 'cls'


jokepon = ['pedra','papel','tesoura']

def menu():
    print(''' Seja Bem-vindo ao Jokepon\n
Escolhar uma opcao entre:\n
Pedra\n
Papel\n
Tesoura\n''')
    jogador = input("Oque voce quer jogar?\n")
    jogador = jogador.lower()
    if jogador != 'pedra' and jogador != 'papel' and jogador != 'tesoura':
        jogador = menu()
    os.system(cls)   
    return jogador
def computerchoice():
    computer = random.choice(['pedra','papel','tesoura'])
    return computer

def win_condition(jogador, computer):
    if jogador == computer:
        return 'empate\n'
    elif (jogador == 'pedra' and computer == 'tesoura') or (jogador =='papel' and computer == 'pedra') \
            or (jogador == 'tesoura' and computer == 'papel'):
        return 'Voce ganhou\n'
    else:
        return 'Voce perdeu\n'
def game():
    while True:
        jogador = menu()
        computer = computerchoice()
        print(f'Voce escolheu: {jogador}')
        print(f'Computador escolheu: {computer}')
        print(win_condition(jogador,computer))
        sair = input('''Se deseja sair digite "sair" e aperte "Enter", caso deseja continuar aperte "Enter".
se voce digitar qualquer coisa diferente de "sair", vai ser considerado que quer continuar.\n''')
        if sair.lower()=='sair':
            exit()
        os.system(cls)

if __name__=='__main__':
    game()




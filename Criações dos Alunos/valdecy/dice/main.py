import platform
import os
import time
import random

list = ['1','2','3','4','5','6']

x = platform.system()

if x == 'Linux':
    cls = 'clear'
if x == 'Windows':
    cls = 'cls'


def rolar_dado():
    dice = random.randint(1, 6)
    return dice

def verificar(numero):
    for n in list:
        if numero == n:
            return True

    return False

def menu():
    while True:
        print("Voce me diz um numero entre 1 e 6, irei rolar o dado e veremos se voce acertou ou nao.")
        numero = input("Me fale um numero de 1 a 6\n")
        if verificar(numero):
            numero = int(numero)
            return numero
        else:
            print('voce nao digitou um numero entre 1 e 6')
            time.sleep(2)
            os.system(cls)
def start():
    numero = menu()
    dado = rolar_dado()
    print(f'Voce escolheu o numero: {numero}')
    print(f'Joguei o dado e deu: {dado}')

    if numero == dado:
        print('Voce acertou')
    else:
        print('Voce errou')
    time.sleep(3)

if __name__ == "__main__":
    start()

import platform 
import os
import time
from pa import Pa

list = ['1','2','3','4','5','6','7','8','9','0']

x = platform.system() # X vai receber a informaçao de qual sistema operacional

if x == 'Linux':
    cls = 'clear'
else:
    cls = 'cls'

def tratarTermo(x):
    verificar = []
    if x == '':
        x = None
        return x
    else:
        for i in range(len(x)):
            if i == 0 and x[i] == '-':
                verificar.append(1)
            else:
                for n in list:
                    if x[i] == n:
                        verificar.append(1)
        if len(verificar) == len(x):
            x = float(x)
            return x
        else:
            return 'termo digitado não é valido'

def entrarTermos():
    xi = input('Digite o termo de menor posicao conhecida: ')
    xi = tratarTermo(xi)
    i = input('Digite a posicao desse termo: ')
    i = tratarTermo(i)
    xn = input('Digite o termo de maior posicao conhecida: ')
    xn = tratarTermo(xn)
    n = input('Digite a posicao desse termo: ')
    n = tratarTermo(n)
    sn = input('Digite o Somatorio da PA ate os dois termos digitados acima: ')
    sn = tratarTermo(sn)
    r = input('Digite a raiz da PA: ')
    r = tratarTermo(r)

    pa = Pa(xi,i,xn,n,sn,r)
    
    return pa

def menu():
    print('Instrucoes basica')
    print('* Caso nao saiba a informacao perguntada sobre a PA aperte "Enter"')
    print('* Na primera vez que entrar ou quiser mudar os termos de uma PA va na opcao "1"')
    print('* Caso nos termos descobertos apareca "None", significa que nao foi posivel encontrar a informacao')
    input('Aperte "Enter" para continuar')
    os.system(cls)
    while True:
        print('Bem vindo ao Paprogram, escolha uma das opcoes abaixo')
        print('1- Entrar com os termos conhecidos de uma pa')
        print('2- Mostrar termos descobertos de uma pa')
        print('3- Mostrar a sequencia da PA informada de I a N')
        print('5- Sair')
        aux = input('Digite o valor da opcao: ')
        if aux == '1':
            os.system(cls)
            pa = entrarTermos()
            pa.encontrarTermos()
        elif aux == '2':
            os.system(cls)
            print(f'Os termos da sua Pa é:\n{pa}')
            input('Aperte "Enter" para continuar')
        elif aux == '3':
            os.system(cls)
            pa.sequenciaDaPa()
            print(pa.sequencia)
            input('Aperte "Enter" para continuar')
            os.system(cls)
        elif aux == '5':
            break

def main():
    pass

if __name__ == "__main__":
    menu()

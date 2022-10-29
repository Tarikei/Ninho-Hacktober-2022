
''' 
    Classe que guarda as informaçoes de uma PA 
    
    Class representing of an arithmetic progression

'''

from dataclasses import dataclass

@dataclass
class Pa:

    xi: float 
#xi == O valor do termo de menor posição conhecido de uma PA, The value of a member with the smallest known position of an AP
    i: float
# i == A posicao desse termo na PA, The position of this term in the AP
    xn: float
# xn == O valor do termo de maior posição conhecido de uma PA, the value of a member with the highest known position of an AP  
    n: float
# n == A posicao desse termo na PA, The position of this term in the AP 
    sn: float
#sn == o Somatorio de i ate n, The sum of terms from I to N
    r: float
#r == raiz da PA , difference of successive members
    def __post_init__(self):
        self.sequencia = []

    def encontrarXi(self):
        if self.i != None and self.xn != None and self.n != None and self.r != None:
            self.xi = self.xn - self.r*(self.n - self.i)
        elif self.sn != None and self.xn != None and self.n != None:
            self.xi = ((self.sn*2)/self.n)-self.xn
        else:
            print('Não é possivel achar o valor de xi, pois falta informacao')

    def encontrarI(self):
        if self.xi != None and self.xn != None and self.n != None and self.r != None:
            self.i = ((self.xn - self.xi)/self.r) - self.n
        else:
            print('Não é possivel achar o valor de i, pois falta informacao')

    def encontrarXn(self):
        if self.xi != None and self.i != None and self.n != None and self.r != None:
            self.xn = self.xi - (self.r*(self.n - self.i))
        elif self.xi != None and self.i != None and self.n != None and self.sn != None:
            self.xn = ((self.sn*2)/self.n) - self.xi
        else:
            print('Não é possivel achar o valor de xn, pois falta informacao')

    def encontrarN(self):
        if self.xi != None and self.i != None and self.xn != None and self.r != None:
            self.n = ((self.xn-self.xi)/self.r)- self.i
        elif self.sn != None and self.xi != None and self.xn != None:
            self.n = ((self.sn*2)/(self.x1+self.xn))
        else:
            print('Não é possivel achar o valor de n, pois falta informacao')

    def encontrarSn(self):
        if self.xi != None and self.xn != None and self.n != None:
            self.sn = (((self.xi + self.xn)*self.n)/2)
        else:
            print('Não é possivel achar o valor do sn, pois falta informacao')

    def encontrarR(self):
        if self.xn != None and self.xi != None and self.n != None and self.i != None: 
            self.r = (self.xn - self.xi)/(self.n-self.i)
        else:
            print('Não é possivel achar o valor de r, pois falta informacao')
    
    def encontrarTermos(self):
        if self.xi == None:
            self.encontrarXi()
        if self.i == None:
            self.encontrarI()
        if self.xn == None:
            self.encontrarXn()
        if self.n == None:
            self.encontrarN()
        if self.sn == None:
            self.encontrarSn()
        if self.r == None:
            self.encontrarR()

    def sequenciaDaPa(self):
        aux = self.i
        self.sequencia.append(self.i)
        while aux < self.n:
            self.sequencia.append(self.xi+(self.r*aux))
            aux+= 1


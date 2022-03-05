from math import sqrt
from typing import Text
class Contas():
    def deixarnativoepositivo(self,a:float):
        self.numero=float(a)
        self.resultado=float(a*-1)
        return self.resultado
    def somar(self,a:float,b:float):
        self.somar1=float(a)
        self.somar2=float(b)
        self.resultado=float(self.somar1+self.somar2)
        return self.resultado
    def dividir(self,a:float,b:float):
        self.dividir1=float(a)
        self.dividir2=float(b)
        self.resultado=float(a/b)
        return self.resultado
    def multiplicar(self,a:float,b:float):
        self.multiplicar1=float(a)
        self.multiplicar2=float(b)
        self.resultado=float(a*b)
        return self.resultado
    def multiplicarresultado(self,c:float):
        self.resultado=float(self.resultado*c)
    def substrair(self,a:float,b:float):
        self.substrair1=float(a)
        self.substrair2=float(b)
        self.resultado=float(a-b)
        return self.resultado
    def substrairresutado(self,c:float):
        self.resultado=float(self.resultado-c)
        return self.resultado
    def raizquadrada(self,a:float):
        self.resultado=float(sqrt(a))
        return self.resultado
    def raizcomresutado(self):
        self.resultado=float(sqrt(self.resultado))
        return self.resultado
    def potenciacao(self,a:float,b:float):
        self.resultado=float(a**b)
        return self.resultado
    def potenciacomresultado(self):
        self.resultado=float(self.resultado**self.resultado)
        return self.resultado
    def calcularporcentagem(self,a:float,b:float):
        self.numeroporcento=float(a)
        self.porcento=float(b)
        self.resultado=float(a*b/100)
        return self.resultado

teste=Contas()
print(teste.somar(1,4))
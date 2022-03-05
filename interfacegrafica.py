from tkinter import*
from calcular1 import Contas
import string
import re
root=Tk()
class calcular(Contas):
    def igual(self):
        self.segundonumero=self.escrever.get()
        self.escrever.delete(0,END)
        if self.matematica=='soma':
            self.numero02=float(self.segundonumero)
            self.tela=self.somar(self.numero,self.numero02)
            self.escrever.insert(0,self.tela)
        if self.matematica=='divisao':
            self.numero02=float(self.segundonumero)
            self.tela=self.dividir(self.numero,self.numero02)
            self.escrever.insert(0,self.tela)
        if self.matematica=='multiplicacao':
            self.numero02=float(self.segundonumero)
            self.tela=self.multiplicar(self.numero,self.numero02)
            self.escrever.insert(0,self.tela)
        if self.matematica=='divisao':
            self.numero02=float(self.segundonumero)
            self.tela=self.dividir(self.numero,self.numero02)
            self.escrever.insert(0,self.tela)
        if self.matematica=='subtracao':
            self.numero02=float(self.segundonumero)
            self.tela=self.substrair(self.numero,self.numero02)
            self.escrever.insert(0,self.tela)
        if self.matematica=='pontencia':
            self.numero02=float(self.segundonumero)
            self.tela=self.potenciacao(self.numero,self.numero02)
            self.escrever.insert(0,self.tela)
        if self.matematica=='porcentagem':
            self.numero02=float(self.segundonumero)
            self.tela=self.calcularporcentagem(self.numero,self.numero02)
            self.escrever.insert(0,self.tela)
        
    def deixarnagativoepositivo1(self):
        self.pegaronumero=self.escrever.get()
        self.numero=float(self.pegaronumero)
        self.escrever.delete(0,END)
        self.verificar=self.deixarnativoepositivo(self.numero)
        self.escrever.insert(0,self.verificar)
        if  self.numero=='-':
            self.escrever.insert(0,self.numero)
    def deixarnagativoepositivo2(self):
        self.segundonumero=self.escrever.get()
        self.numero02=float(self.segundonumero)
        self.escrever.delete(0,END)
        self.verificar=self.deixarnativoepositivo(self.numero02)
        self.escrever.insert(0,self.numero02)
        if self.numero02=='-':
            self.escrever.insert(0,self.numero02)
    def dividirpor1(self):
        self.pegaronumero=self.escrever.get()
        self.matematica='dividepor1'
        self.numero=float(self.pegaronumero)
        self.escrever.delete(0,END)
        self.escrever.insert(0,1/self.numero)
    def raiz(self):
        self.pegaronumero=self.escrever.get()
        self.matematica='raiz'
        self.numero=float(self.pegaronumero)
        self.escrever.delete(0,END)
        self.tela=self.raizquadrada(self.numero)
        self.escrever.insert(0,self.tela)
    def apagar(self):
        self.escrever.delete(0,END)
    def apagarnumero1(self):
        self.pegaronumero=self.escrever.get()
        self.numero=float(self.pegaronumero)
        self.apagar1='true'
        self.escrever.delete(0,END)
    def apagarnumero2(self):
        self.segundonumero=self.escrever.get()
        self.numero02=float(self.segundonumero)
        self.apagar1='true'
        self.escrever.delete(0,END)
    def apagarumnumero(self):
        self.escrever.delete(len(self.escrever.get())-1,END)
    def divisao1(self):
        self.pegaronumero=self.escrever.get()
        self.matematica='divisao'
        self.numero=float(self.pegaronumero)
        self.escrever.delete(0,END)
    def multiplicacao1(self):
        self.pegaronumero=self.escrever.get()
        self.matematica='multiplicacao'
        self.numero=float(self.pegaronumero)
        self.escrever.delete(0,END)
    def subtracao1(self):
        self.pegaronumero=self.escrever.get()
        self.matematica='subtracao'
        self.numero=float(self.pegaronumero)
        self.escrever.delete(0,END)
    def ponteciacao1(self):
        self.pegaronumero=self.escrever.get()
        self.matematica='pontencia'
        self.numero=float(self.pegaronumero)
        self.escrever.delete(0,END)
    def somar1(self):
        self.pegaronumero=self.escrever.get()
        self.matematica='soma'
        self.numero=float(self.pegaronumero)
        self.escrever.delete(0,END)
    def porcentagem(self):
        self.pegaronumero=self.escrever.get()
        self.matematica='porcentagem'
        self.numero=float(self.pegaronumero)
        self.escrever.delete(0,END)
    def clicar(self,numero):
        self.pegarasinformacoes=self.escrever.get()
        self.escrever.delete(0,END)
        self.escrever.insert(END,str(self.pegarasinformacoes)+str(numero))
    def virgula(self):
        self.escrever.insert(END,'.')
class TelaCalculadora(calcular):
    def __init__(self) -> None:
        self.root=root
        self.configtela()
        self.frame()
        self.botaonumero()
        self.botaosimbulo()
        self.digitar()
        root.mainloop()
    def configtela(self):
        self.root.title('calculadora')
        self.root.config(background='#7B68EE')
        self.root.geometry('700x600')
        self.root.resizable(True,True)
        self.root.minsize(width=700,height=600)
    def frame(self):
        self.framecalculadora=Frame(self.root,bd=2,bg='#F5F5F5',highlightbackground='#000000',highlightthickness=2)
        self.framecalculadora.place(relx=0.08,rely=0.06,relwidth=0.8,relheight=0.9)
    def botaonumero(self):
        self.numero8=Button(self.framecalculadora,text='8',command=lambda: self.clicar('8'))
        self.numero8.place(relx=0.09,rely=0.23,relwidth=0.05)
        self.numero7=Button(self.framecalculadora,text='7',command=lambda:self.clicar('7'))
        self.numero7.place(relx=0.012,rely=0.23,relwidth=0.05)
        self.numero9=Button(self.framecalculadora,text='9',command=lambda:self.clicar('9'))
        self.numero9.place(relx=0.17,rely=0.23,relwidth=0.05)
        self.numero4=Button(self.framecalculadora,text='4',command=lambda:self.clicar('4'))
        self.numero4.place(relx=0.012,rely=0.30,relwidth=0.05)
        self.numero5=Button(self.framecalculadora,text='5',command=lambda:self.clicar('5'))
        self.numero5.place(relx=0.09,rely=0.30,relwidth=0.05)
        self.numero6=Button(self.framecalculadora,text='6',command=lambda:self.clicar('6'))
        self.numero6.place(relx=0.17,rely=0.30,relwidth=0.05)
        self.numero1=Button(self.framecalculadora,text='1',command=lambda:self.clicar('1'))
        self.numero1.place(relx=0.012,rely=0.37,relwidth=0.05)
        self.numero2=Button(self.framecalculadora,text='2',command=lambda:self.clicar('2'))
        self.numero2.place(relx=0.09,rely=0.37,relwidth=0.05)
        self.numero3=Button(self.framecalculadora,text='3',command=lambda:self.clicar('3'))
        self.numero3.place(relx=0.17,rely=0.37,relwidth=0.05)
        self.numero0=Button(self.framecalculadora,text='0',command=lambda:self.clicar('0'))
        self.numero0.place(relx=0.09,rely=0.44,relwidth=0.05)
    def botaosimbulo(self):
        self.simbuloporcento=Button(self.framecalculadora,text='%',command=self.porcentagem)
        self.simbuloporcento.place(relx=0.012,rely=0.07,relwidth=0.06)
        self.simbuloCE=Button(self.framecalculadora,text='CE',command=self.apagar)
        self.simbuloCE.place(relx=0.09,rely=0.07,relwidth=0.06)
        self.simbuloC=Button(self.framecalculadora,text='C',command=lambda:[self.apagarnumero1(),self.apagarnumero2()])
        self.simbuloC.place(relx=0.17,rely=0.07,relwidth=0.06)
        self.simbuloApagar=Button(self.framecalculadora,text='<--',command=self.apagarumnumero)
        self.simbuloApagar.place(relx=0.25,rely=0.07,relwidth=0.06)
        self.simbulo1x=Button(self.framecalculadora,text='1/x',command=self.dividirpor1)        
        self.simbulo1x.place(relx=0.012,rely=0.15,relwidth=0.06)
        self.simbuloxelevadoa2=Button(self.framecalculadora,text='x²',command=self.ponteciacao1)
        self.simbuloxelevadoa2.place(relx=0.09,rely=0.15,relwidth=0.06)
        self.simbuloraizquadrada=Button(self.framecalculadora,text='²√',command=self.raiz)
        self.simbuloraizquadrada.place(relx=0.17,rely=0.15,relwidth=0.06)
        self.simbulodividir=Button(self.framecalculadora,text='÷',command=self.divisao1)
        self.simbulodividir.place(relx=0.25,rely=0.15,relwidth=0.06)
        self.simbuloX=Button(self.framecalculadora,text='x',command=self.multiplicacao1)
        self.simbuloX.place(relx=0.25,rely=0.23,relwidth=0.06)
        self.simbulosbtrair=Button(self.framecalculadora,text='-',command=self.subtracao1)
        self.simbulosbtrair.place(relx=0.25,rely=0.30,relwidth=0.06)
        self.simbulosomar=Button(self.framecalculadora,text='+',command=self.somar1)
        self.simbulosomar.place(relx=0.25,rely=0.37,relwidth=0.06)
        self.simbulorpositivoenegativo=Button(self.framecalculadora,text='+/-',command=lambda:[self.deixarnagativoepositivo1(),self.deixarnagativoepositivo2()])
        self.simbulorpositivoenegativo.place(relx=0.012,rely=0.44,relwidth=0.06)
        self.simbulovirgula=Button(self.framecalculadora,text='.',command=self.virgula)
        self.simbulovirgula.place(relx=0.17,rely=0.44,relwidth=0.06)
        self.simbuloigual=Button(self.framecalculadora,text='=',command=self.igual)
        self.simbuloigual.place(relx=0.25,rely=0.44,relwidth=0.06)
    def digitar(self):
        self.escrever=Entry(self.framecalculadora)
        self.escrever.place(relx=0.012,rely=0.01,relwidth=0.3)
teste=TelaCalculadora()
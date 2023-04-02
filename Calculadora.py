class calculadora:
    def __init__(self):
        self.entrada1=0
        self.entrada2=0
        self.calculo=0

    def soma (self):
        self.calculo=self.entrada1+self.entrada2

    def multiplicar(self):
        self.calculo=self.entrada1*self.entrada2

    def mostrarResultado(self):
        print("Valor do calculo é: "+str(self.calculo))

    def entradaNumero(self):
        self.entrada1=float(input("Digitar valor para entrada 1 "))
        self.entrada2=float(input("Digitar valor para entrada 2 "))

    def zerarCalculo(self):
        self.calculo=0

objCalcRafaela=calculadora()
objCalcRafaela.entradaNumero()
objCalcRafaela.soma()
objCalcRafaela.mostrarResultado()
objCalcRafaela.zerarCalculo()
class Conta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def deposito():
         print (f"Saldo inicial: {self.saldo}")
         self.saldo = self.saldo + valor
         primt(f"Saldo final :{self.saldo}")

    def saque ():
        pass
    def info ():
        print(f"Conta: {self.numeros} - {self.titular}- {self.saldo}")


class Banco:

    def __init__ (self) :
        self.contas={}

if __name__ == "__main__" :
    print(f"Criando a primeira conta")
    cc_1= Conta ("00001", "Felipe", 1500.20)
    #cc_1.inf()

    valor_deposito=float(input("digite o valor do deposito :"))
    #cc_1.deposito(100)
    cc_1.deposito(valor_deposito)

    valor_saque=float(input("Digite o valor do saque :"))
    #cc_1.deposito(100)
    cc_1.saque(valor_saque)



   
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca # Atributo
        self.modelo = modelo # atributo
        self.ano = ano # atributos
        self.ligado  = False # Atributos com valor padrão

    def exibir_info(self):

        if self.ligado == True :
            status = "ligado"
        else :
            status = " desligado"
        print(f"{self.marca} {self.modelo} ({self.ano}) está {status}")

if __name__ == "__main__" :
    print (f"Criando um objeto de classe carros")
    meu_carro = Carro("Toyota", "Corolla", 2020)
 
    meu_carro.exibir_info()

    def ligar (self):
        self.ligado = True
        #print (f"Ocarro está ligado")

    def desligar (self):
        self.ligado = False
         #print (f"Ocarro está desligado")

    #print(meu_carro)



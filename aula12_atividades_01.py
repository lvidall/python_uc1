class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def exibir_info(self):
        print(f"{self.marca} {self.modelo} ({self.ano}) ({self.cor})")


        


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas, cor, placa):
        super(). __init__(marca, modelo, ano, cor) #chama o construtor da superclasse
        self.portas = portas
        self.placa = placa

    def exibir_info(self):
        super().exibir_info() #Chama o método da superclasse
        print(f"Este carro tem {self.portas} portas.") 
        print(f"A placa do carro é {self.placa}")


# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020, 4, "preto", "ktz5462")
meu_carro.exibir_info()
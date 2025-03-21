import sys

def principal(parametros):
    for dado in parametros:
        print(dado)

def soma (numeros) :
    somatorio=0
    for valor in numeros:
        somatorio = somatorio + valor
    #print(f"o valor da soma dos números é {somatorio}")


if __name__ == "__main__":
   resultado=soma(sys.argv[1:])
   print(f"o valor da soma dos números é {somatorio}")
   

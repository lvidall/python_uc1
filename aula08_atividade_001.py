def saudacao():
    print("olá, seja bem vindo(a) ao curso de python")

def soma(a, b):
    return a + b

def testar_soma ():
    resultado = soma(5, 7)
    print("A soma é:", resultado)

if __name__=="__main__":
    #resultado=soma(sys.argv[1:])
    #print (f"o valor da soma dos números é {resultado}")
    testar_soma ()



def par_ou_impar(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
# Exemplo de chamada
print("O número 4 é", par_ou_impar(4))
print("O número 7 é", par_ou_impar(7))



def fatorial(n):
    if n < 0:
        return "Número inválido para fatorial."
    elif n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado
def testar_fatorial () :
    #Exemplo de chamada
    numero=int(input("\n\n\tinforme um numero"))
    resultado=fatorial(numero)
    print(f"\n\n\tfatorialde{numero} é iqual á {resultado}\n\n")

    #print("fatorial de 5; " , fatorial(5))
    if __name__=="__main__":
    #resultado=soma(sys.argv[1:])
    #print (f"o valor da soma dos números é {resultado}")
    






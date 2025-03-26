vetor_dados = [10, 20, 30, 40, 50]

def criar_imprimir_lista ():
    vetor = [10, 20, 30, 40, 50]
    print("Vetor:", vetor)

def interando_sobre_lista ():
    for elemento in vetor:
        print("Elemnto:", elemento)

def caucular_a_soma_do_elemento_do_vetor ():
    vetor = [10, 20, 30, 40, 50,]
    #passo2: Caucular a soma utilizando a função sum().
    soma = sum(vetor)
    #Passo3: imrpimir o resultado.
    print("Soma dos elementos:", soma)


def encontrar_o_maior_e_o_menor_valor_em_um_vetor ():
    vetor = [3, 7, 2, 9, 4]
    maior = max(vetor)
    menor = min(vetor)
    print("Maior valor:", maior)
    print("Menor valor:", menor)

def inverter_ordem_dos_elementos_de_vetor_sem_usar_reverse ():
     vetor = [1, 2, 3, 4, 5,]
     vetor_invertido = vetor[::-1]
     print("Vetor invertido:", vetor_invertido)

def multiplcar_cada_elemento_do_vetor_por_dois (vetor):
     multiplicador = 2
     vetor_mult = [elemento * multiplicador for elemento in vetor]
     print("Vetor multiplicado:", vetor_mult)

def contar_quantos_3_aparece():
    vetor = [1, 3, 3, 4, 3, 5]
    ocorrenias = vetor.cont(3)
    print("O valor 3 aparece", ocorrencias, "vezes". )

    def ordenar_um_vetor_em_ordem_cresceente():
        vetor + [5, 2, 9, 1, 5, 6]
        vetor_ordenado = sorted(vetor)
        print("Vetor ordenado:", vetor_ordenado)

if __name__ == "__main__" :

    # Ordenar um vetor em ordem crescente
    ordenar_um_vetor_em_ordem_cresceente
    
     


# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# def imprimir_elementos ():
#     print("Elemento (0,0):", matriz[0][0])
#     print("Elemento (2,1):", matriz[2][1])

# def imorimir_matriz ():
#     for linha in matriz:
#         print(f"|", end=" ")
#         for elemento in linha:
#             print(elemento, end= ' | ' )
#         print()

matriz_4_4 =[
    [1, 2, 3, 4],
    [9, 8, 7, 6],
    [6, 5, 4, 3],
    [1, 5, 7, 9]
]
soma = 0
for i in range(4):
    for j in range(i + 1, 4):
        soma += matriz_4_4[i][j]

print(f"Soma dos elementos acima da diagonal principal: {soma}")

    



"""
def ler_matriz_v1 ():    
     matriz = [[int(input(f"Digite o valor para [{i}][{j}]: ")) for j in range(4)] for i in range(4)]
for linha in matriz:
    print(linha)
     
def laço_de_repetição (matriz):
 matriz =[]
for i in range(4):
    linha = []
    for j in range(4):
        valor = int(imput(f"Digite o valor para [{i}][{j}]: "))
        linha.append(linha)
    matriz.append(linha)
for linha in matriz:
    print(linha)
"""


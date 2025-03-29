matriz_4_4 =[
    [1, 2, 3, 4],
    [9, 8, 7, 6],
    [16, 5, 14, 13],
    [11, 15, 17, 19]
]
# vet_pares=[]
# vet_impares=[]
# pares = 0
# impares = 0
# for i in range(4):
#     for j in range(4):
#         if matriz_4_4[i][j] % 2 == 0:
#             pares += 1
#             vet_pares.append(matriz_4_4[i][j])
#         else:
#             impares += 1
#             vet_impares.append (matriz_4_4[i][j])
# print(f"Quantidade de números pares:{pares}")
# print(f"Quantidade de numeros impares:{impares}")

# print(f"Os numero pares são : {vet_pares}")
# print(f"Os numeros impares são : {vet_impares}")








# for i in range(4):
#     maior = matriz_4_4[i][0]
#     for j in range(4):
#         if matriz_4_4[i][j] > maior:
#             maior = matriz_4_4[i][j]
#     print(f"Maior valor da da linha {i}; {maior}")


matriz_4_4 =[
    [1, 2, 3, 4],
    [9, 8, 7, 6],
    [16, 5, 14, 13],
    [11, 15, 17, 19]
]

num = int(input("Digite o número para a multiplicação: "))
linha_escolhida + int(imput("Digite a linha a ser multiplicada (0-3): "))

matriz_4_4[linha_escolhida] = [num * valor for valor in matriz_4_4[linha_escolhida]]
for linha in matriz_4_4:
    print(linha)

num = int(input("Digité o número para multiplicção: "))
linha_escolhida = int(input("Digite a linha a ser multiplicada (0-3): "))

for j in range(4):
    matriz_4_4[linha_escolhida][j] *= num

for linha in matriz_4_4:
    print(linha)







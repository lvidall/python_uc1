matriz_4_4 =[
    [1, 2, 3, 4],
    [9, 8, 7, 6],
    [6, 5, 4, 3],
    [1, 5, 7, 9]
]
pares = 0
impares = 0
for i in range(4):
    for j in range(4):
        if matriz_4_4[i][j] % 2 == 0:
            pares += 1 
            impares += 1
print(f"Quantidade de números pares:{pares}")
print(f"Quantidade de numeros impares:{impares}")







# for i in range(4):
#     maior = matriz_4_4[i][0]
#     for j in range(4):
#         if matriz_4_4[i][j] > maior:
#             maior = matriz_4_4[i][j]
#     print(f"Maior valor da da linha {i}; {maior}")

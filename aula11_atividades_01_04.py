aluno_1 = {"nome": "Arara", "notas": [5, 8, 9]}
aluno_2 = {"nome": "Luis", "notas": [6, 7, 5]}
aluno_3 = {"nome": "Felipe", "notas": [8, 6, 6]}

print(f"Dados o aluno 1 {aluno_1}")

print(f'As notas do aluno { aluno_1["nome"] }  são {aluno_1["notas"]}')

media = sum ( aluno_1["notas"] ) / len (aluno_1["notas"])
print (f'O aluno {aluno_1["nome"]} obteve media iqual a: {media}')
aluno_1["media"]=media
print (f"Dados do aluno 1 {aluno_1}")



# pessoa = {"nome": "Felipe", "idade": 30, "cidade": "petropolis" }
# pessoa["email"] = "felipe@email.com"
# pessoa["idade"] = 19
# del pessoa["cidade"]
# print(pessoa)

d3=d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

print (f"Dicionario originais:")
print (f" D1    : {d1}")
print (f" D2    : {d2}")

d1.update(d2)
d2.update(d3)

print (f"Dicionários Atualizados: ")
print (f" D1    : {d1}")
print (f" D1    : {d1}")

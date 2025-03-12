idade=int(input("informe a sua idade : "))
habilitado=input("possui carteirade habilitação <s/n> : ")
habilitado=habilitado.lower()

if (idade >= 18) and (habilitado == "s"):
    print("você pode dirigir")
else :
        print("você não pode dirigir")


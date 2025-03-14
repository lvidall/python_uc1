nome=input("informe a seu nome : ")
senha=input("informe uma senha com ao menos 6 caracteres")
if len(nome)<3:
    print("aceso negado: nome com menos de tres letras")
if len(senha)<6:
    print("aceso negado: senha com menos de 6 caracteres")
elif senha=="123456":
    print("acesso negado: senha fraca")
elif senha=="senha":
    print("acesso negado:senha fraca")
else:
    print("acesso permitido")



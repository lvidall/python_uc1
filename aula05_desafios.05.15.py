primeiro_lado=input("diga o tamanho dos seu triangulo e irei dizer qual é")
segundo_lado=input("tamanho do segundo")
terceiro_lado=input("tamanho do terceiro lado")

if (primeiro_lado==segundo_lado)and(primeiro_lado==terceiro_lado):
    print("seu triangulo é equilatero")
elif (primeiro_lado==segundo_lado)or(primeiro_lado==terceiro_lado)or(segundo_lado==terceiro_lado):
   print("seu triangulo é isósceles")
else:
    print("seu triangulo é escaleno")
    

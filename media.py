nota1 = float(input("Digite nota 1:"))
nota2 = float(input("Digite nota 2:"))
nota3 = float(input("Digite nota 3:"))

media = ((nota1 + nota2 + nota3)/3)

print(media)

if media >= 6:
    print("Aprovado")
elif media >= 4:
    print("Recuperacao")
else:
    print("Reprovado")


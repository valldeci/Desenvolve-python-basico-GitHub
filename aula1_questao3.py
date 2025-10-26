# lê  notas
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

# calcula 
m = (n1 + n2 + n3) / 3

# verifica 
if m >= 60:
    print("Aprovado")
elif m >= 40:
    print("Recuperação")
else:
    print("Reprovado")

print("Fim")
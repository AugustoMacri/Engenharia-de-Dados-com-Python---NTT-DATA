curso = "Python"

print(curso.upper())
print(curso.lower())
print(curso.title())

curso1 = "  python  "
print(curso1.strip())
print(curso1.lstrip())
print(curso1.rstrip())

curso2 = "java"
print(curso2.center(15, "!"))
print(".".join(curso2))

print(f"ola estou estudando o curso {curso}, mas depois vou estudar o curso {curso2}")

nome = "Augusto Macri"
print(nome[0:5])
print(nome[0:9:2]) #o 2 é o passo, pegar de dois em dois
print(nome[::-1]) #espelhando string

mensagem = f"""
ola meu nome é augusto, e estou
estudando python focado em engenharia de 
dados"""

print(mensagem)
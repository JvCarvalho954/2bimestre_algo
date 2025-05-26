compras = []
uinput = ""
produto = ""

while uinput.upper() != "SAIR":
    print("--------------------------")
    for item in compras:
        print(f"- {item}")
    uinput = input("Deseja adicionar ou remover?\n + : adicionar\n - : remover\n sair : para sair\n")
    if uinput == "+":
        produto = input("Insira o nome do produto para adicionar:\n")
        compras.append(produto)
    if uinput == "-":
        produto = input("insira o nome do produto para remover:\n(Escreva perfeiamente igual o nome da lista)\n")
        compras.remove(produto)

for i in compras:
        print(f"- {i}")
compras = ["pao", "café", "leite"]
print(compras)

# pode ser removido pelo nome do produto ou pelo indice
# compras.remove("café")
compras.remove(compras[1])
print(compras)

# Append acrescenta um item no final da lista, só pode adicionar um por vez
compras.append("açicar")
print(compras)

# É preciso criar um alista nova para receber os elementos ordenados da lista antiga
compras_ordenadas = sorted(compras)
print(compras_ordenadas)

for item in compras:
    print("-",item)
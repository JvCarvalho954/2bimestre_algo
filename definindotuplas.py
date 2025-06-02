numero = (5,8,12,8,7,8,3)
#para ser uma tupla precisa estar entre parenteses
print("tupla original: ", numero)
#imprimindo para o usuario a tupla original, sem manipulações
print("tamanho da tupla: ",len(numero))
print(numero[2])
print("fazendo o slicing do 2 ao 5", numero[2:5])
#o slicing ele não pega o ultimo item definido no recorte
print("quantas vezes o numero 8 repete: ", numero.count(8))
print("primeira ocorrencia do número 7: ", numero.index[7])

minimo_tupla = min(numero)
print("menor número dentro da tupla: ", minimo_tupla)
maximo_tupla = max(numero)
print("maior número detro da tupla: ", maximo_tupla)
soma_tupla = sum(numero)
print("a soma de todos os números dentro de uma tupla: ", soma_tupla)
print("O numero 4 está na upla?", 4 in numero)
numero2 = (15,20)
tupla_concatenada = numero+numero2
print("a concatenação das tuplas 1 e 2 resulta na nova tupla: ", tupla_concatenada)
tupla_duplicada = numero*2
#okyuu
print(tupla_duplicada)

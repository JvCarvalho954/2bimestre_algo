pacotes = ("ABC123", "Enviado"), ("XYZ789", "Recebido"), ("DEF456","Em transito"), ("JKL321", "Enviado"), ("MNO654", "Recebido"), ("PQR987", "Em transito")
enviado = 0
recebido = 0
transito = 0
codtrans = []
for i in range(0, len(pacotes)):
    if "Enviado" in pacotes[i][1]:
        enviado+=1
    if "Recebido" in pacotes[i][1]:
        recebido+=1
        codtrans.append(pacotes[i][0])
    if "Em transito" in pacotes[i][1]:
        transito+=1
print(f"Pacotes enviados: {enviado} \nPacotes Recebidos: {recebido} \nPacotes em transito: {transito}")
print(f"Código dos pacotes em transito: {codtrans}")

def check(cod):
    for i in range(0,len(pacotes)):
        if cod in pacotes[i]:
            print("Status: ",pacotes[i][1])

uinput = input("Insira o código de rastreamento para receber estatus: ")
check(uinput)
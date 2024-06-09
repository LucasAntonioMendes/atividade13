peso = float(input("Qual seu peso :"))
altura = float(input("Qual sua altura :"))


imc = peso / (altura*altura)

print("seu imc é{:.2f}".format(imc))

if imc <= 18.4:
    print("Em estado de magresa")
elif imc >18.5:
    print("Em estado de sobre peso")
elif imc >= 30:
    print("Em estado de obesidade")
else:
    print("Seu peso esta ideal")
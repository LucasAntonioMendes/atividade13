senha1 = 40028922

user = str(input("Qual user está logando?: "))
senha = int(input("Qual é sua senha: "))

while senha != senha1 :
    senha =int(input("senha incorreta digite novamente: "))

print("Seja bem vindo",user)   
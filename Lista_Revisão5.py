# Combo 5

def numero(n):
    lista = []
    if n == 1:
        lista = [1]
    elif n >= 2:
        lista = [1,1]    
        for termo in range(n - 2):
            termo = lista[-2] + lista[-1]
            lista.append(termo)
      
    
    return lista
str_numero = int(input("Digite a quantidade de termos da sequência que vc deseja:"))
x = input("Deseja imprimir a sequência?(S/N)")
if x.upper() == "S":
    print("A sequência é:",numero(str_numero))
else:
    print("Programa Encerrado!")




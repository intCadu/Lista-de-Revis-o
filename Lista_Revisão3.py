# Combo 3

def oração(palavra):
    contador = 0
    for palavra in lista:
        if len(palavra) >= 5:
            contador += 1
    print(f"Existem {contador} palavras com mais de 5 letras!")
    return contador
    



lista = []
quantidade = int(input("Digite a quantidade de termos:"))
for i in range(quantidade):
    str_plavra = input("Digite uma palavra:")
    lista.append(str_plavra)
while True:    
    x = input("Deseja adicionar mais palavras a lista?(S/N)")
    if x.upper() == "S":
        str_plavra = input("Digite uma palavra:")
        lista.append(str_plavra)
        
    else:
        break 

oração(lista)
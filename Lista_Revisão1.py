# Combo 1

# contador = 0
# lista_int = []
# quantidade = int(input("Digite a quantidade de termos dessa lista:"))

# for i in range(quantidade):
#     termo = int(input("Digite os termos da lista:"))
#     lista_int.append(termo)
    
# x = str(input("Deseja somar os termos pares da lista?(S/N)"))

# if x.upper() == "S": 
#     for i in lista_int:
#         if i % 2 == 0:
#             contador += i
#     print("Sua lista é:", lista_int)
#     print("A soma dos termos é:",contador)
# else:
#     print("PROGRAMA ENCERRADO!")

        

def palavra(palindromo):
    lista = palindromo
    lista2 = lista
  
    lista2.reverse()
    print(lista2)
    


str_palavra = str(input("Digite uma palavra:"))
palavra(str_palavra)

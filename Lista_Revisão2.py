# Combo 2

def palavra(palindromo):
    
        palavraNormal = palindromo
        palavraInversa = palavraNormal[::-1]
        if palavraNormal == palavraInversa:
            print("É um palíndromo!")
        else:
            print("Não é um palíndromo!")
            
while True:        
    str_palavra = (input("Digite uma palavra:"))
    if str_palavra.isnumeric():
         break
    else:
        palavra(str_palavra)
    
   
   
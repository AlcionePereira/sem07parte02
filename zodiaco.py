def zodiaco(d,m):
    if d >= 21 and m == 3:
        return 'Áries'

    
    elif d <= 19 and m == 4:
        return 'Áries'

    
    elif d >= 20 and m == 4:
        return'Touro'

    
    elif d <= 20 and m == 5:
        return'Touro'

    
    elif d >= 21 and m  == 5:
        return'Gêmeos'

    
    elif d <= 21 and m == 6:
        return 'Gêmeos'

    
    elif d >= 22 and m == 6:
        return 'Câncer'

    
    elif d <= 22 and m == 7:
        return'Câncer'

    
    elif d >= 23 and m == 7:
        return"Leão"

    
    elif d <= 22 and m == 8:
        return'Leão'

    
    elif d >= 23 and m == 8:
        return'Virgem'

    
    elif d <= 22 and m == 9:
        return'Virgem'

    
    elif d >= 23 and m == 9:
        return'Libra'

    
    elif d <= 22 and m == 10:
        return'Libra'

    
    elif d >= 23 and m == 10:
        return"Escorpião"

    
    elif d <= 21 and m == 11:
        return"Escorpião"

    
    elif d >= 22 and m == 11:
        return'Sagitário'

    
    elif d <= 21 and m == 12:
        return"Sagitário"

    
    elif d >= 22 and m == 12:
        return'Capricórnio'

    
    elif d <= 19 and m == 1:
        return'Capricórnio'

    
    elif d >= 20 and m == 1:
        return'Aquário'

    
    elif d <= 18 and m == 2:
        return"Aquário"

    
    elif d >= 19 and m == 2:
        return'Peixes'

    
    elif d <= 20 and m == 3:
        return'Peixes'
        

def main():

    
    #Entrada de dados
    dia = int(input().strip())
    mes = int(input().strip())

    #processamento chamando a função
    resultado = zodiaco(dia,mes)

    #Saída de dados
    print(resultado)


if __name__== '__main__':
    main()

















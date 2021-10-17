def ordem_crescente(n,n2,n3):
    if n > n2 and n2 > n3:
        return'{}\n{}\n{}'.format(n3,n2,n)

    elif n > n3 and n3 > n2:
        return'{}\n{}\n{}'.format(n2,n3,n)

    elif n < n2 and n2 < n3:
        return'{}\n{}\n{}'.format(n,n2,n3)

    
    elif n > n2 and n2 < n3:
        return'{}\n{}\n{}'.format(n2,n,n3)
    elif n < n2 and n2 >n3:
        return'{}\n{}\n{}'.format(n3,n,n2)

def main():

    
    #Entrada de dados
    n1 = int(input().strip())
    nu2 = int(input().strip())
    nu3 = int(input().strip())
    #processamento chamando a função
    resultado = ordem_crescente(n1, nu2, nu3)
    #Saída de dados
    print(resultado)

if __name__== '__main__':
    main()





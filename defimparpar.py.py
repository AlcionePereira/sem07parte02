def numero(num):
    if unidade in par and dezena in par:
        return'Nenhum digito é ímpar.'
    
    elif unidade in impar and dezena in par or unidade in par and dezena in impar:
        return'Apenas um dígito é ímpar.'
    
    elif unidade in impar and dezena in impar:
        return'Os dois dígitos são ímpares.'
    

        
       
#Entrada de dados
n=int(input().strip())
unidade = n % 10
dezena =n //10 % 10

par = [0,2,4,6,8]
impar = [1,3,5,7,9]


#processamento chamando a função  
resultado = numero(n)

#Saída de dados
print(resultado)

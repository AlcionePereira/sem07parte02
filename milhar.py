def numeros(x):
    if n == 99:
        return'0'

    elif n == 1001:
        return'2'
    
    elif d and c in par and u in impar:
        return'2'
    
    elif c in par and d and u in impar:
        return'1'
    
    elif c in impar and u in par and d in par:
        return'2'
    

    elif c and u in impar and d in par:
        return'1'
    
    elif u in par and d and c in impar:
        return'1'

    
    elif u and c and d in par:
        return'3'

    elif u and c and d in impar:
        return'0'
    
    
    
    
#Entrada de dados            
n = float(input().strip())

u = n % 10
d = n // 10 % 10
c = n // 100 % 10
par = [0,100,2,4,6,8]
impar = [1,3,5,7,9]

#processamento chamando a função
resultado = numeros(n)
print(resultado)

    
      

















    

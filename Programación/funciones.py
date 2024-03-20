def es_primo(numero):
    if numero==2:
        return True
    else:
        for i in range(2,int(numero**(1/2))):
            if numero%i==0:
                return False
            return True


n=int(input("Ingresa un número -> "))
if es_primo(n):
    n=n+100
    print(n)
else:
    print(n+1)
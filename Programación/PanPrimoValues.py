import sys

while True:
    print("Inserte un valor: ")
    valueInput = input() 
    
    if valueInput.isdigit():
        break  
    else:
        print("La entrada no corresponde a un valor numérico")

print("===================================================================")
print("El valor insertado es: " + valueInput)

digitNum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

isPandigital = True
for digit in digitNum:
    if digit not in valueInput:
       isPandigital = False

if(isPandigital):
    print("Es pandigital")
else:
    print("No es pandigital")

if(len(valueInput) < 3):
    print("Imposible extraer los últimos 3 dígitos")
    sys.exit()

print("===================================================================")
lastThreeValues = valueInput[-3:]
print("Últimos 3 digitos: " + lastThreeValues)

def prime_number(valNum):
    if valNum <= 1:
        return False
    elif valNum <= 3:
        return True
    elif valNum % 2 == 0 or valNum % 3 == 0:
        return False
    i = 5
    while i * i <= valNum:
        if valNum % i == 0 or valNum % (i + 2) == 0:
            return False
        i += 6
    return True

isPrimeNumber = prime_number(int(lastThreeValues))

if (isPrimeNumber):
    print("Es primo")
else:
    print("No es primo")

print("===================================================================")

if (isPandigital and isPrimeNumber):
    print("Resultado: True")
else:
    print("Resultado: False")

print("======================== FIN PROCESO ==============================")







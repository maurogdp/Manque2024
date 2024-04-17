import time

def alcanza(dividendo,divisor):
    alcanza=0
    while True:
        if dividendo<divisor*alcanza:
            break
        alcanza+=1
    return alcanza-1



def dividir(a,b):
    cociente=[]
    resto=[]
    cociente.append(alcanza(a,b))
    #print(cociente)
    resto.append(a%b)
    #print(resto)
    cociente.append(",")
    #print(cociente)
    
    while resto[-1] not in resto[:-1]:
        cociente.append(alcanza(resto[-1]*10,b))
        #print(cociente)
        resto.append(resto[-1]*10%b)
        #print(resto)
        res=resto[-1]

    num=""
    for c in cociente:
        num+=(str(c))
    
    if resto[-1]==0:
        finito = "Finito"
    else:
        finito = "Infinito"
    
    if finito=="Infinito":
        #print(resto)
        comienzo_periodo=resto.index(resto[-1])
        #print(comienzo_periodo)
        largo_periodo=len(resto)-(comienzo_periodo+1)
        #print(cociente)
        parte_entera=cociente[0]
        anteperiodo=""
        for d in cociente[2:comienzo_periodo+2]:
            anteperiodo+=str(d)
        largo_anteperiodo=len(anteperiodo)
        periodo=""
        for d in cociente[comienzo_periodo+2:]:
            periodo+=str(d)
        
        #print("aqui")
        return num,finito,largo_periodo,largo_anteperiodo,parte_entera,anteperiodo,periodo
    cociente=cociente[:-1]
    parte_entera=cociente[0]
    parte_decimal=""
    for d in cociente[2:]:
        parte_decimal+=str(d)
    return num[:-1],finito,str(parte_entera),parte_decimal




# Guarda el tiempo de inicio
inicio = time.time()


maximales=[]
for i in range(2,100):
    datos=dividir(1,i)
    print("================================================================")
    print(f"\nLa división es: 1:{i}\n")
    if datos[1]=="Infinito":
        if datos[3]==0:
            print(f"Tipo: Decimal {datos[1]} periódico")
            print(f"Parte entera: {datos[4]}")
            print(f"Largo de periodo: {datos[2]}")
            if datos[2]==i-1:
                maximales.append(i)
            print(f"Parte periódica: {datos[6]}")
        else:
            print(f"Tipo: Decimal {datos[1]} semiperiódico")
            print(f"Parte entera: {datos[4]}")
            print(f"Largo de anteperido: {datos[3]}")
            print(f"Parte anteperiódica: {datos[5]}")
            print(f"Largo de periodo: {datos[2]}")
            print(f"Parte periódica: {datos[6]}")
        
        print(f"Expansión decimal: {datos[0]}")
    else:
        print(f"Tipo: Decimal {datos[1]}")
        print(f"Parte entera: {datos[2]}")
        print(f"Parte decimal: {datos[3]}")
        print(f"Expansión decimal: {datos[0]}")

    # Guarda el tiempo de finalización
    fin = time.time()

    tiempo_transcurrido = fin - inicio

    print("El programa tardó {:.5f} segundos en ejecutarse.".format(tiempo_transcurrido))

    print(maximales)
import random

def verificar_fila(matriz,numero,posicion):
    fila=matriz[posicion[0]]
    for a in range(0,posicion[1]):
        if fila[a]==numero:
            return False
    return True

def verificar_columna(matriz,numero,posicion):
    columna=[]
    for fila in matriz:
        columna.append(fila[posicion[1]])
    for a in range(0,posicion[0]):
        if columna[a]==numero:
            return False
    return True
    

def determinar_submatriz(matriz,posicion):
    submatriz=[]
    if posicion[0]<3:
        if posicion[1]<3:
            for a in range(0,posicion[0]):
                for b in range(0,posicion[1]):
                    submatriz.append(matriz[a][b])
            return submatriz
        elif posicion[1]<6:
            for a in range(0,posicion[0]):
                for b in range(3,posicion[1]):
                    submatriz.append(matriz[a][b])
            return submatriz
        else:
            for a in range(0,posicion[0]):
                for b in range(6,posicion[1]):
                    submatriz.append(matriz[a][b])
            return submatriz
    elif posicion[0]<6:
        if posicion[1]<3:
            for a in range(3,posicion[0]):
                for b in range(0,posicion[1]):
                    submatriz.append(matriz[a][b])
            return submatriz
        elif posicion[1]<6:
            for a in range(3,posicion[0]):
                for b in range(3,posicion[1]):
                    submatriz.append(matriz[a][b])
            return submatriz
        else:
            for a in range(3,posicion[0]):
                for b in range(6,posicion[1]):
                    submatriz.append(matriz[a][b])
            return submatriz
    else:
        if posicion[1]<3:
            for a in range(6,posicion[0]):
                for b in range(0,posicion[1]):
                    submatriz.append(matriz[a][b])
            return submatriz
        elif posicion[1]<6:
            for a in range(6,posicion[0]):
                for b in range(3,posicion[1]):
                    submatriz.append(matriz[a][b])
            return submatriz
        else:
            for a in range(6,posicion[0]):
                for b in range(6,posicion[1]):
                    submatriz.append(matriz[a][b])
            return submatriz

def verificar_submatriz(matriz,numero,posicion):
    submatriz=determinar_submatriz(matriz,posicion)
    if numero in submatriz:
        return False
    else:
        return True
    

def generar_sudoku_resuelto():
    m1=[0,0,0,0,0,0,0,0,0]
    m2=[0,0,0,0,0,0,0,0,0]
    m3=[0,0,0,0,0,0,0,0,0]
    m4=[0,0,0,0,0,0,0,0,0]
    m5=[0,0,0,0,0,0,0,0,0]
    m6=[0,0,0,0,0,0,0,0,0]
    m7=[0,0,0,0,0,0,0,0,0]
    m8=[0,0,0,0,0,0,0,0,0]
    m9=[0,0,0,0,0,0,0,0,0]
    matriz=[m1,m2,m3,m4,m5,m6,m7,m8,m9]
    
    for i in range(0,9):
        print("fila:",i)
        input()
        conjunto=[1,2,3,4,5,6,7,8,9]
        for j in range(0,9):
            print("columna:",j)
            input()
            
            posicion=[i,j]
            v=0
            while v==0:
                conjunto2=conjunto
                print(conjunto2)
                numero=random.choice(conjunto2)
                print("numero:", numero)
                input()
                #print(i+j)
                if (i+j)!=0:
                    if verificar_columna(matriz,numero,posicion) and verificar_fila(matriz,numero,posicion) and verificar_submatriz(matriz,numero,posicion):
                        matriz[i][j]=numero
                        print(matriz)
                        v=1
                        conjunto.remove(numero)
                else:
                    matriz[i][j]=numero
                    print(matriz)
                    v=1
                    conjunto.remove(numero)
                
                    
            
print(generar_sudoku_resuelto())






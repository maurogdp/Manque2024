user = input("Ingresa tu nombre de usuario -> ")

try:
    with open("users.csv","r") as archivo:
        lineas = archivo.readlines()
        for l in lineas:
            usuario,contraseña=l.split(",")
            if usuario==user:
                print("El usuario existe")
            else:
                print("el usuario no existe")
        
except:
    pass

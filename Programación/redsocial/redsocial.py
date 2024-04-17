
REgi
def registrar_usuario(user):
    registro = True
    print("Para registrar un nuevo usuario entrega la información solicitada a continuación.\nEn caso de querer cancelar el registro, responde a cualquiera de las preguntas con 'cancelar'.")
    print()
    print(f"Usuario: {user}")
    nombre = input("Nombre: ")
    if nombre.lower()=="cancelar":
        print("Registro cancelado.")
        return registro
    apellido = input("Apellido: ")
    if apellido.lower()=="cancelar":
        print("Registro cancelado.")
        return registro
    edad = input("Edad: ")
    if edad.lower()=="cancelar":
        print("Registro cancelado.")
        return registro
    ciudad = input("Ciudad: ")
    if ciudad.lower()=="cancelar":
        print("Registro cancelado.")
        return registro
    password = input("Contraseña: ")
    if password.lower()=="cancelar":
        print("Registro cancelado.")
        return registro
    with open("users.csv","a") as archivo:
        archivo.write(f"{user},{nombre},{apellido},{edad},{ciudad},{password}\n")
    print("\n¡Registro exitoso!")
    return registro
    

user = input("Ingresa tu nombre de usuario -> ")

usuario_existente = False
with open("users.csv", "r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        usuario = linea.split(",")[0]
        if usuario == user:
            usuario_existente = True
            print("El usuario existe")
            break  # Salir del bucle una vez que se encuentra el usuario
    if not usuario_existente:
        print("El usuario no existe")
        new = input("¿Desea registrar un nuevo usuario? (s/n) -> ")
        if new.lower() == "s":
            registrar_usuario(user)
        


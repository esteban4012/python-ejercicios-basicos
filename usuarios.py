usuarios = []

def mostrar_menu():
    print("""
1. Registrar usuario
2. Ver usuarios
3. Eliminar usuario
4. Salir
""")

def registrar_usuario():
    nombre = input("Ingresa nombre: ").strip().lower()

    if len(nombre) == 0:
        print("El nombre no puede estar vacío")
    elif nombre in usuarios:
        print("No se permiten nombres duplicados")
    else:
        usuarios.append(nombre)
        print("Usuario registrado")

def ver_usuarios():
    if not usuarios:
        print("No hay usuarios registrados")
    else:
        print("Usuarios registrados:")
        for i, u in enumerate(usuarios, 1):
            print(f"{i}. {u}")

def eliminar_usuario():
    nombre = input("Nombre a eliminar: ").strip().lower()

    if nombre in usuarios:
        usuarios.remove(nombre)
        print("Usuario eliminado")
    else:
        print("Usuario no encontrado")


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        ver_usuarios()
    elif opcion == "3":
        eliminar_usuario()
    elif opcion == "4":
        print("Saliendo...")
        break
    else:
        print("Opción inválida")
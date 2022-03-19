print ("Ingrese su usuario")
user1 = str(input())
user1 = user1.lower()
print ("Ingrese de nuevo su usuario")
user2 = str(input())
user2 = user2.lower()
while (user1 != user2):
    print ("Su usuario es incorrecto \nVuelva a ingresar su usuario")
    user2 = str(input())
    user2 = user2.lower()
print ("Ingrese su contraseña")
contraseña1 = str(input())
print ("Ingrese de nuevo su contraseña")
contraseña2 = str(input())
contador = 0
while (contraseña1 != contraseña2 and contador <3):
     print (f"Acceso denegado, lleva {contador} intentos \nRecuerde que el máximo de intentos son 3")
     print ("Su contraseña es incorrecta \nVuelva a ingresar su contraseña")
     contraseña2 = str(input())
     contador = contador + 1
if (contador <3):
    print("Acceso permitido")
else:
    print("Ya no tien más intentos \nAcceso bloqueado")
print (f"Bienvenido {user1.capitalize()}")
saldo = 0              
deposito = 0 
comprobador = "si"
while (comprobador == "si"):  
    print ("\tMenu:")
    print ("1. Depositar dinero a la cuenta \n2. Sacar dinero de la cuenta \n3. Ver saldo \n4. Salir")
    opcion = int(input("Digite la opcion de su preferencia \n"))
    while (opcion > 4):
        print ("Error")
        print ("\tMenu:")
        print ("1. Depositar dinero a la cuenta \n2. Sacar dinero de la cuenta \n3. Ver saldo \n4. Salir")
        opcion = int(input("Digite la opcion de su preferencia \n"))
    if (opcion == 1):
        deposito = input("Cuanto dinero desea depositar \n")
        if (deposito.isdigit()):
                deposito = int(deposito)
                if (deposito % 1000 == 0):
                    saldo = saldo + deposito
                    print (f"Usted deposito {deposito}")
                    print (f"Su saldo total es de {saldo}") 
                else:
                    print ("Debe ser un multiplo de 1000")
        else:
            print ("Error \nDebe ingresar numeros \nVuelva a intentar")
    else:
        if (opcion == 2):
            print ("Cuanto dinero desea retirar")
            retiro = int(input())
            if (retiro % 1000 == 0):

                if (saldo >= retiro):
                    saldo = saldo - retiro
                    print (f"Usted retiro {retiro} \nSu saldo actual es de {saldo}")
                else:
                    if (saldo < retiro):
                        print ("El saldo no se puede retirar")
            else:
                print ("Debe ser un multiplo de 1000")
        else:
            if (opcion == 3):
                print ("Usted posee", saldo)
            else:
                if (opcion == 4):
                    print ("Gracias")
    comprobador = str(input("Desea volver a ingresar una de las opciones del menu \nSi \tNo \n"))
    comprobador = comprobador.lower()
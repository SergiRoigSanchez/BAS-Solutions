import tasca1_shodan, tasca2_harvester, tasca3_osint, tasca4_escaneig, tasca5_ssh, tasca6_enumeracio, tasca_telegram

def mostrar_menu():
    print("\nAplicació d'auditoria de BAS Solutions")
    print("1 - Consulta API Shodan")
    print("2 - The Harvester")
    print("3 - OSINT")
    print("4 - Escaneig")
    print("5 - Auditoria SSH")
    print("6 - Ennumeració")

def opcio1():
    print("\nConsulta API Shodan")
    tasca1_shodan.obtenir_informacio_host()
    
def opcio2():
    print("\nThe Harvester")
    tasca2_harvester.recopilar_informacio_domini()

def opcio3():
    print("\nOSINT")
    # tasca3_osint.tasca3_osint.

def opcio4():
    print("\nEscaneig")
    tasca4_escaneig.escaneig_nmap()

def opcio5():
    print("\nAuditoria SSH")
    tasca5_ssh.auditar_ssh()

def opcio6():
    print("\nEnnumeració")
    tasca6_enumeracio.enumerar_host()
    
while True:
    mostrar_menu()
    entrada = input("Elige una opción (1-6) o 'q' para salir: ")
    
    if entrada == 'q':
        break

    try:
        opcion = int(entrada)
        if opcion == 1:
            opcio1()
        elif opcion == 2:
            opcio2()
        elif opcion == 3:
            opcio3()
        elif opcion == 4:
            opcio4()
        elif opcion == 5:
            opcio5()
        elif opcion == 6:
            opcio6()
        else:
            print("Opció invàlida. Per favor, tria un número de l'1 al 6.")

        input("Presiona Enter per tornar al menú principal")

    except ValueError:
        print("Entrada invàlida. Per favor, introdueix un número de l'1 al 6 o 'q' per sortir.")
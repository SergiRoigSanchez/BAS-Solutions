import tasca1_shodan, tasca2_harvester, tasca4_escaneig, tasca5_ssh, tasca6_enumeracio, tasca_telegram

def mostrar_menu():
    print("\nAplicació d'auditoria de BAS Solutions")
    print("1 - Shodan")
    print("2 - The Harvester")
    print("3 - Nmap")
    print("4 - SSH-Audit")
    print("5 - Enum4linux")

def shodan():
    print("\nShodan")
    return tasca1_shodan.demanar_adreca()
    
def harvester():
    print("\nThe Harvester")
    return tasca2_harvester.demanar_dades()

def nmap():
    print("\nNmap")
    return tasca4_escaneig.demanar_opcio()

def ssh_audit():
    print("\nSSH-Audit")
    return tasca5_ssh.demanar_ip()

def enum4linux():
    print("\nEnum4Linux")
    return tasca6_enumeracio.demanar_ip()

# Bucle del menú principal
if __name__ == '__main__':  
    while True:
        # Mostra les opcions del menú
        mostrar_menu()
        print("Tria una opció (1-6) o 'q' per sortir: ")
        entrada = input()
        
        # Sortim si l'usuari introdueix 'q'
        if entrada == 'q':
            break

        try:
            resultat = ""

            # Entrar a una opció depenent de la entrada
            opcio = int(entrada)
            if opcio == 1:
                resultat = shodan()
            elif opcio == 2:
                resultat = harvester()
            elif opcio == 3:
                resultat = nmap()
            elif opcio == 4:
                resultat = ssh_audit()
            elif opcio == 5:
                resultat = enum4linux()
            else:
                print("Opció invàlida. Per favor, tria un número de l'1 al 5.")

            # Imprimir per pantalla el resultat
            print (resultat)

            # Enviar per telegram si l'usuari vol
            print ("Vols enviar el resultat en un missatge al telegram? (s/n): ")
            telegram = input()
            if (telegram == 's'):
                tasca_telegram.enviar_missatge(resultat)
                print ("Missatge enviat correctament.")

            input("Prem Enter per tornar al menú principal")

        except ValueError:
            print("Entrada invàlida. Per favor, introdueix un número de l'1 al 5 o 'q' per sortir.")
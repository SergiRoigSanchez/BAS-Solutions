import subprocess, sys, io

# Demana una IP i utilitza l'eina nmap per descobrir hosts de xarxa, escannejar ports oberts,
# llistar serveis i versions o vulnerabilitats.
def demanar_opcio():
    print("\nTria una de les següents opcions:")
    print("1. Descobrir hosts de xarxa.")
    print("2. Escaneig de ports oberts.")
    print("3. Llistar serveis i versions.")
    print("4. Llistar vulnerabilitats.")

    # Demana una opció.
    opcio = input("\nSelecciona una opció: ")

    resultat = ""

    # Executa l'nmap amb una opció determinada, depen de la opció triada per l'usuari.
    if opcio == "1":
        # Descobriment de hosts.
        target = input("\nIntrodueix la direcció de xarxa a escanejar (Ex: 192.168.1.0/24): ")
        resultat = executar_escaneig("-sn", target)
    elif opcio == "2":
        # Escanneig de ports oberts a un host.
        target = input("\nIntrodueix la IP a escanejar: ")
        resultat = executar_escaneig("-p-", target)
    elif opcio == "3":
        # Escaneig de versions de serveis a cada port obert del host
        target = input("\nIntrodueix la IP a escanejar: ")
        resultat = executar_escaneig("-sV", target)
    elif opcio == "4":
        # Escanneig de vulnerabilitats al sistema del host
        target = input("\nIntrodueix la IP a escanejar: ")
        resultat = executar_escaneig("-sV --script vulners", target)
    else:
        print("\nOpció no vàlida. Selecciona una opció vàlida (1-4).")

    return resultat

def executar_escaneig(params, target, grafic = False):
    try:
        # Crear la lista de comandos
        command = ['nmap'] + params.split() + [target]

        # Executar la comanda i guardar la sortida a result
        result = subprocess.run(command, capture_output=True, text=True)

        if (not grafic):
            print(result.stdout)

        return result

    except Exception as e:
        print(f"Error al executar l'escaneig nmap: {e}")
        return None
    
if __name__ == '__main__':
    demanar_opcio()
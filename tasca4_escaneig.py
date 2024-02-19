import subprocess, sys, io, re

#REGEX per validar IP
def validar_direccion_ip(ip):
    regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return re.match(regex, ip) is not None


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
        ip_address = input("\nIntrodueix la direcció de xarxa a escanejar (Ex: 192.168.1.0/24): ")
        resultat = executar_escaneig("-sn", ip_address)
    elif opcio == "2":
        # Escanneig de ports oberts a un host.
        ip_address = input("\nIntrodueix la IP a escanejar: ")
        resultat = executar_escaneig("-p-", ip_address)
    elif opcio == "3":
        # Escaneig de versions de serveis a cada port obert del host
        ip_address = input("\nIntrodueix la IP a escanejar: ")
        resultat = executar_escaneig("-sV", ip_address)
    elif opcio == "4":
        # Escanneig de vulnerabilitats al sistema del host
        ip_address = input("\nIntrodueix la IP a escanejar: ")
        resultat = executar_escaneig("-sV --script vulners", ip_address)
    else:
        print("\nOpció no vàlida. Selecciona una opció vàlida (1-4).")

    return resultat

def executar_escaneig(params, ip_address, grafic = False):
    try:
        while True:
            ip_address = input("Introdueix una adreça IP: ")

            # Es una adreça ip realment? REGEX
            resultat = validar_direccion_ip(ip_address)
            if resultat == False: 
                print("ERROR. ETS TONTO")
            else:
                break

        # Crear la lista de comandos
        command = ['nmap'] + params.split() + [ip_address]

        # Executar la comanda i guardar la sortida a result
        result = subprocess.run(command, capture_output=True, text=True)

        if (not grafic):
            return result.stdout

        return result

    except Exception as e:
        print(f"Error al executar l'escaneig nmap: {e}")
        return None
    
if __name__ == '__main__':
    demanar_opcio()
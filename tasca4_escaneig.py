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
        resultat = executar_escaneig("-sn", "\nIntrodueix la direcció de xarxa a escanejar (Ex: 192.168.1.0/24): ")
    elif opcio == "2":
        # Escanneig de ports oberts a un host.
        resultat = executar_escaneig("-p-", "\nIntrodueix la IP a escanejar: ")
    elif opcio == "3":
        # Escaneig de versions de serveis a cada port obert del host
        resultat = executar_escaneig("-sV", "\nIntrodueix la IP a escanejar: ")
    elif opcio == "4":
        # Escanneig de vulnerabilitats al sistema del host
        resultat = executar_escaneig("-sV --script vulners", "\nIntrodueix la IP a escanejar: ")
    else:
        print("\nOpció no vàlida. Selecciona una opció vàlida (1-4).")

    return resultat

def executar_escaneig(params, missatge):
    try:
        while True:
            ip_address = input(missatge)

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

        return result.stdout
    except Exception as e:
        print(f"Error al executar l'escaneig nmap: {e}")
        return None
    

def executar_escaneig_grafic(ip_address, params):
    try:        
        # Crear la lista de comandos
        command = ['nmap'] + params.split() + [ip_address]

        # Executar la comanda i guardar la sortida a result
        result = subprocess.run(command, capture_output=True, text=True)

        formatat = formatar_resultat(str(result.stdout))

        return formatar_resultat(formatat)

    except Exception as e:
        print(f"Error al executar l'escaneig nmap: {e}")
        return None
    
def formatar_resultat(result):
    formatat = ""
    if (len(result) > 0):
        for linea in result.split('\n'):
            if "*EXPLOIT*" in linea:
                linea = linea.replace("|     	", "").replace("|_    	", "")
                formatat += linea + '\n'
    
    if (len(formatat) == 0):
        formatat = "No s'ha trobat cap vulnerabilitat al teu servidor."

    return formatat
    
if __name__ == '__main__':
    print(demanar_opcio())
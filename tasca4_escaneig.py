import subprocess, sys, io

# Demana una IP i utilitza l'eina nmap per descobrir hosts de xarxa, escannejar ports oberts,
# llistar serveis i versions o vulnerabilitats.
def escaneig_nmap():
    print("\nOpcions disponibles:")
    print("1. Descobrir hosts de xarxa.")
    print("2. Escaneig de ports oberts.")
    print("3. Llistar de serveis i versions.")
    print("4. Llistar de vulnerabilitats.")

    # Demana una opció.
    opcio = input("\nSelecciona una opció: ")

    resultat = ""

    # Executa l'nmap amb una opció determinada, depen de la opció triada per l'usuari.
    if opcio == "1":
        target = input("\nIntrodueix la direcció de xarxa a escanejar (Ex: 192.168.1.0/24): ")
        resultat = execute_nmap_params("-sn", target)
    elif opcio == "2":
        target = input("\nIntrodueix la IP a escanejar: ")
        resultat = execute_nmap_params("-p-", target)
    elif opcio == "3":
        target = input("\nIntrodueix la IP a escanejar: ")
        resultat = execute_nmap_params("-sV", target)
    elif opcio == "4":
        target = input("\nIntrodueix la IP a escanejar: ")
        resultat = execute_nmap_params("--script vulners", target)
    else:
        print("\nOpció no vàlida. Selecciona una opció vàlida (1-4).")

    return resultat

def execute_nmap_params(params, target):
    try:
        # Crear la lista de comandos
        command = ['nmap', target] + params.split()

        # Ejecutar el comando y obtener el objeto CompletedProcess
        result = subprocess.run(command, capture_output=True, text=True)
        print("Salida estándar:", result.stdout)
        print("Salida de error:", result.stderr)
        print("Código de retorno:", result.returncode)

        return result
    except Exception as e:
        print(f"Error al ejecutar el escaneo Nmap: {e}")
        return None
    
if __name__ == '__main__':
    escaneig_nmap()
import subprocess, re

# Demana una direcció IP per enumerar i recopilar informació sobre aquesta.
def enumerar_host():

    # Solicita a l'usuari la direcció IP o el nom de host
    target = input("Introdueix la direcció IP o el nom de host del sistema: ")

    try:
        output = enumerar_host_parametre(target)
        
        # Imprimeix la sortida a la consola
        print(output)
        
    except subprocess.CalledProcessError as e:
        # En cas d'error, mostra un missatge d'error
        print("Error al ejecutar Enum4linux:", e)

def enumerar_host_parametre(target, color = True):
    # Executa la comanda y captura la sortida a la variable output
    command = f"enum4linux -a {target}"

    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True, text=True)

    if (not color):
        # Treiem el color
        output = re.sub(r'\x1b\[[0-9;]*[mGK]', '', output)

    return output


if __name__ == '__main__':
    enumerar_host()

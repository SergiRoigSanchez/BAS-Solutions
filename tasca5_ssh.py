import subprocess, re

# Audita la configuració del servidor SSH que es troba a la IP proporcionada per l'usuari.
def demanar_ip():
    try:
        # Demanar a l'usuari l'adreça IP o el nom del domini
        host = input("Introdueix l'adreça IP a auditar: ")

        result = auditar_ssh(host, False)

        print (result)
        
    # Gestió d'errors
    except subprocess.CalledProcessError as e:
        print(f"Error en l'execució de ssh-audit: {e}")
    except Exception as e:
        print(f"S'ha produït un error: {e}")

def auditar_ssh(host, grafic = False):
    if (not grafic):
        result = subprocess.run(["ssh-audit", host], capture_output=True, text=True)
        print("color")
        print("Resultat de l'auditoria SSH:")
    else:
        print("nocolor")
        result = subprocess.run(["ssh-audit", "--no-color", host], capture_output=True, text=True)

    formatat = formatar_resultat(str(result.stdout))

    return formatat

def formatar_resultat(result):
    formatat = ""
    if (len(result) > 0):
        for linea in result.split('\n'):
            if "#" in linea or "[warn]" in linea or "[fail]" in linea or "to remove" in linea or len(linea) == 0:
                formatat += linea + '\n'
    
    if (len(formatat) == 0):
        formatat = "El teu ssh està en perfectes condicions."

    return formatat

if __name__ == '__main__':
    demanar_ip()
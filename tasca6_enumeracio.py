import subprocess, re

# Demana una direcció IP per enumerar i recopilar informació sobre aquesta.
def demanar_ip():
    try:
        host = input("Introdueix la direcció IP o el nom de host del sistema: ")
        output = enumerar_host(host)
        
        # Imprimeix la sortida a la consola
        print(output)
        
    except subprocess.CalledProcessError as e:
        # En cas d'error, mostra un missatge d'error
        print("Error al ejecutar Enum4linux:", e)

def enumerar_host(host, grafic = False):
    # Executa la comanda y captura la sortida a la variable output
    command = f"enum4linux -a {host}"

    output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True, text=True)

    # Treiem el color en cas d'estar a la interfície gràfica
    if (grafic):
        output = re.sub(r'\x1b\[[0-9;]*[mGK]', '', output)

    formatat = formatar_resultat(output)

    return formatat

def formatar_resultat(result):
    formatat = ""
    if (len(result) > 0):
        for linea in result.split('\n'):
            if "OS information" in linea:
                break
            if "Starting" not in linea:
                linea = linea.replace("=", "").replace(" ( ", "- ").replace(" )", "").replace("[+] ", "")
                formatat += linea + '\n'
    
    return formatat

if __name__ == '__main__':
    demanar_ip()

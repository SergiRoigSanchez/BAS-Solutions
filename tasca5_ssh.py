import subprocess, re

#REGEX per a saber si es una IP
def validar_direccio_ip(ip):
    regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    return re.match(regex, ip) is not None

# Audita la configuració del servidor SSH que es troba a la IP proporcionada per l'usuari.
def demanar_ip():
    try:
        # Demanar a l'usuari l'adreça IP o el nom del domini
        host = input("Introdueix l'adreça IP a auditar: ")
        while True:
            host = input("Introdueix l'adreça IP a auditar: ")
            # Es una adreça ip realment? REGEX
            resultat = validar_direccio_ip(host)
            if resultat == False: 
                print("ERROR. ETS TONTO")
            else:
                break

        result = auditar_ssh(host, False)

        print (result.stdout)
        
    # Gestió d'errors
    except subprocess.CalledProcessError as e:
        print(f"Error en l'execució de ssh-audit: {e}")
    except Exception as e:
        print(f"S'ha produït un error: {e}")

def auditar_ssh(host, grafic = False):
    if (not grafic):
        result = subprocess.run(["ssh-audit", host], capture_output=True, text=True)
        print("Resultat de l'auditoria SSH:")
    else:
        result = subprocess.run(["ssh-audit", "--no-color", host], capture_output=True, text=True)
        
    return result

if __name__ == '__main__':
    demanar_ip()

import subprocess

# Audita la configuració del servidor SSH que es troba a la IP proporcionada per l'usuari.
def demanar_ip():
    try:
        # Demanar a l'usuari l'adreça IP o el nom del domini
        host = input("Introdueix l'adreça IP a auditar: ")

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
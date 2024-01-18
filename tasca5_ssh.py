import subprocess

# Audita la configuració del servidor SSH que es troba a la IP proporcionada per l'usuari.
def auditar_ssh():
    try:
        # Demanar a l'usuari l'adreça IP o el nom del domini
        host = input("Introdueix l'adreça IP a auditar: ")

        result = auditar_ssh_parametre(host, True)

        print (result.stdout)
        
    # Gestió d'errors
    except subprocess.CalledProcessError as e:
        print(f"Error en l'execució de ssh-audit: {e}")
        print("Sortida d'error:")
        print(e.stderr)
    except FileNotFoundError:
        print("L'eina ssh-audit no està instal·lada o no es pot trobar.")
    except Exception as e:
        print(f"S'ha produït un error: {e}")

def auditar_ssh_parametre(host, colors):
    if (colors):
        result = subprocess.run(["ssh-audit", host], capture_output=True, text=True)
    else:
        result = subprocess.run(["ssh-audit", "--no-color", host], capture_output=True, text=True)

    print("Resultat de l'auditoria SSH:")
        
    return result

if __name__ == '__main__':
    auditar_ssh()
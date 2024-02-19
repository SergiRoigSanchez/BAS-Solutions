import subprocess, re

#REGEX per a verificar el domini
def validar_domini(domini):
    regex = r"^(?!:\/\/)(?:[-A-Za-z0-9]+\.)+[A-Za-z]{2,6}$"
    return re.match(regex, domini) is not None

#REGEX per a verificar que només són números i tres xifres
def validar_max_resultats(max_resultats):
    regex = r"^\d{1,3}$"
    return re.match(regex, max_resultats) is not None

#REGEX per a verificar només són lletres
def validar_fonts(fonts):
    regex = r"^[A-Za-z]+$"
    return re.match(regex, fonts) is not None

# Funció que utilitza TheHarvester per obtenir informació pública relacionada amb un domini, 
# com adreçes de correu electrònic, subdominis, noms de hosts, noms d'usuaris i altres dades
def demanar_dades():
    # Demanar informació a l'usuari
    print("Introdueix les seguents dades: ")

    while True:
        domini = input("Domini de destí (p.ex. bing.com): ")

        # Es un domini realment?
        resultat = validar_domini(domini)
        if resultat == False: 
            print("ERROR. ETS TONTO")
        else:
            break

    while True:
        max_resultats = input("Número máxim de resultats (p.ex. 20): ")
        # Es realment un número?
        resultat_num = validar_max_resultats(max_resultats)
        if resultat_num == False:
            print("ERROR. ETS TONTO")
        else:
            break

    while True:
        fonts = input("Fonts de dades (p.ex. bing): ")
        # Són realment lletres?
        resultat_fonts = validar_fonts(fonts)
        if resultat_fonts == False:
            print("ERROR. ETS TONTO")
        else:
            break


    resultat = recopilar_informacio_domini(domini, max_resultats, fonts)

    # Imprimir la sortida
    print(resultat)

    # Pintar la lletra del terminal de color blanc
    print("\033[0m")

def recopilar_informacio_domini(domini, max_resultats, fonts):
    # Construir la comanda TheHarvester amb les opcions introduides per l'usuari
    comanda = f"python3 /home/alumne/Documents/py/BAS-Solutions/theHarvester/theHarvester.py -d {domini} -l {max_resultats} -b {fonts}"

    try:
        # Executar la comanda construida anteriorment
        resultat = subprocess.check_output(comanda, shell=True, stderr=subprocess.STDOUT, text=True)
        return resultat
    except Exception as e:
        print("Error al executar la comanda:", comanda + "\n" + e.output)

if __name__ == '__main__':
    demanar_dades()
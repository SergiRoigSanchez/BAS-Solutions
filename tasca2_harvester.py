import subprocess

# Funció que utilitza TheHarvester per obtenir informació pública relacionada amb un domini, 
# com adreçes de correu electrònic, subdominis, noms de hosts, noms d'usuaris i altres dades
def demanar_dades():
    # Demanar informació a l'usuari
    print("Introdueix les seguents dades: ")
    domini = input("Domini de destí (p.ex. bing.com): ")
    max_resultats = input("Número máxim de resultats (p.ex. 20): ")
    fonts = input("Fonts de dades (p.ex. bing): ")

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
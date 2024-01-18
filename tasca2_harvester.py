import subprocess

# Funció que utilitza TheHarvester per obtenir informació pública relacionada amb un domini, 
# com adreces de correu electrònic, subdominis, noms de hosts, noms d'usuaris i altres dades
def recopilar_informacio_domini():
    # Demanar informació a l'usuari
    domini = input("Introdueix el domini de destí (per exemple, bing.com): ")
    max_resultats = input("Introdueix el número máxim de resultats (per exemple, 100): ")
    fonts = input("Introdueix les donts de dades (per exemple exemple, bing): ")

    resultat = recopilar_informacio_domini_params(domini, max_resultats, fonts)

    # Imprimir la sortida
    print(resultat)

def recopilar_informacio_domini_params(domini, max_resultats, fonts):
    # Construir la comanda TheHarvester amb les opcions introduides per l'usuari
    comanda = f"python3 /home/alumne/Documents/py/BAS-Solutions/theHarvester/theHarvester.py -d {domini} -l {max_resultats} -b {fonts}"

    try:
        # Executar la comanda construida anteriorment
        resultat = subprocess.check_output(comanda, shell=True, stderr=subprocess.STDOUT, text=True)

        return resultat
    except Exception as e:
        print("Error al executar la comanda:", comanda + "\n" + e.output)

if __name__ == '__main__':
    domini = input("Introdueix el domini de destí (per exemple, bing.com): ")
    max_resultats = input("Introdueix el número máxim de resultats (per exemple, 100): ")
    fonts = input("Introdueix les donts de dades (per exemple exemple, bing): ")
    recopilar_informacio_domini_params(domini, max_resultats, fonts)
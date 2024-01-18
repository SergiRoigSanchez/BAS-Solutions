import subprocess

def ejecutar_osmedeus(target):
    try:
        # Comando para ejecutar Osmedeus
        command = f"osmedeus.py -t {target}"

        # Ejecutar el comando y capturar la salida
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

        # Imprimir la salida en la consola
        print(output)

    except subprocess.CalledProcessError as e:
        # En caso de error, mostrar un mensaje de error
        print(f"Error al ejecutar Osmedeus: {e}")
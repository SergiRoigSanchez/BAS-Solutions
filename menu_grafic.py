import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tasca1_shodan, tasca2_harvester, tasca3_osint, tasca4_escaneig, tasca5_ssh, tasca6_enumeracio

# def funcio_unificada(eina, params="none"):
#     # Limpiar la ventana antes de mostrar la nueva interfaz
#     limpiar_ventana()

#     def mostrar_informacion_host():
#         try:
#             ip_address = entrada_ip.get()

#             resultado = "Resultat buit"
#             if (eina == "shodan"):
#                 resultado = tasca1_shodan.obtenir_informacio_params(ip_address)
#             elif (eina == "osint"):
#                 print("")
#             elif (eina == "harvester"):
#                 domain = entrada_domini.get()
#                 max_results = entrada_max_resultats.get()
#                 sources = entrada_fonts.get()
#                 resultado = tasca2_harvester.recopilar_informacio_domini_params(domain, max_results, sources)
#             elif (eina == "nmap"):
#                 resultado = tasca4_escaneig.execute_nmap_params(ip_address, params)
#             elif (eina == "ssh"):
#                 resultado = tasca5_ssh.auditar_ssh_parametre(ip_address, False)
#             elif (eina == "enum4linux"):
#                 resultado = tasca6_enumeracio.enumerar_host_parametre(ip_address)

#             # Convertir resultado a cadena antes de insertarlo en el widget de texto
#             resultado_str = str(resultado)

#             texto_salida.config(state=tk.NORMAL)
#             texto_salida.delete(1.0, tk.END)
#             texto_salida.insert(tk.END, resultado_str)
#             texto_salida.config(state=tk.DISABLED)
#         except Exception as e:
#             mensaje_error = f"Error al obtenir información del host: {e}"
#             texto_salida.config(state=tk.NORMAL)
#             texto_salida.delete(1.0, tk.END)
#             texto_salida.insert(tk.END, mensaje_error)
#             texto_salida.config(state=tk.DISABLED)

#     titol = "Titol"
#     subtitol = "Subtitol"
#     if (eina == "shodan"):
#         titol = "Shodan"
#     elif (eina == "osint"):
#         titol = "Osint"
#     elif (eina == "harvester"):
#         titol = "Harvester"
#     elif (eina == "nmap"):
#         titol = "Nmap"
#     elif (eina == "ssh"):
#         titol = "Ssh-audit"
#     elif (eina == "enum4linux"):
#         titol = "Enum4linux"

#     # Crear un Frame para agrupar etiqueta_ip, entrada_ip, y boton_confirmar
#     frame_entrada = ttk.Frame(finestra)
#     frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  # Alineado a la izquierda

#     # Título de la sección con formato personalizado
#     estilo_titulo = ttk.Style()
#     estilo_titulo.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  # Fuente más grande, negrita y alineado a la izquierda
#     titulo_seccion = ttk.Label(frame_entrada, text=titol, style="EstiloTitulo.TLabel")
#     titulo_seccion.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  # Sticky "w" para alineación a la izquierda

#     # Subtítulo
#     subtitulo_seccion = ttk.Label(frame_entrada, text="Obtenció d'informació detallada sobre un host específic utilitzant Shodan.")
#     subtitulo_seccion.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  # Sticky "w" para alineación a la izquierda

#     etiqueta_ip = ttk.Label(frame_entrada, text="Introdueix una adreça IP:")
#     etiqueta_ip.grid(row=2, column=0, padx=5)

#     entrada_ip = ttk.Entry(frame_entrada, width=15)
#     entrada_ip.grid(row=2, column=1, padx=5)

#     boton_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=mostrar_informacion_host)
#     boton_confirmar.grid(row=2, column=2, padx=5)

#     boton_telegram = ttk.Button(frame_entrada, text="Telegram")
#     boton_telegram.grid(row=2, column=3, padx=5)

#     # Crear el área de texto para mostrar la salida de la función
#     texto_salida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
#     texto_salida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
#     texto_salida.config(state=tk.DISABLED)

def shodan():
    # Limpiar la ventana antes de mostrar la nueva interfaz
    limpiar_ventana()

    def mostrar_informacion_host():
        try:
            ip_address = entrada_ip.get()
            resultado = tasca1_shodan.obtenir_informacio_params(ip_address)

            # Convertir resultado a cadena antes de insertarlo en el widget de texto
            resultado_str = str(resultado)

            texto_salida.config(state=tk.NORMAL)
            texto_salida.delete(1.0, tk.END)
            texto_salida.insert(tk.END, resultado_str)
            texto_salida.config(state=tk.DISABLED)
        except Exception as e:
            mensaje_error = f"Error al obtenir información del host: {e}"
            texto_salida.config(state=tk.NORMAL)
            texto_salida.delete(1.0, tk.END)
            texto_salida.insert(tk.END, mensaje_error)
            texto_salida.config(state=tk.DISABLED)

    # Crear un Frame para agrupar etiqueta_ip, entrada_ip, y boton_confirmar
    frame_entrada = ttk.Frame(finestra)
    frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  # Alineado a la izquierda

    # Título de la sección con formato personalizado
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  # Fuente más grande, negrita y alineado a la izquierda
    titulo_seccion = ttk.Label(frame_entrada, text="Shodan", style="EstiloTitulo.TLabel")
    titulo_seccion.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  # Sticky "w" para alineación a la izquierda

    # Subtítulo
    subtitulo_seccion = ttk.Label(frame_entrada, text="Obtenció d'informació detallada sobre un host específic utilitzant Shodan.")
    subtitulo_seccion.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  # Sticky "w" para alineación a la izquierda

    etiqueta_ip = ttk.Label(frame_entrada, text="Introdueix una adreça IP:")
    etiqueta_ip.grid(row=2, column=0, padx=5)

    entrada_ip = ttk.Entry(frame_entrada, width=15)
    entrada_ip.grid(row=2, column=1, padx=5)

    boton_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=mostrar_informacion_host)
    boton_confirmar.grid(row=2, column=2, padx=5)

    boton_telegram = ttk.Button(frame_entrada, text="Telegram")
    boton_telegram.grid(row=2, column=3, padx=5)

    # Crear el área de texto para mostrar la salida de la función
    texto_salida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
    texto_salida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
    texto_salida.config(state=tk.DISABLED)

def harvester():
    # Limpiar la ventana antes de mostrar la nueva interfaz
    limpiar_ventana()

    def mostrar_informacion_host():
        try:
            domain = entrada_domini.get()
            max_results = entrada_max_resultats.get()
            sources = entrada_fonts.get()
            resultado = tasca2_harvester.recopilar_informacio_domini_params(domain, max_results, sources)

            # Convertir resultado a cadena antes de insertarlo en el widget de texto
            resultado_str = str(resultado)

            texto_salida.config(state=tk.NORMAL)
            texto_salida.delete(1.0, tk.END)
            texto_salida.insert(tk.END, resultado_str)
            texto_salida.config(state=tk.DISABLED)
        except Exception as e:
            mensaje_error = f"Error al obtener información del host: {e}"
            texto_salida.config(state=tk.NORMAL)
            texto_salida.delete(1.0, tk.END)
            texto_salida.insert(tk.END, mensaje_error)
            texto_salida.config(state=tk.DISABLED)

    # Crear un Frame para agrupar etiqueta_domini, entrada_domini, etiqueta_max_resultats, entrada_max_resultats,
    # etiqueta_fonts, entrada_fonts y boton_confirmar
    frame_entrada = ttk.Frame(finestra)
    frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  # Alineado a la izquierda

    # Título de la sección con formato personalizado
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  # Fuente más grande, negrita y alineado a la izquierda
    titulo_seccion = ttk.Label(frame_entrada, text="The Harvester", style="EstiloTitulo.TLabel")
    titulo_seccion.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  # Sticky "w" para alineación a la izquierda

    # Subtítulo
    subtitulo_seccion = ttk.Label(frame_entrada, text="Obtenció d'informació publica relacionada amb un domini utilitzant Harvester.")
    subtitulo_seccion.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  # Sticky "w" para alineación a la izquierda

    # Etiqueta y entrada para Domini de destí
    etiqueta_domini = ttk.Label(frame_entrada, text="Domini de destí:")
    etiqueta_domini.grid(row=2, column=0, padx=10, pady=10)
    entrada_domini = ttk.Entry(frame_entrada, width=15)
    entrada_domini.grid(row=2, column=1, padx=5)

    # Etiqueta y entrada para Máx. resultats
    etiqueta_max_resultats = ttk.Label(frame_entrada, text="Máx. resultats:")
    etiqueta_max_resultats.grid(row=3, column=0, padx=5)
    entrada_max_resultats = ttk.Entry(frame_entrada, width=15)
    entrada_max_resultats.grid(row=3, column=1, padx=5)

    # Etiqueta y entrada para Fonts de dades
    etiqueta_fonts = ttk.Label(frame_entrada, text="Fonts de dades:")
    etiqueta_fonts.grid(row=4, column=0, padx=10, pady=10)
    entrada_fonts = ttk.Entry(frame_entrada, width=15)
    entrada_fonts.grid(row=4, column=1, padx=5)

    # Botón de Confirmar
    boton_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=mostrar_informacion_host)
    boton_confirmar.grid(row=4, column=2, padx=5)  # Mismo row que la etiqueta y entrada de "Fonts de dades"

    boton_telegram = ttk.Button(frame_entrada, text="Telegram")
    boton_telegram.grid(row=4, column=3, padx=5)

    # Crear el área de texto para mostrar la salida de la función
    texto_salida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
    texto_salida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
    texto_salida.config(state=tk.DISABLED)

def osint():
    # Limpiar la ventana antes de mostrar la nueva interfaz
    limpiar_ventana()

    def mostrar_informacion_host():
        print ("lol")
        # try:
        #     resultado = tasca3_osint.ejecutar_osmedeus()
        #     # Convertir resultado a cadena antes de insertarlo en el widget de texto
            
        #     resultado_str = str(resultado)

        #     texto_salida.config(state=tk.NORMAL)
        #     texto_salida.delete(1.0, tk.END)
        #     texto_salida.insert(tk.END, resultado_str)
        #     texto_salida.config(state=tk.DISABLED)
        # except Exception as e:
        #     mensaje_error = f"Error al obtener información del host: {e}"
        #     texto_salida.config(state=tk.NORMAL)
        #     texto_salida.delete(1.0, tk.END)
        #     texto_salida.insert(tk.END, mensaje_error)
        #     texto_salida.config(state=tk.DISABLED)

    # Crear un Frame para agrupar etiqueta_domini, entrada_domini, etiqueta_max_resultats, entrada_max_resultats,
    # etiqueta_fonts, entrada_fonts y boton_confirmar
    frame_entrada = ttk.Frame(finestra)
    frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  # Alineado a la izquierda

    # Título de la sección con formato personalizado
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  # Fuente más grande, negrita y alineado a la izquierda
    titulo_seccion = ttk.Label(frame_entrada, text="Osint", style="EstiloTitulo.TLabel")
    titulo_seccion.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  # Sticky "w" para alineación a la izquierda

    # Subtítulo
    subtitulo_seccion = ttk.Label(frame_entrada, text="No està fet encara c:")
    subtitulo_seccion.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  # Sticky "w" para alineación a la izquierda

    etiqueta_ip = ttk.Label(frame_entrada, text="Introdueix una adreça IP:")
    etiqueta_ip.grid(row=2, column=0, padx=5)

    entrada_ip = ttk.Entry(frame_entrada, width=15)
    entrada_ip.grid(row=2, column=1, padx=5)

    boton_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=mostrar_informacion_host)
    boton_confirmar.grid(row=2, column=2, padx=5)

    boton_telegram = ttk.Button(frame_entrada, text="Telegram")
    boton_telegram.grid(row=2, column=3, padx=5)

    # Crear el área de texto para mostrar la salida de la función
    texto_salida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
    texto_salida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
    texto_salida.config(state=tk.DISABLED)

def nmap(params, subtitle):
    # Limpiar la ventana antes de mostrar la nueva interfaz
    limpiar_ventana()

    def ejecutar_escaneo_nmap():
        try:
            ip_target = entrada_ip.get()
            resultado = tasca4_escaneig.execute_nmap_params(ip_target, params)

            # Obtener la salida del proceso y el código de retorno
            salida = resultado.stdout
            codigo_retorno = resultado.returncode

            if codigo_retorno == 0:
                # No es necesario decodificar si la salida ya es texto
                resultado_str = str(salida)
                texto_salida.config(state=tk.NORMAL)
                texto_salida.delete(1.0, tk.END)
                texto_salida.insert(tk.END, resultado_str)
                texto_salida.config(state=tk.DISABLED)
            else:
                mensaje_error = f"Error al executar l'escanneig Nmap. Codi de retorn: {codigo_retorno}"
                texto_salida.config(state=tk.NORMAL)
                texto_salida.delete(1.0, tk.END)
                texto_salida.insert(tk.END, mensaje_error)
                texto_salida.config(state=tk.DISABLED)
        except Exception as e:
            mensaje_error = f"Error al executar l'escanneig Nmap: {e}"
            texto_salida.config(state=tk.NORMAL)
            texto_salida.delete(1.0, tk.END)
            texto_salida.insert(tk.END, mensaje_error)
            texto_salida.config(state=tk.DISABLED)

    # Crear un Frame para agrupar etiqueta_ip, entrada_ip y boton_confirmar
    frame_entrada = ttk.Frame(finestra)
    frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  # Alineado a la izquierda

    # Título de la sección con formato personalizado
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  # Fuente más grande, negrita y alineado a la izquierda
    titulo_seccion = ttk.Label(frame_entrada, text="Escaneig", style="EstiloTitulo.TLabel")
    titulo_seccion.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  # Sticky "w" para alineación a la izquierda

    # Subtítulo
    subtitulo_seccion = ttk.Label(frame_entrada, text=subtitle)
    subtitulo_seccion.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  # Sticky "w" para alineación a la izquierda

    # Etiqueta y entrada para IP a escanear
    etiqueta_ip = ttk.Label(frame_entrada, text="IP a escanejar:")
    etiqueta_ip.grid(row=2, column=0, padx=5)
    entrada_ip = ttk.Entry(frame_entrada, width=15)
    entrada_ip.grid(row=2, column=1, padx=5)

    # Botón de Confirmar
    boton_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=ejecutar_escaneo_nmap)
    boton_confirmar.grid(row=2, column=2, padx=5)  # Cambiado de row=1 a row=0

    boton_telegram = ttk.Button(frame_entrada, text="Telegram")
    boton_telegram.grid(row=2, column=3, padx=5)

    # Crear el área de texto para mostrar la salida del escaneo
    texto_salida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
    texto_salida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
    texto_salida.config(state=tk.DISABLED)

def descobrir_hosts():
    nmap("-sn", "Descobriment de hosts d'una xarxa.")

def escaneig_ports():
    nmap("-p-", "Identificació de ports oberts d'un host.")

def llistar_serveis_versions():
    nmap("-sV", "Llistat de serveis i versions de software d'un host.")

def llistar_vulnerabilitats():
    nmap("--script vulners", "Identificació de vulnerabilitats d'un host.")

def ssh_audit():
    # Limpiar la ventana antes de mostrar la nueva interfaz
    limpiar_ventana()

    def ejecutar_ssh_audit():
        try:
            ip_target = entrada_ip.get()
            resultado = tasca5_ssh.auditar_ssh_parametre(ip_target, False)

            # Obtener la salida del proceso y el código de retorno
            salida = resultado.stdout
            codigo_retorno = resultado.returncode

            if salida is not None:
                codigo_retorno = 0

            if codigo_retorno == 0:
                # No es necesario decodificar si la salida ya es texto
                resultado_str = str(salida)
                texto_salida.config(state=tk.NORMAL)
                texto_salida.delete(1.0, tk.END)
                texto_salida.insert(tk.END, resultado_str)
                texto_salida.config(state=tk.DISABLED)
            else:
                mensaje_error = f"Error al executar l'escanneig ssh_audit. Codi de retorn: {codigo_retorno}"
                texto_salida.config(state=tk.NORMAL)
                texto_salida.delete(1.0, tk.END)
                texto_salida.insert(tk.END, mensaje_error)
                texto_salida.config(state=tk.DISABLED)
        except Exception as e:
            mensaje_error = f"Error al executar l'escanneig ssh_audit: {e}"
            texto_salida.config(state=tk.NORMAL)
            texto_salida.delete(1.0, tk.END)
            texto_salida.insert(tk.END, mensaje_error)
            texto_salida.config(state=tk.DISABLED)

    # Crear un Frame para agrupar etiqueta_ip, entrada_ip y boton_confirmar
    frame_entrada = ttk.Frame(finestra)
    frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  # Alineado a la izquierda

    # Título de la sección con formato personalizado
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  # Fuente más grande, negrita y alineado a la izquierda
    titulo_seccion = ttk.Label(frame_entrada, text="Auditoria SSH", style="EstiloTitulo.TLabel")
    titulo_seccion.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  # Sticky "w" para alineación a la izquierda

    # Subtítulo
    subtitulo_seccion = ttk.Label(frame_entrada, text="Auditoria de la configuració del servidor SSH d'un host.")
    subtitulo_seccion.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  # Sticky "w" para alineación a la izquierda

    # Etiqueta y entrada para IP a escanear
    etiqueta_ip = ttk.Label(frame_entrada, text="IP a escanejar:")
    etiqueta_ip.grid(row=2, column=0, padx=5)
    entrada_ip = ttk.Entry(frame_entrada, width=15)
    entrada_ip.grid(row=2, column=1, padx=5)

    # Botón de Confirmar
    boton_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=ejecutar_ssh_audit)
    boton_confirmar.grid(row=2, column=2, padx=5)  # Cambiado de row=1 a row=0

    boton_telegram = ttk.Button(frame_entrada, text="Telegram")
    boton_telegram.grid(row=2, column=3, padx=5)

    # Crear el área de texto para mostrar la salida del escaneo
    texto_salida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
    texto_salida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
    texto_salida.config(state=tk.DISABLED)

def enum4linux():
    # Limpiar la ventana antes de mostrar la nueva interfaz
    limpiar_ventana()

    def ejecutar_enum4linux():
        try:
            ip_target = entrada_ip.get()
            resultado = tasca6_enumeracio.enumerar_host_parametre(ip_target)

            # Obtener la salida del proceso y el código de retorno
            salida = resultado
            codigo_retorno = 0

            if codigo_retorno == 0:
                # No es necesario decodificar si la salida ya es texto
                resultado_str = str(salida)
                texto_salida.config(state=tk.NORMAL)
                texto_salida.delete(1.0, tk.END)
                texto_salida.insert(tk.END, resultado_str)
                texto_salida.config(state=tk.DISABLED)
            else:
                mensaje_error = f"Error al executar l'escanneig ssh_audit. Codi de retorn: {codigo_retorno}"
                texto_salida.config(state=tk.NORMAL)
                texto_salida.delete(1.0, tk.END)
                texto_salida.insert(tk.END, mensaje_error)
                texto_salida.config(state=tk.DISABLED)
        except Exception as e:
            mensaje_error = f"Error al executar l'escanneig ssh_audit: {e}"
            texto_salida.config(state=tk.NORMAL)
            texto_salida.delete(1.0, tk.END)
            texto_salida.insert(tk.END, mensaje_error)
            texto_salida.config(state=tk.DISABLED)

    # Crear un Frame para agrupar etiqueta_ip, entrada_ip y boton_confirmar
    frame_entrada = ttk.Frame(finestra)
    frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  # Alineado a la izquierda

    # Título de la sección con formato personalizado
    estilo_titulo = ttk.Style()
    estilo_titulo.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  # Fuente más grande, negrita y alineado a la izquierda
    titulo_seccion = ttk.Label(frame_entrada, text="Enumeració", style="EstiloTitulo.TLabel")
    titulo_seccion.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  # Sticky "w" para alineación a la izquierda

    # Subtítulo
    subtitulo_seccion = ttk.Label(frame_entrada, text="Enumera i recopila informació d'un host. Pot tardar molt.")
    subtitulo_seccion.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  # Sticky "w" para alineación a la izquierda

    # Etiqueta y entrada para IP a escanear
    etiqueta_ip = ttk.Label(frame_entrada, text="IP a escanejar:")
    etiqueta_ip.grid(row=2, column=0, padx=5)
    entrada_ip = ttk.Entry(frame_entrada, width=15)
    entrada_ip.grid(row=2, column=1, padx=5)

    # Botón de Confirmar
    boton_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=ejecutar_enum4linux)
    boton_confirmar.grid(row=2, column=2, padx=5)  # Cambiado de row=1 a row=0

    boton_telegram = ttk.Button(frame_entrada, text="Telegram")
    boton_telegram.grid(row=2, column=3, padx=5)

    # Crear el área de texto para mostrar la salida del escaneo
    texto_salida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
    texto_salida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
    texto_salida.config(state=tk.DISABLED)

def limpiar_ventana():
    # Obtener todos los widgets dentro de la ventana principal
    widgets = finestra.winfo_children()

    # Eliminar todos los widgets excepto los menús
    for widget in widgets:
        if not isinstance(widget, tk.Menu):
            widget.destroy()

# Crear la ventana principal
finestra = ThemedTk(theme="radiance")
finestra.attributes('-alpha', 0.0)
finestra.title("BAS-Solutions")

# Establecer el tamaño de la ventana
finestra.geometry("800x600")

# Crear el menú
menu_principal = tk.Menu(finestra)
finestra.config(menu=menu_principal)

# Crear el menú "Eines" y sus submenús
menu_eines = tk.Menu(menu_principal)
menu_principal.add_cascade(label="Eines", menu=menu_eines)

menu_eines.add_command(label="Shodan", command=shodan)
menu_eines.add_command(label="Harvester", command=harvester)
menu_eines.add_command(label="Osint", command=osint)

# Submenú "Nmap" con sus opciones
menu_nmap = tk.Menu(menu_eines)
menu_eines.add_cascade(label="Nmap", menu=menu_nmap)

menu_nmap.add_command(label="Descobrir hosts de xarxa", command=descobrir_hosts)
menu_nmap.add_command(label="Escaneig de ports oberts", command=escaneig_ports)
menu_nmap.add_command(label="Llista de serveis i versions", command=llistar_serveis_versions)
menu_nmap.add_command(label="Llista de vulnerabilitats", command=llistar_vulnerabilitats)

menu_eines.add_command(label="SSH Audit", command=ssh_audit)
menu_eines.add_command(label="Enum4Linux", command=enum4linux)

# Iniciar el bucle principal
def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

if __name__ == '__main__':
    center(finestra)
    finestra.attributes('-alpha', 1.0)
    finestra.mainloop()
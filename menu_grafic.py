import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tasca1_shodan, tasca2_harvester, tasca4_escaneig, tasca5_ssh, tasca6_enumeracio, tasca_telegram

def shodan():
    # Netejar la finestra abans de mostrar la nova interficie
    netejar_finestra()

    def mostrar_informacio_host():
        try:
            # Obtenir les dades de la interficie
            ip_address = entrada_ip.get()

            # Passar-les per parametre a la funció que obté la informació
            resultat = tasca1_shodan.obtenir_informacio_host(ip_address)
            resultat_str = str(resultat)

            # Netejar el quadre de text i posar la informació nova
            text_sortida.config(state=tk.NORMAL)
            text_sortida.delete(1.0, tk.END)
            text_sortida.insert(tk.END, resultat_str)
            text_sortida.config(state=tk.DISABLED)

        # Tractament d'excepcions
        except Exception as e:
            mensaje_error = f"Error al obtenir información del host: {e}"
            text_sortida.config(state=tk.NORMAL)
            text_sortida.delete(1.0, tk.END)
            text_sortida.insert(tk.END, mensaje_error)
            text_sortida.config(state=tk.DISABLED)

    def enviar_telegram():
        text = text_sortida.get("1.0", tk.END)
        informacio = ""
        if text and text.strip():
            tasca_telegram.enviar_missatge(text)
            informacio = "Missatge enviat correctament."
        else:
            informacio = "No hi ha res que enviar."
        
        # Netejar el quadre de text i posar la informació nova
        text_sortida.config(state=tk.NORMAL)
        text_sortida.delete(1.0, tk.END)
        text_sortida.insert(tk.END, informacio)
        text_sortida.config(state=tk.DISABLED)

    # Crear un Frame para agrupar etiqueta_ip, entrada_ip, y boto_confirmar
    frame_entrada = ttk.Frame(finestra)
    frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  

    # Títol de la secció
    estil_titol = ttk.Style()
    estil_titol.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  
    titol_seleccio = ttk.Label(frame_entrada, text="Shodan", style="EstiloTitulo.TLabel")
    titol_seleccio.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  

    # Subtítol
    subtitol_seleccio = ttk.Label(frame_entrada, text="Obtenció d'informació detallada sobre un host específic utilitzant Shodan.")
    subtitol_seleccio.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  

    # Etiquetes, inputs i botons
    etiqueta_ip = ttk.Label(frame_entrada, text="Introdueix una adreça IP:")
    etiqueta_ip.grid(row=2, column=0, padx=5)

    entrada_ip = ttk.Entry(frame_entrada, width=15)
    entrada_ip.grid(row=2, column=1, padx=5)

    boto_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=mostrar_informacio_host)
    boto_confirmar.grid(row=2, column=2, padx=5)

    boto_telegram = ttk.Button(frame_entrada, text="Telegram", command=enviar_telegram)
    boto_telegram.grid(row=2, column=3, padx=5)

    # Crear l'àrea de text que mostra la sortida de la funció
    text_sortida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
    text_sortida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
    text_sortida.config(state=tk.DISABLED)

def harvester():
    # Netejar la finestra abans de mostrar la nova interficie
    netejar_finestra()

    def mostrar_informacion_host():
        try:
            domain = entrada_domini.get()
            max_results = entrada_max_resultats.get()
            sources = entrada_fonts.get()
            resultat = tasca2_harvester.recopilar_informacio_domini(domain, max_results, sources)

            # Convertir resultat a cadena antes de insertarlo en el widget de texto
            resultat_str = str(resultat)

            text_sortida.config(state=tk.NORMAL)
            text_sortida.delete(1.0, tk.END)
            text_sortida.insert(tk.END, resultat_str)
            text_sortida.config(state=tk.DISABLED)
        except Exception as e:
            mensaje_error = f"Error al obtener información del host: {e}"
            text_sortida.config(state=tk.NORMAL)
            text_sortida.delete(1.0, tk.END)
            text_sortida.insert(tk.END, mensaje_error)
            text_sortida.config(state=tk.DISABLED)

    def enviar_telegram():
        text = text_sortida.get("1.0", tk.END)
        informacio = ""
        if text and text.strip():
            tasca_telegram.enviar_missatge(text)
            informacio = "Missatge enviat correctament."
        else:
            informacio = "No hi ha res que enviar."
        
        # Netejar el quadre de text i posar la informació nova
        text_sortida.config(state=tk.NORMAL)
        text_sortida.delete(1.0, tk.END)
        text_sortida.insert(tk.END, informacio)
        text_sortida.config(state=tk.DISABLED)

    # Crear un Frame para agrupar etiqueta_domini, entrada_domini, etiqueta_max_resultats, entrada_max_resultats,
    # etiqueta_fonts, entrada_fonts y boto_confirmar
    frame_entrada = ttk.Frame(finestra)
    frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  

    # Títol de la secció
    estil_titol = ttk.Style()
    estil_titol.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  
    titol_seleccio = ttk.Label(frame_entrada, text="The Harvester", style="EstiloTitulo.TLabel")
    titol_seleccio.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  

    # Subtítol
    subtitol_seleccio = ttk.Label(frame_entrada, text="Obtenció d'informació publica relacionada amb un domini utilitzant Harvester.")
    subtitol_seleccio.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  

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

    # Botó de Confirmar
    boto_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=mostrar_informacion_host)
    boto_confirmar.grid(row=4, column=2, padx=5)  # Mismo row que la etiqueta y entrada de "Fonts de dades"

    boto_telegram = ttk.Button(frame_entrada, text="Telegram", command=enviar_telegram)
    boto_telegram.grid(row=4, column=3, padx=5)

    # Crear l'àrea de text que mostra la sortida de la funció
    text_sortida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
    text_sortida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
    text_sortida.config(state=tk.DISABLED)

def nmap(params, subtitle):
    # Netejar la finestra abans de mostrar la nova interficie
    netejar_finestra()

    def ejecutar_escaneo_nmap():
        try:
            ip_target = entrada_ip.get()
            resultat = tasca4_escaneig.executar_escaneig(ip_target, params, True)

            # Obtenir la sortida del proces i el codi de retorn
            sortida = resultat.stdout
            codigo_retorno = resultat.returncode

            if codigo_retorno == 0:
                
                resultat_str = str(sortida)
                text_sortida.config(state=tk.NORMAL)
                text_sortida.delete(1.0, tk.END)
                text_sortida.insert(tk.END, resultat_str)
                text_sortida.config(state=tk.DISABLED)
            else:
                mensaje_error = f"Error al executar l'escanneig Nmap. Codi de retorn: {codigo_retorno}"
                text_sortida.config(state=tk.NORMAL)
                text_sortida.delete(1.0, tk.END)
                text_sortida.insert(tk.END, mensaje_error)
                text_sortida.config(state=tk.DISABLED)
        except Exception as e:
            mensaje_error = f"Error al executar l'escanneig Nmap: {e}"
            text_sortida.config(state=tk.NORMAL)
            text_sortida.delete(1.0, tk.END)
            text_sortida.insert(tk.END, mensaje_error)
            text_sortida.config(state=tk.DISABLED)

    def enviar_telegram():
        text = text_sortida.get("1.0", tk.END)
        informacio = ""
        if text and text.strip():
            tasca_telegram.enviar_missatge(text)
            informacio = "Missatge enviat correctament."
        else:
            informacio = "No hi ha res que enviar."
        
        # Netejar el quadre de text i posar la informació nova
        text_sortida.config(state=tk.NORMAL)
        text_sortida.delete(1.0, tk.END)
        text_sortida.insert(tk.END, informacio)
        text_sortida.config(state=tk.DISABLED)

    # Crear frame per agrupar les etiquetes i el botó
    frame_entrada = ttk.Frame(finestra)
    frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  

    # Títol de la secció
    estil_titol = ttk.Style()
    estil_titol.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  
    titol_seleccio = ttk.Label(frame_entrada, text="Escaneig", style="EstiloTitulo.TLabel")
    titol_seleccio.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  

    # Subtítol
    subtitol_seleccio = ttk.Label(frame_entrada, text=subtitle)
    subtitol_seleccio.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  

    # Etiqueta i entrada per IP a escanejar
    etiqueta_ip = ttk.Label(frame_entrada, text="IP a escanejar:")
    etiqueta_ip.grid(row=2, column=0, padx=5)
    entrada_ip = ttk.Entry(frame_entrada, width=15)
    entrada_ip.grid(row=2, column=1, padx=5)

    # Botó de Confirmar
    boto_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=ejecutar_escaneo_nmap)
    boto_confirmar.grid(row=2, column=2, padx=5)  # Cambiado de row=1 a row=0

    boto_telegram = ttk.Button(frame_entrada, text="Telegram", command=enviar_telegram)
    boto_telegram.grid(row=2, column=3, padx=5)

    # Crear l'àrea de text per mostrar la sortida
    text_sortida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
    text_sortida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
    text_sortida.config(state=tk.DISABLED)

def descobrir_hosts():
    nmap("-sn", "Descobriment de hosts d'una xarxa.")

def escaneig_ports():
    nmap("-p-", "Identificació de ports oberts d'un host.")

def llistar_serveis_versions():
    nmap("-sV", "Llistat de serveis i versions de software d'un host.")

def llistar_vulnerabilitats():
    nmap("--script vulners", "Identificació de vulnerabilitats d'un host.")

def ssh_audit():
    # Netejar la finestra abans de mostrar la nova interficie
    netejar_finestra()

    def ejecutar_ssh_audit():
        try:
            ip_target = entrada_ip.get()
            resultat = tasca5_ssh.auditar_ssh(ip_target, True)

            # Obtenir la sortida del proces i el codi de retorn
            sortida = resultat.stdout
            codigo_retorno = resultat.returncode

            if sortida is not None:
                codigo_retorno = 0

            if codigo_retorno == 0:
                resultat_str = str(sortida)
                text_sortida.config(state=tk.NORMAL)
                text_sortida.delete(1.0, tk.END)
                text_sortida.insert(tk.END, resultat_str)
                text_sortida.config(state=tk.DISABLED)
            else:
                mensaje_error = f"Error al executar l'escanneig ssh_audit. Codi de retorn: {codigo_retorno}"
                text_sortida.config(state=tk.NORMAL)
                text_sortida.delete(1.0, tk.END)
                text_sortida.insert(tk.END, mensaje_error)
                text_sortida.config(state=tk.DISABLED)
        except Exception as e:
            mensaje_error = f"Error al executar l'escanneig ssh_audit: {e}"
            text_sortida.config(state=tk.NORMAL)
            text_sortida.delete(1.0, tk.END)
            text_sortida.insert(tk.END, mensaje_error)
            text_sortida.config(state=tk.DISABLED)

    def enviar_telegram():
        text = text_sortida.get("1.0", tk.END)
        informacio = ""
        if text and text.strip():
            tasca_telegram.enviar_missatge(text)
            informacio = "Missatge enviat correctament."
        else:
            informacio = "No hi ha res que enviar."
        
        # Netejar el quadre de text i posar la informació nova
        text_sortida.config(state=tk.NORMAL)
        text_sortida.delete(1.0, tk.END)
        text_sortida.insert(tk.END, informacio)
        text_sortida.config(state=tk.DISABLED)

    # Crear frame per agrupar les etiquetes i el botó
    frame_entrada = ttk.Frame(finestra)
    frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  

    # Títol de la secció
    estil_titol = ttk.Style()
    estil_titol.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  
    titol_seleccio = ttk.Label(frame_entrada, text="Auditoria SSH", style="EstiloTitulo.TLabel")
    titol_seleccio.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  

    # Subtítol
    subtitol_seleccio = ttk.Label(frame_entrada, text="Auditoria de la configuració del servidor SSH d'un host.")
    subtitol_seleccio.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  

    # Etiqueta i entrada per IP a escanejar
    etiqueta_ip = ttk.Label(frame_entrada, text="IP a escanejar:")
    etiqueta_ip.grid(row=2, column=0, padx=5)
    entrada_ip = ttk.Entry(frame_entrada, width=15)
    entrada_ip.grid(row=2, column=1, padx=5)

    # Botó de Confirmar
    boto_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=ejecutar_ssh_audit)
    boto_confirmar.grid(row=2, column=2, padx=5)  # Cambiado de row=1 a row=0

    boto_telegram = ttk.Button(frame_entrada, text="Telegram", command=enviar_telegram)
    boto_telegram.grid(row=2, column=3, padx=5)

    # Crear l'àrea de text per mostrar la sortida
    text_sortida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
    text_sortida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
    text_sortida.config(state=tk.DISABLED)

def enum4linux():
    # Netejar la finestra abans de mostrar la nova interficie
    netejar_finestra()

    def ejecutar_enum4linux():
        try:
            ip_target = entrada_ip.get()
            resultat = tasca6_enumeracio.enumerar_host(ip_target, True)

            # Obtenir la sortida del proces i el codi de retorn
            sortida = resultat
            codigo_retorno = 0

            if codigo_retorno == 0:
                
                resultat_str = str(sortida)
                text_sortida.config(state=tk.NORMAL)
                text_sortida.delete(1.0, tk.END)
                text_sortida.insert(tk.END, resultat_str)
                text_sortida.config(state=tk.DISABLED)
            else:
                mensaje_error = f"Error al executar l'escanneig ssh_audit. Codi de retorn: {codigo_retorno}"
                text_sortida.config(state=tk.NORMAL)
                text_sortida.delete(1.0, tk.END)
                text_sortida.insert(tk.END, mensaje_error)
                text_sortida.config(state=tk.DISABLED)
        except Exception as e:
            mensaje_error = f"Error al executar l'escanneig ssh_audit: {e}"
            text_sortida.config(state=tk.NORMAL)
            text_sortida.delete(1.0, tk.END)
            text_sortida.insert(tk.END, mensaje_error)
            text_sortida.config(state=tk.DISABLED)

    def enviar_telegram():
        text = text_sortida.get("1.0", tk.END)
        informacio = ""
        if text and text.strip():
            tasca_telegram.enviar_missatge(text)
            informacio = "Missatge enviat correctament."
        else:
            informacio = "No hi ha res que enviar."
        
        # Netejar el quadre de text i posar la informació nova
        text_sortida.config(state=tk.NORMAL)
        text_sortida.delete(1.0, tk.END)
        text_sortida.insert(tk.END, informacio)
        text_sortida.config(state=tk.DISABLED)

    # Crear frame per agrupar les etiquetes i el botó
    frame_entrada = ttk.Frame(finestra)
    frame_entrada.pack(padx=10, pady=10, anchor=tk.W)  

    # Títol de la secció
    estil_titol = ttk.Style()
    estil_titol.configure("EstiloTitulo.TLabel", font=('Arial', 14, 'bold'), anchor='w')  
    titol_seleccio = ttk.Label(frame_entrada, text="Enumeració", style="EstiloTitulo.TLabel")
    titol_seleccio.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="w")  

    # Subtítol
    subtitol_seleccio = ttk.Label(frame_entrada, text="Enumera i recopila informació d'un host. Pot tardar molt.")
    subtitol_seleccio.grid(row=1, column=0, columnspan=10, padx=5, pady=2, sticky="w")  

    # Etiqueta i entrada per IP a escanejar
    etiqueta_ip = ttk.Label(frame_entrada, text="IP a escanejar:")
    etiqueta_ip.grid(row=2, column=0, padx=5)
    entrada_ip = ttk.Entry(frame_entrada, width=15)
    entrada_ip.grid(row=2, column=1, padx=5)

    # Botó de Confirmar
    boto_confirmar = ttk.Button(frame_entrada, text="Confirmar", command=ejecutar_enum4linux)
    boto_confirmar.grid(row=2, column=2, padx=5)  # Cambiado de row=1 a row=0

    boto_telegram = ttk.Button(frame_entrada, text="Telegram", command=enviar_telegram)
    boto_telegram.grid(row=2, column=3, padx=5)

    # Crear l'àrea de text per mostrar la sortida
    text_sortida = tk.Text(finestra, wrap=tk.WORD, height=15, width=50)
    text_sortida.pack(expand=True, padx=10, pady=(0, 10), fill=tk.BOTH)
    text_sortida.config(state=tk.DISABLED)

def netejar_finestra():
    # Obté els widgets de la finestra
    widgets = finestra.winfo_children()

    # Eliminar-los tots menys el menú
    for widget in widgets:
        if not isinstance(widget, tk.Menu):
            widget.destroy()

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

# Crear la finestra principal
finestra = ThemedTk(theme="radiance")
finestra.attributes('-alpha', 0.0)
finestra.title("BAS-Solutions")

# Estableix la mida de la finestra
finestra.geometry("800x600")

# Crear el menú
menu_principal = tk.Menu(finestra)
finestra.config(menu=menu_principal)

# Crear el menú "Eines" i els seus submenús
menu_eines = tk.Menu(menu_principal)
menu_principal.add_cascade(label="Eines", menu=menu_eines)

menu_eines.add_command(label="Shodan", command=shodan)
menu_eines.add_command(label="Harvester", command=harvester)

# Submenú "Nmap" i les seves opciones
menu_nmap = tk.Menu(menu_eines)
menu_eines.add_cascade(label="Nmap", menu=menu_nmap)

menu_nmap.add_command(label="Descobrir hosts de xarxa", command=descobrir_hosts)
menu_nmap.add_command(label="Escaneig de ports oberts", command=escaneig_ports)
menu_nmap.add_command(label="Llista de serveis i versions", command=llistar_serveis_versions)
menu_nmap.add_command(label="Llista de vulnerabilitats", command=llistar_vulnerabilitats)

menu_eines.add_command(label="SSH Audit", command=ssh_audit)
menu_eines.add_command(label="Enum4Linux", command=enum4linux)

if __name__ == '__main__':
    center(finestra)
    finestra.attributes('-alpha', 1.0)
    finestra.mainloop()
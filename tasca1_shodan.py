import shodan, sys, io

# La nostra API key
api_key = 'FfS8VG9tA5GoHBVEUcwc9gJcfGqKAi6W'

# Inicialitzar client de Shodan
api = shodan.Shodan(api_key)

# Funció que utilitza l'API de Shodan per obtenir informació detallada sobre un host específic, incloent la seva adreça IP, organització, 
# sistema operatiu, noms de host i els ports i serveis oberts al host, juntament amb banners i detalls del producte si estan disponibles.
def demanar_adreca():
    # Demanar l'adreça IP
    ip_address = input("Introdueix una adreça IP: ")

    return obtenir_informacio_host(ip_address)

def obtenir_informacio_host(ip_address):
    # Redirigir la sortida estándar a un objecte StringIO
    output_buffer = io.StringIO()
    sys.stdout = output_buffer

    try:
        host = api.host(ip_address)
        print(f"IP: {host['ip_str']}")
        print(f"Organització: {host.get('org', 'N/A')}")
        print(f"Sistema operatiu: {host.get('os', 'N/A')}")
        print(f"Hostnames: {', '.join(host.get('hostnames', []))}")
        
        for item in host['data']:
            print(f"Port: {item['port']}")
            # print(f"Banner: {item.get('banner', 'N/A')}")
            if 'product' in item:
                print(f"Servei: {item['product']}")
            print()

    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {str(e)}"
    
    # Restablir la sortida estándar
    sys.stdout = sys.__stdout__

    # Obtenir el contingut capturat y retornar-lo com a String
    output_text = str(output_buffer.getvalue())
    return output_text
if __name__ == '__main__':
    demanar_adreca()

# Funció que utilitza l'API de Shodan per buscar hosts que estiguin executant un servei específic, 
# recopila informació sobre aquests hosts, com les adreces IP i ports
# def find_ips_with_service(service_name):
#     # Redirigir la sortida estándar a un objecte StringIO
#     output_buffer = io.StringIO()
#     sys.stdout = output_buffer

#     try:
#         # Busca els hosts que tenen executant el servei utilitzat
#         results = api.search(f'service:"{service_name}"')

#         # Imprimeix les adreces IP i els ports dels hosts coincidents
#         for result in results['matches']:
#             ip_address = result['ip_str']
#             port = result['port']
            
#             print(f"IP: {ip_address}, Port: {port}")
#     except Exception as e:
#         print(f"Error: {e}")
    
#     # Restablir la sortida estándar
#     sys.stdout = sys.__stdout__

#     # Obtenir el contingut capturat y retornar-lo com a String
#     output_text = str(output_buffer.getvalue())
#     return output_text
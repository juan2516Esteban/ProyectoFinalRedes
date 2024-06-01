# imporatmos el Modulo Speed Test

import re
import psutil
import socket
import subprocess
import requests
import speedTest


# Obotener Ip Publica de red 

def get_public_ip_address():
    try:
            # Utilizar un servicio externo para obtener la dirección IP pública
        response = requests.get("https://api.ipify.org")
            
            # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
                # Extraer la dirección IP pública del cuerpo de la respuesta
            public_ip_address = response.text
            return public_ip_address
    except requests.RequestException as e:
        print(f"Error al obtener la dirección IP pública: {e}")



    # Sirve para medir los datos de Subida (upload) y de Bajada (download) de la red 

def medir_ancho_de_banda_red_local(unidadDeMedida: str):
        # Obtener estadísticas sobre el uso de la red
    network_stats = psutil.net_io_counters()

    bytes_sent_gb: any
    bytes_recv_gb : any
        
    if unidadDeMedida == 'bytes':
        # Mostrar las estadísticas de subida y bajada de datos en bytes
        print(f"Bytes enviados Subida: {network_stats.bytes_sent} bytes")
        print(f"Bytes recibidos Bajada: {network_stats.bytes_recv} bytes")

        bytes_sent_gb =  network_stats.bytes_sent
        bytes_recv_gb = network_stats.bytes_recv
        
    if unidadDeMedida == 'gigabytes':
        # Convertir los bytes a gigabytes (GB) para una mejor comprensión
        bytes_sent_gb = round(network_stats.bytes_sent / (1024 ** 3) , 2)  # Convertir bytes a gigabytes (GB)
        bytes_recv_gb = round(network_stats.bytes_recv / (1024 ** 3) , 2)  # Convertir bytes a gigabytes (GB)

    return bytes_sent_gb , bytes_recv_gb


    # Obtener Nombre de la Red 

def get_windows_ssid():
    try:
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'interfaces'],
            capture_output=True,
            text=True
        )
        interfaces_info = result.stdout
        # Use regex to find the SSID
        ssid_match = re.search(r"^\s*SSID\s*:\s*(.+)$", interfaces_info, re.MULTILINE)
        if ssid_match:
            return ssid_match.group(1).strip()
    except subprocess.CalledProcessError:
        return None


    # sirve para obtener la ip del computador o dispositivo 

def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


    # Sirve para odtener la dirección privada asignada por el router en el dispositivo en uina red LAN 

def obtener_ip_privada():
    try:
        # Creamos un socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
        # Conectamos el socket a una dirección IP no utilizada
        s.connect(("8.8.8.8", 80))
            
        # Obtenemos la dirección IP del socket conectado, que será la IP privada del dispositivo
        ip_privada = s.getsockname()[0]
            
        # Cerramos el socket
        s.close()
            
        return ip_privada
    except Exception as e:
        print("Error al obtener la dirección IP privada:", e)
        return None
    
def internet_bajada():
    st = speedTest.Speedtest()
    st.get_best_server()
    return st.download() / 1024 / 1024

def internet_subida():
    st = speedTest.Speedtest()
    st.get_best_server()
    return st.upload() / 1024 / 1024



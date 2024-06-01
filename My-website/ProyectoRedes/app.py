from flask import Flask, render_template , request 
from Backend import speedTest


app = Flask(__name__)
functions = speedTest
Json = []
velocidadSubida = functions.internet_subida()
velocidadBajada = functions.internet_bajada()


@app.route("/", methods=['GET', 'POST'])
def speedtest():
    salida = "hola"
    if request.method == 'POST':
        unidades = str(request.form['options'])
        bytes_sent_gb, bytes_recv_gb = functions.medir_ancho_de_banda_red_local(unidades)
        if unidades == 'bytes':
            output = f"Bytes enviados: {bytes_sent_gb} bytes, Bytes recibidos: {bytes_recv_gb} bytes"
        elif unidades == 'gigabytes':
            output = f"Bytes enviados: {bytes_sent_gb} GB, Bytes recibidos: {bytes_recv_gb} GB"
        else:
            output = 'Unidad no válida'
    else:
        output = None

    datos = {
        "ip": functions.get_public_ip_address(),
        "nombre": functions.get_windows_ssid(),
        "IpDevices": functions.get_ip_address(),
        "PrivateIp": functions.obtener_ip_privada(),
    }
    
    v1 = velocidadSubida
    v2 = velocidadBajada
    Json = datos
    salida = output
    return render_template("redes.html", datos=Json, output=salida , v1=v1 , v2=v2)

if __name__ == "__main__":
    app.run(debug=True)
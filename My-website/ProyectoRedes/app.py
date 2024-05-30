from flask import Flask, render_template , request 
from Backend import speedTest


app = Flask(__name__)
functions = speedTest

ip = functions.get_public_ip_address()

@app.route("/" , methods = ['GET'])
def speedtest():
    ip = functions.get_public_ip_address()
    nombre = functions.get_windows_ssid()
    IpDevices = functions.get_ip_address()
    PriavteIp = functions.obtener_ip_privada()
    return render_template("index.html", ip=ip , nombreDeRed = nombre , IpDevices = IpDevices , PriavteIp = PriavteIp) 

@app.route("/" , methods = ['POST'] )
def AnchodeBanda():
    unidades = str(request.form['options'])
    bytes_sent_gb , bytes_recv_gb = functions.medir_ancho_de_banda_red_local(unidades)
    if unidades == 'bytes':
        output = f"Bytes enviados: {bytes_sent_gb} bytes, Bytes recibidos: {bytes_recv_gb} bytes"
    elif unidades == 'gigabytes':
        output = f"Bytes enviados: {bytes_sent_gb} GB, Bytes recibidos: {bytes_recv_gb} GB"
    else:
        output = 'Unidad no valida'

    ip = functions.get_public_ip_address()
    nombre = functions.get_windows_ssid()
    IpDevices = functions.get_ip_address()
    PriavteIp = functions.obtener_ip_privada()
    return render_template("index.html", ip=ip , nombreDeRed = nombre , IpDevices = IpDevices , PriavteIp = PriavteIp, output=output) 


if __name__ == "__main__":
    app.run(debug=True)
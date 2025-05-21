from flask import Flask, render_template, request, redirect, send_from_directory
import psycopg2
import os
from dotenv import load_dotenv

import smtplib
from email.mime.text import MIMEText

# Ruta absoluta al frontend
FRONTEND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'frontend'))

app = Flask(__name__,
            template_folder=FRONTEND_PATH,  
            static_folder=FRONTEND_PATH)    


@app.route('/css/<path:filename>')
def css_static(filename):
    return send_from_directory(os.path.join(FRONTEND_PATH, 'css'), filename)

@app.route('/js/<path:filename>')
def js_static(filename):
    return send_from_directory(os.path.join(FRONTEND_PATH, 'js'), filename)

@app.route('/assets/<path:filename>')
def assets_static(filename):
    return send_from_directory(os.path.join(FRONTEND_PATH, 'assets'), filename)

load_dotenv()

# try:
#     conn = psycopg2.connect(
#         dbname=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASS"),
#         host=os.getenv("DB_HOST"),
#         port='5432'
#     )
#     print("✅ Conectado a PostgreSQL")
# except Exception as e:
#     print("❌ Error al conectar a PostgreSQL:", e)
#     conn = None

def enviar_correo(email, telefono, empresa, plan, personas, mensaje):
    try:
        cuerpo = f"""
        Tienes una nueva solicitud en el espacio de coworking de {email}:  

        Teléfono: {telefono}
        Empresa: {empresa}
        Plan: {plan}
        Personas: {personas}
        
        {mensaje}
        """

        msg = MIMEText(cuerpo)
        msg['Subject'] = 'Nuevo formulario de contacto'
        msg['From'] = os.getenv("EMAIL_USER")
        msg['To'] = os.getenv("EMAIL_TO")

        with smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT"))) as server:
            server.starttls()
            server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            server.send_message(msg)
        print("✅ Correo enviado")
    except Exception as e:
        print("❌ Error al enviar correo:", e)


@app.route('/', methods=['GET'])
def index():
    idioma = request.form.get("idioma", "frontend/index")
    return redirect(f'/{idioma}.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    # if conn is None:
    #     return "Error de conexión a base de datos", 500

    try:
        email = request.form['email']
        telefono = request.form['telefono']
        empresa = request.form['empresa']
        plan = request.form['plan']
        personas = request.form['personas']
        mensaje = request.form.get('mensaje', '')
        privacidad = 'privacidad' in request.form

        print("📨 Datos recibidos:")
        print(email, telefono, empresa, plan, personas, mensaje, privacidad)

        # cur = conn.cursor()
        # cur.execute("""
        #     INSERT INTO formulario_contacto 
        #     (email, telefono, empresa, plan, personas, mensaje, privacidad)
        #     VALUES (%s, %s, %s, %s, %s, %s, %s)
        # """, (email, telefono, empresa, plan, personas, mensaje, privacidad))
        # conn.commit()
        # cur.close()
        enviar_correo(email, telefono, empresa, plan, personas, mensaje) #correo
        idioma = request.form.get("idioma", "frontend/index")
        return redirect(f'/frontend/redirect-{idioma}.html')
        # return redirect('frontend/requested.html')
    except Exception as e:
        print("❌ Error al insertar en la base de datos:", e)
        return "Error al procesar el formulario", 500

if __name__ == '__main__':
    app.run(debug=True) 
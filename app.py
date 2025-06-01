from flask import Flask, render_template, request, redirect, send_from_directory
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

load_dotenv()

app = Flask(__name__)  

@app.route('/robots.txt')
def robots():
    return send_from_directory('.', 'robots.txt', mimetype='text/plain')

@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('.', 'sitemap.xml', mimetype='application/xml')

# --------------------------
# Envío de correo
# --------------------------
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
        destinatarios = [os.getenv("EMAIL_TO_1"), os.getenv("EMAIL_TO_2")]
        msg['To'] = ", ".join(destinatarios)

        with smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT"))) as server:
            server.starttls()
            server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            server.sendmail(msg['From'], destinatarios, msg.as_string())
        print("✅ Correo enviado")

    except Exception as e:
        print("❌ Error al enviar correo:", e)

# --------------------------
# Rutas de páginas
# --------------------------
@app.route('/')
def index():
    return render_template('index.html', lang='')  

@app.route('/<lang>')
def idioma(lang):
    return render_template(f'{lang}/index.html', lang=lang)

@app.route('/redirect')
def redirect_es():
    return render_template('redirect.html')

@app.route('/<lang>/redirect')
def redirect_idioma(lang):
    if lang in ['ca', 'en']:
        return render_template(f'{lang}/redirect.html')
    else:
        return redirect('/')

# --------------------------
# Ruta de formulario
# --------------------------
@app.route('/enviar', methods=['POST'])
def enviar():
    try:
        email = request.form['email']
        telefono = request.form['telefono']
        empresa = request.form['empresa']
        plan = request.form['plan']
        personas = request.form['personas']
        mensaje = request.form.get('mensaje', '')
        privacidad = 'privacidad' in request.form

        print("📨 Datos recibidos:", email, telefono, empresa, plan, personas, mensaje, privacidad)

        enviar_correo(email, telefono, empresa, plan, personas, mensaje)

        idioma = request.form.get("idioma", "")

        if idioma in ["ca", "en"]:
            return redirect(f'/{idioma}/redirect')
        else:
            return redirect('/redirect')

    except Exception as e:
        print("❌ Error al procesar el formulario:", e)
        return "Error al procesar el formulario", 500

# --------------------------
# Iniciar servidor
# --------------------------
if __name__ == '__main__':
    app.run(debug=True)

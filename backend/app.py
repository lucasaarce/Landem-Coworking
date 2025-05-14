from flask import Flask, render_template, request, redirect, send_from_directory
import psycopg2
import os
from dotenv import load_dotenv

# Ruta absoluta al frontend
FRONTEND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

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
# Conexión a PostgreSQL
try:
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port='5432'
    )
    print("✅ Conectado a PostgreSQL")
except Exception as e:
    print("❌ Error al conectar a PostgreSQL:", e)
    conn = None

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    if conn is None:
        return "Error de conexión a base de datos", 500

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

        cur = conn.cursor()
        cur.execute("""
            INSERT INTO formulario_contacto 
            (email, telefono, empresa, plan, personas, mensaje, privacidad)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (email, telefono, empresa, plan, personas, mensaje, privacidad))
        conn.commit()
        cur.close()

        return redirect('/')
    except Exception as e:
        print("❌ Error al insertar en la base de datos:", e)
        return "Error al procesar el formulario", 500

# 🚨 Asegúrate de tener esto al final del archivo
if __name__ == '__main__':
    app.run(debug=True)

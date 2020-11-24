
from flask import Flask, render_template, url_for, redirect
from pruebaturnos import procesar_archivo

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
	return render_template('principal.html')

resultado = {}

@app.route('/', methods=["POST"])
def submit():
	archivo = 'turnos.json'
	global resultado
	resultado = procesar_archivo(archivo)
	return redirect(url_for('resultados'))

@app.route('/resultados')
def resultados():
	return render_template('resultados.html', resultado = resultado)

@app.route('/detalle/<status>')
def detalle(status):	
	return render_template('detalle.html', resultado = resultado[status])
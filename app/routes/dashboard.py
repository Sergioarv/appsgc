from app import app, db
from flask import render_template
from app.schemas.models import Request

# Dashboard y otros graficos
@app.route('/dashboard')
def dashboard_index():
    return render_template('/dashboard/dashboard.html')

@app.route('/solicitudes/<string:d>')
def prueba(d):
    tittle ='Cantidad de Solicitudes por Tipo'
    data = []
    valor = ['Solicitado','Rechazado','Procesado','Aceptado']
    data.append(Request.query.filter_by(state = 'Solicitado').count())
    data.append(Request.query.filter_by(state = 'Rechazado').count())
    data.append(Request.query.filter_by(state = 'Procesado').count())
    data.append(Request.query.filter_by(state = 'Aceptado').count())
    return render_template('/dashboard/piechart.html', mydata = data, valor = valor, tittle = tittle, dashboard = d)

@app.route('/solicitudesBar/<string:d>')
def prueba2(d):
    tittle ='Cantidad de Solicitudes por Tipo'
    data = []
    c = ['#0040FF','#088A4B','#FF0000','#FF8000']
    valor = ['Solicitado','Aceptado','Rechazado','Procesado']
    data.append(Request.query.filter_by(state = 'Solicitado').count())
    data.append(Request.query.filter_by(state = 'Aceptado').count())
    data.append(Request.query.filter_by(state = 'Rechazado').count())
    data.append(Request.query.filter_by(state = 'Procesado').count())
    return render_template('/dashboard/barchart.html', mydata = data, valor = valor, tittle = tittle, c = c, dashboard = d)

@app.route('/Tiempo/<string:d>')
def prueba2(d):
    tittle ='Tiempo en Responder Solicitudes'
    data = []
    valor = ['Solicitado','Rechazado','Procesado','Aceptado']
    data.append(Request.query.filter_by(state = 'Solicitado').count())
    data.append(Request.query.filter_by(state = 'Rechazado').count())
    data.append(Request.query.filter_by(state = 'Procesado').count())
    data.append(Request.query.filter_by(state = 'Aceptado').count())
    return render_template('/dashboard/piechart.html', mydata = data, valor = valor, tittle = tittle, dashboard = d)
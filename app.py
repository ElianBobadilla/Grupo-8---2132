from datetime import date, datetime
from flask import Flask, render_template, url_for, request, redirect,flash
import controlador

app=Flask(__name__)

app.secret_key='Mi clave Secreta'+str(datetime.now)

@app.route('/prueba')
def prueba():
    return True

@app.route('/addregistro', methods=['POST'])
def add_registro():
    datos=request.form
    nom=datos['nombre']
    ape=datos['apellido']
    usu=datos['email']
    p1=datos['pass1']
    p2=datos['pass2']
     
  

    if nom==''and ape=='' and usu=='' and p1=='' and p2=='':
        #return '<h2>Datos Incompletos</h2>'
       flash('Datos Incompletos')
    elif p1!=p2:
        #return '<h2>Las Contraseñas no coinciden</h2>'
       flash('Las Constraseñas no Coinciden')
    elif len(p1)<8:
       #return '<h2>Verificar las constraseñas</h2>'     
       flash('Verificar Tamaño de la Contaseña')
    else:
       resultado=controlador.adicionar_registros(nom,ape,usu,p1)
       if resultado:
        flash('Registro Almacenado Correctamente')
       else:
        flash('Error en Base de Datos')

    return redirect(url_for('registro'))





@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/contra')
def contra():
    return render_template('contra.html')

@app.route('/recuperar')
def recuperar():
    return render_template('recuperar.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')


if  __name__=='__main__':
     app.run(debug=True) 
from datetime import date, datetime
from flask import Flask, render_template, url_for, request, redirect, flash
import controlador
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)

app.secret_key='Mi clave Secreta'+str(datetime.now)

@app.route('/prueba')
def prueba():
    return True


@app.route('/activarCuenta', methods=['POST'])
def activarCuenta():
    datos=request.form
    Usuario=datos['Usuario']
    Cod_Verificacion=datos['Codigo']
    if Usuario=='' and Cod_Verificacion=='':
        flash('Datos Incompletos')
        return redirect('/validar')
    else:
        resultado=controlador.activar_cuenta(Usuario, Cod_Verificacion)
        if resultado==True:
            flash('Cuenta Activada Safisfactoriamente')
            return redirect('/login')   
        else:
            flash('Error en la activación de la activación')
            return redirect('/validar')
              
                       
@app.route('/verificar', methods=['POST'])
def validarlogin():
    datos=request.form
    Usu=datos['Usuario']
    Contraseña=datos['Contraseña']
    if Usu==''and Contraseña=='':
       flash('Datos Incompletos')
       print('Datos Incompletos')
       return redirect(url_for('login'))
    elif len(Contraseña)<=6:    
       flash('La contraseña debe tener minimo 6 caracteres')
       return redirect(url_for('login'))
    else:
        resultado=controlador.validacion_login(Usu)
        if resultado==False:
            flash('Usuario/Contraseña Incorrectos')
            return redirect(url_for('login'))
        else:
            if check_password_hash(resultado[0]['Contraseña'],Contraseña):
                if resultado[0]['Verificado']==1:
                    return render_template('bandeja.html')
                else:
                    return redirect(url_for('validar'))
            else:
                flash('Contraseña Incorrecta')
                return redirect(url_for('login'))
            

@app.route('/addregistro', methods=['POST'])
def add_registro():
    datos=request.form
    Usuario=datos['Usuario']
    Contraseña=datos['Contraseña']
    Email=datos['Email']
    ContraseñaEnc=generate_password_hash(Contraseña)
    if Usuario==''and Contraseña=='' and Email=='':
       flash('Datos Incompletos')
       print('Datos Incompletos')
       return redirect(url_for('registro'))
    elif len(Contraseña)<=6:    
       flash('La contraseña debe tener minimo 6 caracteres')
       return redirect(url_for('registro'))
    else:
       resultado=controlador.adicionar_registros(Usuario,ContraseñaEnc,Email)
       if resultado:
        flash('Registro Almacenado Correctamente')
        return redirect(url_for('login'))
       else:
        flash('Ha oc')
        return redirect(url_for('registro'))
    
    
@app.route('/recuperarcontra', methods=['POST'])
def recuperarcontra():
    datos=request.form
    Email=datos['Email']
    if  Email=='':
        flash('Ingrese un correo') 
        return redirect(url_for('recuperar'))    
    else:
        resultado = controlador.validarcorreo(Email)
        if resultado == 'NO':
            flash('No hay una cuenta asociada a este correo')
            return redirect(url_for('recuperar')) 
        elif resultado == 'SI':
            flash('Revise la bandeja de entrada de su correo')
            return redirect(url_for('login')) 
        else:
            flash('Invalid')
            return redirect(url_for('recuperar'))

    
@app.route('/bandeja')
def bandeja():
    return render_template('bandeja.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/nueva-contra')
def nueva_contra():
    return render_template('nueva-contra.html')

@app.route('/recuperar')
def recuperar():
    return render_template('recuperar.html')

@app.route('/validar')
def validar():
    return render_template('validar.html')

@app.route('/politicas')
def politicas():
    return render_template('politicas.html')


if  __name__=='__main__':
     app.run(debug=True) 
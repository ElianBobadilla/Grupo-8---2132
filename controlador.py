from ctypes import resize
from dataclasses import replace
from datetime import datetime
import email
import sqlite3
import EnviarCorreo
from flask import flash
import random


DB_NAME='Ejemplo_DB.db'

def conexion():
    conn=sqlite3.connect(DB_NAME)
    return conn

def adicionar_registros(Usuario, Contraseña, Email):
    may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    general = may + num 
    longitud = 6
    codigo = random.sample(general, longitud)
    Cod_verificacion = "".join(codigo)
    try:
        db=conexion()
        cursor=db.cursor()
        sql = 'INSERT INTO Usuario (Usuario, Contraseña, Email, Verificado, Cod_Verificacion) VALUES (?,?,?,?,?)'
        cursor.execute(sql,[Usuario, Contraseña, Email, 0, Cod_verificacion])
        db.commit()
        EnviarCorreo.Correo(Email, Cod_verificacion)
        return True
    except:
        return False
    
def validacion_login(Usuario):
    try:   
        db=conexion()
        cursor=db.cursor()
        sql = 'SELECT * FROM Usuario WHERE Usuario=?'
        cursor.execute(sql,[Usuario])
        resultado = cursor.fetchone()
        print(resultado)
        datos=[
            {
                'ID':resultado[0],
                'Usuario':resultado[1],
                'Contraseña':resultado[2],
                'Email':resultado[3],
                'Verificado':resultado[4],
                'Cod_Verificacion':resultado[5]       
            }       
        ]
        return datos
    except:
        return False
    
def activar_cuenta(Usuario, Cod_Verificacion):
    try:   
        db=conexion()
        cursor=db.cursor()
        #sql='UPDATE Usuario SET Verificado=1 WHERE Usuario=? AND Cod_Verificacion=?'
        #
        Sql = "UPDATE Usuario SET Verificado=1 WHERE Usuario=? AND Cod_Verificacion=?"
        cursor.execute(Sql,[Usuario, Cod_Verificacion])
        db.commit()

        print(Usuario, Cod_Verificacion)
        return True
    except:
        return False
    
    
def validarcorreo(Email):
    print(Email)
    try:   
        db=conexion()
        cursor=db.cursor()
        Sql = 'SELECT * FROM Usuario WHERE Email=?'
        cursor.execute(Sql,[Email])
        resultado = cursor.fetchone()
        EnviarCorreo.RecuperarContraseña()
        print(resultado)
        if resultado != None:
            return 'SI'
        else: 
            return 'NO'
    except:
        return False

def listar_usuario(Usuario):
    try:
        db=conexion()
        cursor=db.cursor()
        sql='SELECT * FROM Usuario WHERE Usuario<>?'
        cursor.execute(sql,[Usuario])
        resultado=cursor.fetchall()
        usuarios=[]
        for u in resultado:
            registro={
                    'ID':u[0],
                    'Usuario':u[1],
                    'Contraseña':u[2],
                    'Email':u[3]
                }
            usuarios.append(registro)        
                    
        return usuarios
    except:
        return False   


def adicionar_mensajes(rem,dest,asunto,cuerpo):
    try:
        db=conexion()
        cursor=db.cursor()
        sql='INSERT INTO Correos(Remitente,Destinatario,Asunto,Mensaje) VALUES(?,?,?,?)'
        cursor.execute(sql,[rem,dest,asunto,cuerpo])
        db.commit()
        return True
    except:
        return False

def listar_mensajes(tipo,Usuario):
    try:
        db=conexion()
        cursor=db.cursor()
        if tipo==1:
            sql='SELECT * FROM Correos ORDER BY Fecha DESC'
            cursor.execute(sql)
        else:  
            sql='SELECT * FROM Correos WHERE Remitente=? OR Destinatario=? ORDER BY Fecha DESC'
            cursor.execute(sql,[Usuario,Usuario])
        resultado=cursor.fetchall()
        usuarios=[]
        for u in resultado:
            mensaje='Mensaje Recibido'
            if u[1]==Usuario:
                mensaje='Mensaje Enviado'
            registro={
                    'Id':u[0],
                    'Remitente':u[1],
                    'Destinatario':u[2],
                    'Asunto':u[3],
                    'Mensaje':u[4],
                    'Fecha':u[5],
                    'tipo':mensaje
                }
            usuarios.append(registro)        
                    
        return usuarios
    except:
        return False
    
    
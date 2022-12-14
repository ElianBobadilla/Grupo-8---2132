from email.message import EmailMessage
import smtplib
import email

def Correo(usuario, email_destino, codigo):
    remitente = "equipo_g8@outlook.com"
    destinatario = email_destino
    mensaje = "<p>¡Hola "+usuario + "! Estas a solo un paso de ser parte de Mensajería LBPH. </p>"
    mensaje=mensaje+ "<a href='http://127.0.0.1:5000/validar'>¡Ingresa aquí!</a>"
    mensaje=mensaje+ "<p>Y digita el siguiente código para activar tu cuenta:"+codigo+"</p>"
    email = EmailMessage()
    email["To"] = destinatario
    email["Subject"] = "Codigo de Activacion"
    email.set_content(mensaje, subtype="html")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "centermail8")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()

def RecuperarContraseña(email_destino): 
    remitente = "equipo_g8@outlook.com"
    destinatario = email_destino
    mensaje = "<p>Para restablecer su contraseña ingrese al siguiente enlace:</p>"
    mensaje=mensaje+ "<a href='http://127.0.0.1:5000/nueva-contra""'>Click para restablecer su contraseña</a>"
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Restablecer Contraseña"
    email.set_content(mensaje, subtype="html")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "centermail8")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()
    
def Notificacion(Usuario, email_destino): 
    remitente = "equipo_g8@outlook.com"
    destinatario = email_destino
    mensaje = Usuario + ", te ha enviado un nuevo mensaje"
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "¡Tienes un nuevo mensaje!"
    email.set_content(mensaje)
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "centermail8")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()


   
#!/usr/bin/python3
""" 
Script para enviar un e-mail de registro, o de restauración de contraseña al usuario 
"""
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def sendMail(tipo, destino, data):
    """ 
    tipo: PWD= link to reset a password | REG= Código de registro
    destino = dirección(es) de email (1 string, +1 list)
    data = Dictionary JSON, name, last_name, code
    """
    message = Mail(
        from_email = 'rappilending@gmail.com',
        to_emails = destino
        #subject = 'Registro RappiLending' if (tipo == 'REG') else 'Restaurar contraseña'
    )
    print(data)
    message.dynamic_template_data = {
        'name': data.get('name'),
        'last_name': data.get('last_name'),
        'code': data.get('code')
        }
    message.template_id = 'd-d8285dc4e2a1417890ad340d2575d687'
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
#        print(response.body)
#        print(response.headers)
    except Exception as error:
        print(error)
        

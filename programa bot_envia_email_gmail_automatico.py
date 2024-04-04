#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>Olá, tudo bem? </p>
    <p>Segue o meu e-mail automático para você! </p>
     <p>Assim que possível, eu envio um e-mail, ok! </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Resposta automatica"
    msg['From'] = 'SEU E-MAIL@gmail.com'
    msg['To'] = 'SEU E-MAIL@gmail.com'
    password = 'AQUI VOCÊ GERA A SENHA PELO GMAIL NÃO É A SENHA DA CONTA' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')


# In[ ]:


enviar_email()

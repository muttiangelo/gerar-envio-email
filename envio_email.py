import smtplib 

try:
    msgFrom = str(input("Insira o email de destino: "))
    print("tentando conexao")
    smtpObj = smtplib.SMTP('smtp-mail.outlook.com')
    print("conectado")
    smtpObj.ehlo()
    smtpObj.starttls()
    emailLogin = 'mutti_angelo23@hotmail.com'
    senhaLogin = 'senha'
    print("tentando login")
    smtpObj.login(emailLogin, senhaLogin)
    print("usuario logado")

    msg = """"""
    smtpObj.sendmail("mutti_angelo23@hotmail.com", msgFrom, 'Subject: subject\n{}'.format(msg))
    smtpObj.quit()
    print("email enviado com sucesso")


except:
    print("erro")


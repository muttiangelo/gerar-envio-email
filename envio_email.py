import smtplib 

try:
    msgFrom = str(input())
    print("tentando conexao")
    smtpObj = smtplib.SMTP('smtp.gmail.com')
    print("conectado")
    smtpObj.ehlo()
    smtpObj.starttls()
    emailLogin = 'amutti.dev@gmail.com'
    senhaLogin = ''
    print("tentando login")
    smtpObj.login(emailLogin, senhaLogin)
    print("usuario logado")

    msg = ""
    smtpObj.sendmail("amutti.dev@gmail.com", msgFrom, 'Subject: subject\n{}'.format(msg))
    smtpObj.quit()
    print("email enviado com sucesso")


except:
    print("erro")


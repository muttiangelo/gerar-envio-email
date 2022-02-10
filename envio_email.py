import smtplib 

try:
        
    msgFrom = "sofiapitta3101@gmail.com"
    print("tentando conexao")
    smtpObj = smtplib.SMTP('smtp.gmail.com')
    print("conectado")
    smtpObj.ehlo()
    smtpObj.starttls()
    emailLogin = 'amutti.dev@gmail.com'
    senhaLogin = 'asmtti989'
    print("tentando login")
    smtpObj.login(emailLogin, senhaLogin)
    print("usuario logado")

    msg = "voce eh linda."
    smtpObj.sendmail("amutti.dev@gmail.com", msgFrom, 'Subject: oi linda\n{}'.format(msg))
    smtpObj.quit()
    print("email enviado com sucesso")


except:
    print("erro")


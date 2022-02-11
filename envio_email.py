import email
import smtplib 
import json

class envio_email():
    def __init__(self):
        f = open('parametros.json', 'r')
        dados = json.load(f)
        self.emailDestino =  dados["email_destino"]
        self.email = dados["email"]
        self.senha = dados["senha"]


    def execute(self, listaDados):
        try:
            open("parametros.json")
            msgFrom = self.emailDestino
            print("tentando conexao")
            smtpObj = smtplib.SMTP('smtp-mail.outlook.com')
            print("conectado")
            smtpObj.ehlo()
            smtpObj.starttls()
            emailLogin = self.email
            senhaLogin = self.senha
            print("tentando login")
            smtpObj.login(emailLogin, senhaLogin)
            print("usuario logado")

            msg = """"""
            smtpObj.sendmail("mutti_angelo23@hotmail.com", msgFrom, 'Subject: test\n{}'.format(msg))
            smtpObj.quit()
            print("email enviado com sucesso")


        except:
            print("erro")

if __name__ == "__main__":
    a = envio_email()
    a.execute()

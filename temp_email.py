import requests
# from requests.exceptions import RequestException
from loguru import logger 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
logger.add('log/error.log',level='INFO', rotation='10 MB', format='{time:YYYY-MM-DD HH:mm:ss.SSS} | {message}')

class gmail_send():
    def __init__(self):
        # email.
        self.gmail = ''
        self.gmail_secret = ''
        self.subject = f'.'

    def send_email(self, text):
        sender_email = self.gmail
        receiver_email = 'xiham53960@anwarb.com , dosakapa@altmails.com , jcqdwqoukv@drowblock.com'
        message = MIMEMultipart('alternative')
        message['Subject'] = self.subject
        message['From'] = sender_email
        message['To'] = receiver_email

        try :
            text = str(text)
        except Exception as e:
            logger.error(str(e))
            logger.info('Text of log have something problem base on gmail.')

        plain_text = MIMEText(text, 'plain')
        message.attach(plain_text)

        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.ehlo()
            smtp.login(sender_email, self.gmail_secret)
            smtp.sendmail(sender_email, receiver_email, message.as_string())
        logger.info(f'The daily report have been sent.')

class temp_email:
    def __init__(self) -> None:
        self.key = ''

    def check_domian_email(self):
        url = 'https://api.apilayer.com/temp_mail/domains'

        payload = {}
        headers= {
        'apikey': self.key
        }

        response = requests.request('GET', url, headers=headers, data = payload)

        if response.status_code == 200 :
            return response.json()
        else :
            return None
        
    def hashed_email_address(self):

        url = "https://api.apilayer.com/temp_mail/mail/id/{hashed_email_address}"

        payload = {}
        headers= {
        "apikey": self.key
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        if response.status_code == 200 : 
            return response.json() 
        else :
            return None

    def generate_temp_email(self):
        try:
            url = 'https://api.apilayer.com/temp_mail/atchmnts/id/mail_id'

            payload = {}
            headers= {
            'apikey': self.key
            }

            response = requests.request('GET', url, headers=headers, data = payload)
            
            if response.status_code == 200 :
                return response.json()
            else :
                return None
        except Exception as e:
            print(f'{e}')

if __name__ == '__main__':

    # 生成临时邮件地址
    temp = temp_email()
    print(f'Get list of usable domains : {temp.check_domian_email()}')
    print(f'generate email address : {temp.generate_temp_email()}')

    # 发送邮件
    # g = gmail_send()
    # g.send_email('Hello World.')
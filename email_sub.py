import requests #http requests

from bs4 import BeautifulSoup #web scraping

#Send email
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#system date and time
import datetime

now = datetime.datetime.now()

#email content placeholder

content = ''

#getting Hacker News

def extract_news(url):
    print('Getting your news stories for Hacking...')
    cnt = ''
    cnt += ('<b>Hacker News Top Stories: </b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text + "/n" + '<br>') if tag.text!='More' else '')
    return(cnt)
cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>=====<br>')
content += ('<br><br>Ending here')

#sends email ^^^^

print('Getting your dang email...')

#update email details

SERVER = 'smtp.gmail.com' #"smtp server"
PORT = 587 #your port num
FROM = 'drakejak302@gmail.com' #Your email address
TO = 'danielc6275@gmail.com' #Receiver email
PASS = 'CwagdIh924'





#fp = open(file_name, 'rb')
#Create a message text
# msg = MIMEText('')
msg = MIMEMultipart()

# msg.add_header('Content-Disposition','attatchment',filename='empty.txt')
msg['Subject'] = 'Top NEWS Stories of your DREAMS [Automated Email]' + ' ' + str(now.day) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO

msg.attach(MIMEText(content, 'html'))
#fp.close()

print('Getting the server ya filthy animal...')

server = smtplib.SMTP(SERVER, PORT)
#server = smtplib.SMTP SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
#server.ehlo (for some reason)
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email is sent... keep the change ya filthy animal')

server.quit()


    






























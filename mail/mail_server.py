from flask import Flask, request, jsonify
from flask import render_template
import requests
import json
import smtplib   
from email.mime.multipart import MIMEMultipart #email內容
from email.mime.text import MIMEText #製作文字內文
from email.mime.base import MIMEBase #承載附檔
from email import encoders #附檔編碼

app = Flask(__name__)

#設定使用帳戶
sender = '110356044@g.nccu.edu.tw' 
sender_password = '0829wang'

#設定smtp伺服器
smtpserver = smtplib.SMTP_SSL("smtp.gmail.com",465)
smtpserver.ehlo()
smtpserver.login(sender, sender_password)

@app.route('/')
def login():

    smtpserver.ehlo()
    smtpserver.login(sender, sender_password)

    return jsonify(message = 'mail login')

@app.route('/logout')
def logout():
    smtpserver.quit()

    return jsonify(message = 'mail logout')

@app.route('/confirmMail', methods=['GET', 'POST'])
def confirmMail():
    name = request.args.get('name')
    receiver = request.args.get('email')
    concertID = request.args.get('concertID')
    information ={'concertID': concertID}

    # r = requests.get('http://10.111.111.2:8002/find', params = information)
    artist = 'TTT' # json.loads(r.text).get('artist')
    date = 'ZZZ' # json.loads(r.text).get('date')
    time = 'xxx' # json.loads(r.text).get('time')

    mail = MIMEMultipart()
    mail['From'] = 'Super Star Company'
    mail['To'] = name
    mail['Subject'] = 'Concert Confirmation'

    contents = 'Dear customer,\n\n\
        Thanks for booking concert!\n\
        Here is your order informarion:\n\n\
        Concert: \n\
        Kpop:  ' + artist + '\n\
        Date:  ' + date + '\n\
        Time:  ' + time
    # print(contents)
    mail.attach(MIMEText(contents))
    smtpserver.sendmail(sender, receiver, mail.as_string())
    print('=======================================================')
    
    return jsonify(message = 'OK')

app.run(debug=True, host='127.0.0.1', port=8003)

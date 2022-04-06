from flask import Flask, request, jsonify
from flask import render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    r = requests.get('http://10.111.111.2:8002/')
    return jsonify(message = 'please go to home')

@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/BTS', methods=['GET', 'POST'])
def BTS():
    return render_template('BTS.html')

@app.route('/TWICE', methods=['GET', 'POST'])
def TWICE():
    return render_template('TWICE.html')

@app.route('/BP', methods=['GET', 'POST'])
def BP():
    return render_template('BP.html')

@app.route('/bookTicket', methods=['GET', 'POST'])
def bookTicket():
    if request.method == 'POST':
        # artist = request.form.get('oredr_artist')
        concertID = request.form.get('order_session')
        name = request.form.get('order_name')
        email = request.form.get('order_mail')

        information = {
            'name': name,
            'email': email,
            'concertID': concertID,
        }
        
        r = requests.get('http://10.111.111.2:8002/add', params = information)
        response = json.loads(r.text).get('message')

    if response == 'success':
        # r = requests.get('http://10.111.111.3:8003/confirmMail', params = information)
        return render_template('success.html')
    else:
        return render_template('fail.html')

app.run(debug=True, host='0.0.0.0', port=8001)


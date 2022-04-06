from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from model import db, Order, Concert
from db import db_config

app = Flask(__name__)

app.config.update(db_config)
app.app_context().push()
db.init_app(app)

@app.route('/')
def index():
    db.create_all()

    bts1 = Concert('10109', 'BTS', '01/09', '18:00')
    bts2 = Concert('10110', 'BTS', '01/10', '18:00')
    twice1 = Concert('20111', 'TWICE', '01/11', '19:00')
    twice2 = Concert('20112', 'TWICE', '01/12', '19:00')
    bp1 = Concert('30113', 'BlackPink', '01/13', '18:30')
    bp2 = Concert('30114', 'BlackPink', '01/14', '18:30')
    c = [bts1, bts2, twice1, twice2, bp1, bp2]
    
    db.session.add_all(c)
    db.session.commit()

    return jsonify(message = 'Create!')

@app.route('/add', methods=['GET', 'POST'])
def add():

    if request.method == 'GET':
        name = request.args.get('name')
        email = request.args.get('email')
        concertID = request.args.get('concertID')

        new_order = Order(
            name = name,
            email = email,
            concertID = concertID
        )
        # print('=======================================================')
        db.session.add(new_order)
        db.session.commit()

        return jsonify(message = 'success')
    else:
        print('no data')
        return jsonify(message = 'fail')

@app.route('/find', methods=['GET', 'POST'])
def show():
    if request.method == 'GET':
        concertID = request.args.get('concertID')
        queryID = Concert.query.filter_by(concertID = concertID).first()
        
        info = {
            'artist': queryID.artist,
            'date': queryID.date,
            'time': queryID.time
        }

    return jsonify(info)

app.run(debug=True, host='0.0.0.0', port=8002)

"""
   
"""
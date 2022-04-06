from db import db

class Concert(db.Model):
    __tablename__ = 'Concert'
    id = db.Column(
        db.Integer,
        primary_key=False
    )
    concertID = db.Column(
        db.String(64),
        unique=True,
        nullable=False,
        primary_key=True
    )
    artist = db.Column(
        db.String(64),
        unique=False,
        nullable=False
    )
    date = db.Column(
        db.String(64),
        unique=False,
        nullable=False
    )
    time = db.Column(
        db.String(64),
        unique=False,
        nullable=False
    )

    def __init__(self, concertID, artist, date, time):
        self.concertID = concertID
        self.artist = artist
        self.date = date
        self.time = time

class Order(db.Model):

    __tablename__ = 'Order'

    id = db.Column(
        db.Integer,
        primary_key=True
    )
    name = db.Column(
        db.String(64),
        unique=False,
        nullable=False
    )
    email = db.Column(
        db.String(80),
        unique=False,
        nullable=False
    )
    concertID = db.Column(
        db.String(64),
        unique=False,
        nullable=False
    )

    def __init__(self, name, email, concertID):
        self.name = name
        self.email = email
        self.concertID = concertID
from api_config import db


class Habitacion(db.Model):
    __tablename__ = "habitacion"
    id = db.Column(db.Integer, primary_key=True) #La primary key deberia ser numero y hotel_fk
    numero = db.Column(db.Integer)
    precio = db.Column(db.Integer)
    disponible = db.Column(db.Boolean)
    hotel_fk = db.Column(db.Integer, db.ForeignKey("hotel.id"))
    hotel = db.relationship("Hotel", backref='habitacion_hotel')
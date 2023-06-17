from api_config import db


class Hotel(db.Model):
    __tablename__ = "hotel"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    direccion = db.Column(db.String(100))
    estrellas = db.Column(db.Integer)
    gerente_fk = db.Column(db.Integer, db.ForeignKey("gerente.dni"))
    gerente = db.relationship("Gerente", backref='hotel_gerente')
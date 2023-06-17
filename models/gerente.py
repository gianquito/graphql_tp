from api_config import db


class Gerente(db.Model):
    __tablename__ = "gerente"
    dni = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    last_name = db.Column(db.String(500))
    telefono = db.Column(db.Integer)
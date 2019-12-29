from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class Materia(db.Model):
    __tablename__="materias"
    id = db.Column(db.Integer,primary_key=True)
    Nombre=db.Column(db.String)
    sigla = db.Column(db.String)
    def save(self):
        db.session.add(self)
        db.session.commit()
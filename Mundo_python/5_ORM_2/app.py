
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/javi_cercasi/flask/Flask/Mundo_python/5_ORM_2/orm.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Definimos la tabla de la BD
# Para crear la BD local, hacemos python3, from app import db, 
class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    fundacion = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f'{self.nombre}'   #Para tener una representacion amigable de la BD


class Lenguaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    creador = db.Column(db.String(60))
    #empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id')) # One to many, una empresa tiene muchos programadores
    #empresa = db.Relationship('Empresa', backref=db.backref('programadores', lazy=True)) # Crearia como un campo programadores en Empresa

    def __repr__(self):
        return f'{self.nombre}'


class Programador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    edad = db.Column(db.Integer)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id')) # One to many, una empresa tiene muchos programadores
    empresa = db.relationship('Empresa', backref=db.backref('programadores', lazy=True)) # Crearia como un campo programadores en Empresa

    def __repr__(self):
        return f'{self.nombre}'


# No se pondria
def create():
    db.create_all()
    google = Empresa(nombre="Google",fundacion=1998)
    apple = Empresa(nombre="Apple",fundacion=1975)
    facebook = Empresa(nombre="Facebook",fundacion=2003)
    db.session.add(google)
    db.session.add(apple)
    db.session.add(facebook)
    db.session.commit()
    facebook.fundacion = 2004
    db.session.commit()


if __name__ == "__main__":
    create()
    app.run(debug=True)

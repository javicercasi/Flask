
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/javi_cercasi/flask/Flask/Mundo_python/5_ORM_2/orm.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Para crear una relacion many to many, necesitamos crear una table intermedia:
lenguajes_programador = db.Table('lenguajes_programador',
    db.Column('lenguaje_id',db.Integer, db.ForeignKey('lenguaje.id'), primary_key=True),
    db.Column('programador_id',db.Integer, db.ForeignKey('programador.id'), primary_key=True),
    )



# Definimos la tabla de la BD
# Para crear la BD local, hacemos python3, from app import db, 
class Empresa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    fundacion = db.Column(db.Integer, nullable=True)
    # programadores

    def __repr__(self):
        return f'{self.nombre}'   #Para tener una representacion amigable de la BD


class Lenguaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(60))
    creador = db.Column(db.String(60))
   
    def __repr__(self):
        return f'{self.nombre}'


class Programador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    edad = db.Column(db.Integer)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id')) # One to many, una empresa tiene muchos programadores
    empresa = db.relationship('Empresa', backref=db.backref('programadores', lazy=True)) # Crearia como un campo programadores en Empresa, para tener acceso a la clase Programador desde Empresa.programadores
    lenguajes = db.relationship('Lenguaje', secondary = lenguajes_programador,      # many to many
                                backref=db.backref('programadores', lazy=True))


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

def consultas():
    print(Empresa.query.all()[:3])  # Usamos all o first, para que no nos devuelva el objeto crudo
    Empresa.query.first()
    Empresa.query.filter(Empresa.nombre=='Google').first()
    Empresa.query.filter(Empresa.id==1).first()
    Empresa.query.filter(Empresa.nombre != 'Google').all() # Con palabra exacta
    print("Busqueda aproximada: ", Empresa.query.filter(Empresa.nombre.like ('%goo%')).first())
    Programador.query.filter(Programador.edad >= 25).all()
    print("Que este en la lista :", Programador.query.filter(Programador.nombre.in_(['Jose','Joel','Jaime']))).all()
    Programador.query.filter(~Programador.nombre.in_(['Jose','Joel','Jaime'])).all()   # Muestra todos los datos menos estos
    Programador.query.filter(Programador.edad >= 23, Programador.nombre == 'Jose').first()
    Empresa.query.count()  # Cantidad de entradas en la tabla

if __name__ == "__main__":
    consultas()
    app.run(debug=True)

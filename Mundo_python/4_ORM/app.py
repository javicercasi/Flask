
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/javi_cercasi/flask/Flask/Mundo_python/4_ORM/orm.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Definimos la tabla de la BD
# Para crear la BD local, hacemos python3, from app
class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    pais = db.Column(db.String)

    def __repr__(self):
        return "<Equipo %r>" % self.nombre   #Para tener una representacion amigable de la BD

# No se pondria
def create():
    barcelona = Equipo(nombre="Barca",pais="Esp")
    atletico = Equipo(nombre="Atle",pais="Esp")
    db.session.add(barcelona)
    db.session.add(atletico)
    db.session.commit()
    atletico.nombre = "Atletico"
    atletico.pais = "Mexico"
    db.session.commit()


# No se pondria
def consultas():
    result = Equipo.query.all()  #Consultar todo
    for fila in result:
        print(fila.nombre)  # o fila.pais
    
    barca = Equipo.query.filter_by(nombre="Barca").first()
    print("Consulta Especifica: ", barca.nombre)

    atle = Equipo.query.filter_by(nombre="Atletico").all()  
    for fila in atle:  
        print("Consulta Especifica de mismos nombres: ", fila.nombre)
        # o fila.id

    # Pero se usa mas esta:
    #juv = Equipo.query.filter(Equipo.nombre == "Juventus").first()
    #print("Consulta mas estandar: ",juv.nombre)
    #db.session.delete(juv)
    #db.session.commit()

    # Consulta por distinto:
    result = Equipo.query.filter(Equipo.pais != "Mexico").all()
    print("Equipos no mexicanos:", result)

    # Consulta por varios nombres:
    result = Equipo.query.filter(Equipo.nombre.in_(["Barca", "Atletico"]))
    for fila in result:  
        print("Consulta Especifica de lista: ", fila.nombre)

    # Consulta not in lista:
    result = Equipo.query.filter(~Equipo.nombre.in_(["Barca"]))
    for fila in result:  
        print("Consulta Especifica not in lista: ", fila.nombre)


if __name__ == "__main__":
    #create()
    consultas()
    app.run(debug=True)


import imp
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/javi_cercasi/flask/Flask/Mundo_python/6_Migraciones/migr.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Definimos la tabla de la BD
# Para crear la BD local, hacemos python3, from app import db, 
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))

class post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(20))


if __name__ == '__main__':
    app.run(debug=True)

### Creamos la BD con la tabla usuario y luego queremos aregar solo la tabla post: 
### flask db init, flask db migrate, flask db migrate o downgrade

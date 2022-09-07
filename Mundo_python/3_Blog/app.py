from email.policy import default
import imp
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/javi_cercasi/flask/Flask/Mundo_python/3_Blog/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Definimos la tabla de la BD
# Para crear la BD local, hacemos python3, from app
class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.now)
    texto = db.Column(db.String, nullable=False)


@app.route("/")
def inicio():
	posts = Post.query.order_by(Post.fecha.desc()).all() # select * from posts order by
	return render_template("inicio.html", posts=posts)

@app.route("/agregar")
def agregar():
	return render_template("agregar.html")

@app.route("/crear", methods=["POST"])
def crear_post():
	titulo = request.form.get("titulo")
	texto = request.form.get("texto")
	post = Post(titulo=titulo, texto=texto)
	db.session.add(post)
	db.session.commit()
	return redirect("/")

@app.route("/borrar", methods=["POST"])
def borrar():
	post_id = request.form.get("post_id")
	post = db.session.query(Post).filter(Post.id==post_id).first()
	db.session.delete(post)
	db.session.commit()
	return redirect("/")


def create():
    from app import db
    db.create_all()
    # Terminal: sqlite3 blog.db, .tables, select * from posts

if __name__ == "__main__":
    #create()
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def index():
    nombre = "Javier"
    num = 1
    lista = [1,2,3,4]
    return render_template("index.html", nombre=nombre, num=num, lista=lista)

@app.route("/contacto")
def contacto():
    nombre = "Javier Cercasi"
    num = "261432134"
    return render_template("contacto.html", nombre=nombre, num=num)


@app.route("/hola/<string:nombre>")
def hola(nombre):
    return f"<h1> Hola {nombre} </h1>"

if __name__ == "__main__":
    app.run(debug=True)
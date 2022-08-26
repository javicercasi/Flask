from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index3.html")


@app.route("/contacto", methods=["POST"])
def contacto():
    nombre = request.form.get("name")
    return render_template("contacto2.html", nombre=nombre)


@app.route("/hola/<string:nombre>")
def hola(nombre):
    return f"<h1> Hola {nombre} </h1>"

if __name__ == "__main__":
    app.run(debug=True)
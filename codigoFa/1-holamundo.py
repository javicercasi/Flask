
from flask import Flask

app = Flask(__name__)  #Creo una instancia de flask

@app.route('/')  #Es decorador

def index():
    return ("Hola mundo")

app.run()   #Ejecura el server en el puerto 5000

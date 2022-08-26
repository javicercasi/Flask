from flask import Flask, request

app = Flask(__name__)  #Creo una instancia de flask

@app.route('/')  #Es decorador
def index():
    return ("Hola mundo, carlos")

@app.route('/saluda')  #Es decorador
def saludo():
    return ("Estoy saludando")

@app.route('/params/<name>')  #Es decorador
@app.route('/params/')
@app.route('/params/<name>/<int:num>')  #Es decorador

def params(name = 'Valor default', num=0):
    return 'El parametro es {}, {} '.format(name, num)
   

if __name__ == '__main__':  
    app.run(debug= True, port= 8000)   #Ejecura el server en el puerto 5000

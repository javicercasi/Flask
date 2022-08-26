from flask import Flask, request

app = Flask(__name__)  #Creo una instancia de flask

@app.route('/')  #Es decorador
def index():
    return ("Hola mundo, carlos")

@app.route('/saluda')  #Es decorador
def saludo():
    return ("Estoy saludando")

@app.route('/params')  #Es decorador
def params():
    param = request.args.get('params1', 'no contiene este parametro') # Si no encuentra ese parametro, hace ruta por default
    param2 = request.args.get('params2', 'no contiene un parametro 2') # Si no encuentra ese parametro, hace ruta por default

    return 'El parametro es {}, {}'.format(param, param2)
    # http://localhost:8000/params  > El parametro es no contiene este parametro
    # http://localhost:8000/params?params1=Javi_cercasi  > El parametro es Javi_cercasi
    # http://localhost:8000/params?params1=Javi_cercasi&params2=ITC  > El parametro es Javi_cercasi, ITC

if __name__ == '__main__':  
    app.run(debug= True, port= 8000)   #Ejecura el server en el puerto 5000

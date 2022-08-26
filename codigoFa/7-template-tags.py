from flask import Flask, request, render_template

app = Flask(__name__)  #Creo una instancia de flask

@app.route('/user/<name>')  #Es decorador
def index(name= 'Default'):
    my_list = [1, 2, 3, 4]
    age = 19
    return render_template('user.html', nombre=name, lista=my_list, age=age)


if __name__ == '__main__':  
    app.run(debug= True, port= 8000)   #Ejecura el server en el puerto 5000

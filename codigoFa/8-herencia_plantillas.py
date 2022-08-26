from flask import Flask, request, render_template

app = Flask(__name__)  #Creo una instancia de flask

@app.route('/')  #Es decorador
def index():
    name = 'Eduardo'
    return render_template('index.html', name=name)

@app.route('/client')  #Es decorador
def client():
    listname = ['test1', 'test2', 'test3']
    return render_template('client.html', lista=listname)




if __name__ == '__main__':  
    app.run(debug= True, port= 8000)   #Ejecura el server en el puerto 5000

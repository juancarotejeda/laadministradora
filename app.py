from datetime import datetime
from flask import Flask,render_template,request,redirect,url_for,session
import bbdd
import funciones
app = Flask(__name__)
# rutas
app.secret_key='mysecret_key'


parada=[]
@app.route("/")
def login():
    n_paradas=[] 
    titulo='login'   
    query="SELECT nombre FROM tabla_index" 
    n_paradax=bbdd.consultar_db(query)
    for paradax in n_paradax:
          n_paradas+=paradax                    
    return render_template('login.html',n_paradas=n_paradas,titulo=titulo)

# ruta para nosotros
@app.route('/nosotros')
def nosotros():
    titulo = "nosotros"
    return render_template('nosotros.html', titulo=titulo)

# bloque de prueba
if __name__ == "__main__":
    app.run(debug=True)
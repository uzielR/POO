from flask import Flask, render_template, request
from flask_mysqldb import MySQL

#inicializacion del APP
app = Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='bdflask'
mysql = MySQL(app)

#declaracion de las rutas

#declaracion de la ruta al local host
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST': 
        titulo=request.form['txtTitulo']
        artista=request.form['txtArtista']
        anio=request.form['txtAnio']
        print(titulo, artista, anio)

    return 'los datos llegaron'

@app.route('/eliminar')
def eliminar():
    return "se elimino en la BD"
  
#ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=5000,debug=True)

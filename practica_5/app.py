from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#inicializacion del APP
app = Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='bdflask'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

#declaracion de las rutas

#declaracion de la ruta al local host
@app.route('/')
def index():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM album')
    conAlbum = CC.fetchall() 
    print (conAlbum)
    return render_template('index.html', Listalbum=conAlbum)

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST': 
        titulo=request.form['txtTitulo']
        artista=request.form['txtArtista']
        anio=request.form['txtAnio']
        print(titulo, artista, anio)

        #conectar a la bd
        CS = mysql.connection.cursor()
        
        CS.execute('INSERT INTO albums (titulo, artista, anio) VALUES (%s, %s, %s)', (titulo, artista, anio))

        mysql.connection.commit()
    
    flash('el album fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    return "se elimino en la BD"
  
#ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=5000,debug=True)

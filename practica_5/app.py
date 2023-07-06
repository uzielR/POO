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
        CS.execute('INSERT INTO album (titulo, artista, anio) VALUES (%s, %s, %s)', (titulo, artista, anio))

        mysql.connection.commit()
    
    flash('el album fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar(id):

    return "se elimino en la BD"
  
@app.route('/editar/<string:id>')
def editar(id):
    cursorID=mysql.connection.cursor()
    cursorID.execute('select * from album where id = %s',(id,))
    cunsultaID= cursorID.fetchone()

    return render_template('editarAlbum.html',album=cunsultaID)

@app.route('/actualizar/<id>',methods=['POST'])
def eactualizar(id):

    if request.method == 'POST':
       varTitulo = request.form ['txtTitulo']
       varArtista= request.form ['txtArtista']
       varAnio = request.form ['txtAnio']

       cursorAct=mysql.connection.cursor()
       cursorAct.execute('update album set titulo= %s, artista= %s, anio= %s where id = %s', (varTitulo,varArtista,varAnio,id))
       mysql.connection.commit()
    
    flash('Se actualizo el album'+varTitulo)
    return redirect(url_for('index'))


#ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=5000,debug=True)

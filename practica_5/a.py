from flask import Flask
from flask_mysqldb import MySQL

#inicializacion del APP
app = Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='bdflask'
mysql = MySQL(app)

#declaracion de la ruta al local host
@app.route('/')
def index():
    return "hola mundo Flask"

@app.route('/GUARDAR')
def GUARDAR():
    return "se guardo en la BD"

@app.route('/eliminar')
def eliminar():
    return "se elimino en la BD"
  
#ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=5000,debug=True)

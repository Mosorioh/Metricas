from flask import Flask, request
from flask import render_template
# BD
import time
import datetime 
from datetime import date
from datetime import datetime
import pymysql
from flask_cors import CORS

app=Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return 'Api rest Covid-19'

@app.route('/Registro', methods=['POST'])
def Registro():
    if request.method == 'POST':
        Pais = request.form['Pais']
        Region = request.form['Provincia']
        City = request.form['Ciudad']
        Sector = request.form['Sector']
        TotalPersonas = request.form['TotalPersonas']
        TotalSalidas = request.form['TotalSalidas']
        intervaloSalida = request.form['IntervaloSalida']
        fechapeticion = date.today()
        now = datetime.now()
        timeget = now.time()
        print ("//////////////////////////////////////////////////")
        print (fechapeticion)
        print (now)
        print(timeget)
        print (Pais)
        print (Region)
        print (City)
        print (Sector)
        print (TotalPersonas)
        print (TotalSalidas)
        print (intervaloSalida)
        # IP del Servidor
        # user_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        #Ip client
        user_ip = request.environ["REMOTE_ADDR"]

        #x = Pais + Region + City +Sector + TotalPersonas + TotalSalidas + intervaloSalida 
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='COVID19',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
    # Create a new record
                            
            sql = "INSERT INTO `Data` (`Id_Pais`, `Id_Region`, `Id_City`, `Id_Sector`, `Total_Personas_Casa`, `Total_personas_Salida`, `Time_Aprox_Salida`, `IP`, `Date`, `Hora`) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (Pais, Region, City, Sector, TotalPersonas, TotalSalidas, intervaloSalida, user_ip, fechapeticion, timeget))
            
    # connection is not autocommit by default. So you must commit to save
    # your changes.
            connection.commit()

    finally:
        connection.close()
    return render_template('Validar-Registro.html')

if __name__ == '__main__':
    #app.run( )
    app.run(host='192.168.100.233', port=5050, debug=True)
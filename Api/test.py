from flask import Flask, request
from flask import render_template
from flask import jsonify
# BD
import time
import datetime 
from datetime import date
from datetime import datetime
import pymysql
from flask_cors import CORS

app=Flask(__name__,template_folder='templates')
cors = CORS(app)

@app.route('/')
def home():
    return 'Api rest Covid-19'
#//////////////////////////////////////////

@app.route('/pais')
def select():
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='COVID19',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `Id`, `Name_Pais` FROM `Pais`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            """
            #///////////////////////////////
            sql2 = "SELECT COUNT(Genero) AS Male FROM `json_metrics` WHERE `Id_Genero`=%s"
            cursor.execute(sql2, ('1'))
            resultMale = cursor.fetchall()
            print(resultMale)
            #///////////////////////////////
            sql3 = "SELECT COUNT(Id_Genero) AS Female FROM `json_metrics` WHERE `Id_Genero`=%s"
            cursor.execute(sql3, ('2'))
            resultFemale = cursor.fetchall()
            print(resultFemale)
            """
        return jsonify(result)
    finally:
        connection.close()

#/////////////////////////////////////////////

@app.route('/provincia/<idPais>')
def Provincia(idPais):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='COVID19',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Provincia` WHERE `Id_Pais`=%s"
            cursor.execute(sql, (idPais))
            result = cursor.fetchall()
            print(result)
            """
            #///////////////////////////////
            sql2 = "SELECT COUNT(Genero) AS Male FROM `json_metrics` WHERE `Id_Genero`=%s"
            cursor.execute(sql2, ('1'))
            resultMale = cursor.fetchall()
            print(resultMale)
            #///////////////////////////////
            sql3 = "SELECT COUNT(Id_Genero) AS Female FROM `json_metrics` WHERE `Id_Genero`=%s"
            cursor.execute(sql3, ('2'))
            resultFemale = cursor.fetchall()
            print(resultFemale)
            """
        return jsonify(result)
    finally:
        connection.close()

#/////////////////////////////////////////////

@app.route('/City/<idCity>')
def City(idCity):
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='COVID19',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `City` WHERE `Id_Provincia`=%s"
            cursor.execute(sql, (idCity))
            result = cursor.fetchall()
            print(result)
            """
            #///////////////////////////////
            sql2 = "SELECT COUNT(Genero) AS Male FROM `json_metrics` WHERE `Id_Genero`=%s"
            cursor.execute(sql2, ('1'))
            resultMale = cursor.fetchall()
            print(resultMale)
            #///////////////////////////////
            sql3 = "SELECT COUNT(Id_Genero) AS Female FROM `json_metrics` WHERE `Id_Genero`=%s"
            cursor.execute(sql3, ('2'))
            resultFemale = cursor.fetchall()
            print(resultFemale)
            """
        return jsonify(result)
    finally:
        connection.close()


#////////////////////////////////////////

@app.route('/Registro', methods=['POST'])
def Registro():
    if request.method == 'POST':
        Pais = request.form['Pais']
        Region = request.form['Provincia']
        City = request.form['Ciudad']
        IdSector = request.form['Sector']
        TotalPersonas = request.form['TotalPersonas']
        TotalSalidas = request.form['TotalSalidas']
        intervaloSalida = request.form['IntervaloSalida']
        Ultimas48 = request.form['Ultimas48']
        fechapeticion = date.today()
        now = datetime.now()
        timeget = now.time()
        IdSectorIn = int(IdSector)
        # Determinar el Nombre del Sector
        if IdSectorIn == 1:
            Sectorname = "Norte"
        elif IdSectorIn == 2:
            Sectorname = "Centro"
        else:
            Sectorname = "Sur"
        # determinar las Personas_Riesgo
        PersonasRiesgo = int(TotalPersonas) - int(TotalSalidas)
        # IP
        user_ip = request.environ["REMOTE_ADDR"]
        #//////////////////////////////////////////////////
        #  Print Result
        #/////////////////////////////////////////////////
        print ("//////////////////////////////////////////////////")
        print (fechapeticion)
        print (now)
        print(timeget)
        print (Pais)
        print (Region)
        print (City)
        print (IdSector)
        print ("Id Sector", IdSectorIn)
        print (Sectorname)
        print (TotalPersonas)
        print (TotalSalidas)
        print (PersonasRiesgo)
        print (intervaloSalida)
        print (Ultimas48)
        print (user_ip)
        # IP del Servidor
        # user_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        #Ip client
        #user_ip = request.environ["REMOTE_ADDR"]
        #input()
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
                            
            sql = "INSERT INTO `Data` (`DatePeticion`, `Hora`, `Id_Pais`, `Id_Region`, `Id_City`, `Id_Sector`, `Sector`, `Total_Personas_Casa`, `Total_personas_Salida`, `Personas_Riesgo`, `Time_Aprox_Salida`, `Last48`, `IP`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (fechapeticion, timeget, Pais, Region, City, IdSector, Sectorname, TotalPersonas, TotalSalidas, PersonasRiesgo, intervaloSalida, Ultimas48, user_ip))
            
    # connection is not autocommit by default. So you must commit to save
    # your changes.
            connection.commit()

    finally:
        connection.close()
    return render_template('Validar-Registro.html')

if __name__ == '__main__':
    #app.run( )
    app.run(host='192.168.100.233', port=5050, debug=True)
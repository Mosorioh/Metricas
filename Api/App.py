from flask import Flask, request
from flask import render_template
from flask import jsonify
import uuid 
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
# Api Pais
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
            sql = "SELECT `Id`, `Name_Pais` FROM `Pais` WHERE `IsActive`=%s ORDER BY `Name_Pais`"
            cursor.execute(sql, 1)
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()

#//////////////////////////////////////////
# Api provincia idPais
#//////////////////////////////////////////

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
            sql = "SELECT * FROM `Provincia` WHERE `Id_Pais` = %s AND `IsActive`=%s ORDER BY `Name_provincia`"
            params = [idPais, 1]
            cursor.execute(sql, params)
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()

#//////////////////////////////////////////
# Api Ciudad idProvincia
#//////////////////////////////////////////

@app.route('/City/<idProvincia>')
def City(idProvincia):
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
            sql = "SELECT * FROM `City` WHERE `Id_Provincia`=%s AND `IsActive`=%s"
            cursor.execute(sql, (idProvincia, 1))
            result = cursor.fetchall()
            print(result)

        return jsonify(result)
    finally:
        connection.close()


#//////////////////////////////////////////
# Api Sector idcity
#//////////////////////////////////////////

@app.route('/Sector/<idcity>')
def Sector(idcity):
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
            sql = "SELECT * FROM `Sector` WHERE `Id_City`=%s"
            cursor.execute(sql, (idcity))
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


#//////////////////////////////////////////
# Api Ubicaciom idcity
#//////////////////////////////////////////

@app.route('/Ubicacion/<idsector>')
def Ubicacion(idsector):
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
            sql = "SELECT * FROM `Ubicacion` WHERE `Id_Sector`=%s"
            cursor.execute(sql, (idsector))
            result = cursor.fetchall()
            print(result)
 
        return jsonify(result)
    finally:
        connection.close()

#//////////////////////////////////////////
# Metodo Post
#//////////////////////////////////////////

@app.route('/Registro', methods=['POST'])
def Registro():
    if request.method == 'POST':
        Pais = request.form['Pais']
        Region = request.form['Provincia']
        City = request.form['Ciudad']
        IdSector = request.form['Sector']
        IdUbicacion = request.form['Ubicacion']
        TotalPersonas = request.form['TotalPersonas']
        TotalSalidas = request.form['TotalSalidas']
        intervaloSalida = request.form['IntervaloSalida']
        Ultimas48 = request.form['Ultimas48']
        MotivoSalida = request.form['MotivoSalida']
        Visitasrecibidas = request.form['visitas']
        fechapeticion = date.today()
        now = datetime.now()
        timeget = now.time()
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
        print (IdUbicacion)
        print (TotalPersonas)
        print (TotalSalidas)
        print (PersonasRiesgo)
        print (intervaloSalida)
        print (Ultimas48)
        print (MotivoSalida)
        print (Visitasrecibidas)
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
                            
            sql = "INSERT INTO `Data` (`DatePeticion`, `Hora`, `Id_Pais`, `Id_Region`, `Id_City`, `Id_Sector`, `Total_Personas_Casa`, `Total_personas_Salida`, `Personas_Riesgo`, `Time_Aprox_Salida`, `Last48`, `IP`, `VisitasRecibidas`, `MotivoSalida`, Id_ubicacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (fechapeticion, timeget, Pais, Region, City, IdSector, TotalPersonas, TotalSalidas, PersonasRiesgo, intervaloSalida, Ultimas48, user_ip, Visitasrecibidas, MotivoSalida, IdUbicacion))
            
    # connection is not autocommit by default. So you must commit to save
    # your changes.
            connection.commit()

    finally:
        connection.close()
    return render_template('Validar-Registro.html')


#//////////////////////////////////////////
# Metodo Post
#//////////////////////////////////////////

@app.route('/UbicacionAdd', methods=['POST'])
def addUbicacion():
    if request.method == 'POST':
        Pais = request.form['Pais']
        Region = request.form['Provincia']
        City = request.form['Ciudad']
        IdSector = request.form['Sector']
        CodigoName = request.form['CodigoName']
        Email = request.form['Email']
        #///////////////////////////////////////////
        # Generamos Un GUID para Identificar la prueba
        #///////////////////////////////////////////
        #IdUnico = uuid.uuid4() #32 caracteres
        IdUnico = uuid.uuid4()
        # Convertimos el GUID obtenido con "uuid.uuid4", en una cadena para poder guardar en la DB
        # la Variable "GuidTest" define el Id de la Prueba Actual, a demas este valor es constante durante toda la prueba.
        GuidTest = str(IdUnico)[0:8] 
        Guid = Pais + Region + City + IdSector + "-" + GuidTest
        

        #//////////////////////////////////////////////////
        #  Print Result
        #/////////////////////////////////////////////////
        print ("//////////////////////////////////////////////////")

        print (Pais)
        print (Region)
        print (City)
        print (IdSector)
        print (CodigoName)
        print (Email)
        print (GuidTest)
        print (Guid)
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
                            
            sql = "INSERT INTO `Ubicacion` (`Id_Pais`, `Id_Region`, `Id_City`, `Id_Sector`, `Des_Codigo`, `Email`, `Guid`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (Pais, Region, City, IdSector, CodigoName, Email, Guid))
            
    # connection is not autocommit by default. So you must commit to save
    # your changes.
            connection.commit()

    finally:
        connection.close()
    return render_template('Validar-Registro.html')



#//////////////////////////////////////////
# Chart -
#//////////////////////////////////////////
@app.route('/test/idpais')
def test():
    # Connect to the database
    connection = pymysql.connect(host='192.168.100.51',
                                user='Qatest',
                                password='Quito.2019',
                                db='COVID19',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:

            #///////////////////////////////
            
            #sql2 = "SELECT Id AS Month, `Total_Personas_Casa` As Sales_Figure, `Total_personas_Salida` AS Perc, Time_Aprox_Salida AS TimeSalida FROM `Data`"
            sql2 = "SELECT Id AS Month, `Total_Personas_Casa` As Sales_Figure, `Total_personas_Salida` AS Perc, Time_Aprox_Salida AS TimeSalida FROM `Data`"
            cursor.execute(sql2)
            resultMensajes_Actual = cursor.fetchall()
            Mensajes_Actual = resultMensajes_Actual
            print("Mensaje: ", Mensajes_Actual)
            #print(resultMale)
            
            #///////////////////////////////
         

        return jsonify(Mensajes_Actual)

    finally:
        connection.close()

#//////////////////////////////////////////
# Chart - Pie
#//////////////////////////////////////////
@app.route('/PieChart')
def PieChart():
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
        
            #///////////////////////////////
            #sql2 = "SELECT COUNT(Total_Personas_Casa) AS Male FROM `Data` WHERE `Id_Genero`=%s"
            sql2 = "SELECT SUM(Total_Personas_Casa) AS Male FROM `Data`"
            cursor.execute(sql2)
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)
            #print(resultMale)
            #///////////////////////////////
            #sql3 = "SELECT COUNT(Id_Genero) AS Female FROM `json_metrics` WHERE `Id_Genero`=%s"
            sql3 = "SELECT SUM(Total_personas_Salida) AS Female FROM `Data`"
            cursor.execute(sql3)
            resultFemale = cursor.fetchall()
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)  
            #print(resultFemale)   

        return jsonify({
            "cols": [
                {"id":"","label":"Topping","pattern":"","type":"string"},
                {"id":"","label":"Slices","pattern":"","type":"number"}
                ],
                "rows": [
                {"c":[{"v":"Male1","f":"Personas en Casa"},{"v":male,"f":male}]},
                {"c":[{"v":"Female2","f":"Personas que Salieron"},{"v":Female,"f":Female}]}
                ]
                })
    finally:
        connection.close()

#//////////////////////////////////////////
# Datos Personas Expuestos vs Personas en riesgos
#//////////////////////////////////////////
@app.route('/Expuestos')
def Expuestos():
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
        
            #///////////////////////////////
            #sql2 = "SELECT COUNT(Total_Personas_Casa) AS Male FROM `Data` WHERE `Id_Genero`=%s"
            sql2 = "SELECT SUM(Total_personas_Salida) AS Male FROM `Data`"
            cursor.execute(sql2)
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)
            #print(resultMale)
            #///////////////////////////////
            #sql3 = "SELECT COUNT(Id_Genero) AS Female FROM `json_metrics` WHERE `Id_Genero`=%s"
            sql3 = "SELECT SUM(Personas_Riesgo) AS Female FROM `Data`"
            cursor.execute(sql3)
            resultFemale = cursor.fetchall() 
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)
            total = male + Female  
            #print(resultFemale)   

        """
        return jsonify({"Expuetas": male, "message": "Lista de Personas expuestas"},
                       {"Riesgo": Female, "message": "Lista de Personas en riesgo"},
                       {"Total": total, "message": "Total de Personas en riesgo"})
        """
        return jsonify({"Expuetas": male, "Riesgo": Female,"Total": total, "message": "Lista de Personas expuestas y en riesgo"})
                       

             
    finally:
        connection.close()

#//////////////////////////////////////////
# Datos motivo
#//////////////////////////////////////////
@app.route('/motivo')
def motivo():
    # Connect to the database
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
            Alimento = 1
            Trabajo = 2
            Medicina = 3
            anteriores = 4
            otros = 5
        
            #///////////////////////////////
            
            sql1 = "SELECT COUNT(MotivoSalida) AS Alimento FROM `Data`  WHERE `MotivoSalida`=%s"
            cursor.execute(sql1, (Alimento))
            resultAlimento = cursor.fetchall()
            Alimento = int(resultAlimento[0]['Alimento'])
            print("Alimento: ", Alimento)
            #input()
            
            #///////////////////////////////
                       
            sql2 = "SELECT COUNT(MotivoSalida) AS Trabajo FROM `Data`  WHERE `MotivoSalida`=%s"
            cursor.execute(sql2, (Trabajo))
            resultTrabajo = cursor.fetchall()
            Trabajo = int(resultTrabajo[0]['Trabajo'])
            print("Trabajo: ", Trabajo)
            #input()

            #///////////////////////////////
            
            sql3 = "SELECT COUNT(MotivoSalida) AS Medicina FROM `Data`  WHERE `MotivoSalida`=%s"
            cursor.execute(sql3, (Medicina))
            resultMedicina = cursor.fetchall()
            Medicina = int(resultMedicina[0]['Medicina'])
            print("Medicina: ", Medicina)
            #input()
            
            #///////////////////////////////
                       
            sql4 = "SELECT COUNT(MotivoSalida) AS anteriores FROM `Data`  WHERE `MotivoSalida`=%s"
            cursor.execute(sql4, (anteriores))
            resultanteriores = cursor.fetchall()
            anteriores = int(resultanteriores[0]['anteriores'])
            print("anteriores: ", anteriores)
            #input()

                        #///////////////////////////////
                       
            sql5 = "SELECT COUNT(MotivoSalida) AS otros FROM `Data`  WHERE `MotivoSalida`=%s"
            cursor.execute(sql5, (otros))
            resultotros = cursor.fetchall()
            otros = int(resultotros[0]['otros'])
            print("otros: ", otros)
            #input()


        return jsonify({
            "cols": [
                {"id":"","label":"Topping","pattern":"","type":"string"},
                {"id":"","label":"Slices","pattern":"","type":"number"},
                {"id":"","label":"Topping","pattern":"","type":"string"},
                {"id":"","label":"Topping","pattern":"","type":"string"},
                {"id":"","label":"Slices","pattern":"","type":"number"}
                ],
                "rows": [
                {"c":[{"v":"Male1","f":"Alimento"},{"v":Alimento,"f":Alimento}]},
                {"c":[{"v":"Female2","f":"Trabajo"},{"v":Trabajo,"f":Trabajo}]},
                {"c":[{"v":"Male1","f":"Medicina"},{"v":Medicina,"f":Medicina}]},
                {"c":[{"v":"Female2","f":"Alimento/Trabajo/Medicina"},{"v":anteriores,"f":anteriores}]},
                {"c":[{"v":"Female2","f":"Otros"},{"v":otros,"f":otros}]}
                ]
                })
    finally:
        connection.close()


if __name__ == '__main__':
    #app.run( )
    app.run(host='192.168.100.51', port=5050, debug=True)
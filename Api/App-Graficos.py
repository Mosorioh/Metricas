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
    return 'Api rest Graficos'


#//////////////////////////////////////////
# Chart - Grafico Main Pais 
#//////////////////////////////////////////
@app.route('/Grafico/<idpais>')
def Mainpais(idpais):
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
# Chart - Grafico  Main Provinicia
#//////////////////////////////////////////
@app.route('/Grafico/<idpais>/<idProvinicia>')
def MainProvinicia(idpais, idProvinicia):
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
# Chart - Grafico  Main Ciudad
#//////////////////////////////////////////
@app.route('/Grafico/<idpais>/<idCiudad>')
def MainCiudad(idpais, idProvinicia, idCiudad):
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
# Chart - Grafico Main Sector
#//////////////////////////////////////////
@app.route('/Grafico/<idpais>/<idCiudad>/<idSector>')
def MainSector(idpais, idProvinicia, idCiudad, idSector):
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
# Chart - Grafico Main Ubicacion
#//////////////////////////////////////////
@app.route('/Grafico/<idpais>/<idCiudad>/<idSector>/<idUbicacion>')
def Mainubicacion(idpais, idProvinicia, idCiudad, idSector, idUbicacion):
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

#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#
# Grafico Dos 
# Porcentaje del total de "Personas en Casa" vs "Total de personas Expuestas"
#
#//////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////


#//////////////////////////////////////////
# Chart - Grafico PieChart Pais 
#//////////////////////////////////////////
@app.route('/PieChart/<idpais>')
def PieChartpais(idpais):
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
# Chart - Grafico  PieChart Provinicia
#//////////////////////////////////////////
@app.route('/PieChart/<idpais>/<idProvinicia>')
def PieChartProvinicia(idpais, idProvinicia):
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
# Chart - Grafico  PieChart Ciudad
#//////////////////////////////////////////
@app.route('/PieChart/<idpais>/<idCiudad>')
def PieChartCiudad(idpais, idProvinicia, idCiudad):
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
# Chart - Grafico PieChart Sector
#//////////////////////////////////////////
@app.route('/PieChart/<idpais>/<idCiudad>/<idSector>')
def PieChartSector(idpais, idProvinicia, idCiudad, idSector):
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
# Chart - Grafico PieChart Ubicacion
#//////////////////////////////////////////
@app.route('/PieChart/<idpais>/<idCiudad>/<idSector>/<idUbicacion>')
def PieChartubicacion(idpais, idProvinicia, idCiudad, idSector, idUbicacion):
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

if __name__ == '__main__':
    #app.run( )
    app.run(host='192.168.100.51', port=5060, debug=True)
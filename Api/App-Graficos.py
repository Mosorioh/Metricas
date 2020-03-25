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
# Chart - Grafico Pais
#//////////////////////////////////////////
@app.route('/Grafico/<idpais>')
def pais(idpais, idProvinicia):
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
# Chart - Grafico Provinicia
#//////////////////////////////////////////
@app.route('/Grafico/<idpais>/<idProvinicia>')
def Provinicia(idpais, idProvinicia):
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
# Chart - Grafico Ciudad
#//////////////////////////////////////////
@app.route('/Grafico/<idpais>/<idCiudad>')
def Ciudad(idpais, idProvinicia, idCiudad):
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
# Chart - Grafico Sector
#//////////////////////////////////////////
@app.route('/Grafico/<idpais>/<idCiudad>/<idSector>')
def Sector(idpais, idProvinicia, idCiudad, idSector):
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
# Chart - Grafico Ubicacion
#//////////////////////////////////////////
@app.route('/Grafico/<idpais>/<idCiudad>/<idSector>/<idUbicacion>')
def ubicacion(idpais, idProvinicia, idCiudad, idSector, idUbicacion):
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



if __name__ == '__main__':
    #app.run( )
    app.run(host='192.168.100.51', port=5050, debug=True)
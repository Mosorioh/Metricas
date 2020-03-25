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

#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#
# GRAFICO MAIN
# Chart - Grafico Main Pais 
#
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////

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
            
            sql2 = "SELECT Id AS Month, `Total_Personas_Casa` As Sales_Figure, `Total_personas_Salida` AS Perc, Time_Aprox_Salida AS TimeSalida FROM `Data` WHERE `Id_Pais`=%s"
            cursor.execute(sql2, (idpais))
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
            
            sql2 = "SELECT Id AS Month, `Total_Personas_Casa` As Sales_Figure, `Total_personas_Salida` AS Perc, Time_Aprox_Salida AS TimeSalida FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s"
            cursor.execute(sql2, (idpais, idProvinicia))
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
@app.route('/Grafico/<idpais>/<idProvinicia>/<idCiudad>')
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
            
            sql2 = "SELECT Id AS Month, `Total_Personas_Casa` As Sales_Figure, `Total_personas_Salida` AS Perc, Time_Aprox_Salida AS TimeSalida FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad))
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
@app.route('/Grafico/<idpais>/<idProvinicia>/<idCiudad>/<idSector>')
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
            
            sql2 = "SELECT Id AS Month, `Total_Personas_Casa` As Sales_Figure, `Total_personas_Salida` AS Perc, Time_Aprox_Salida AS TimeSalida FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad, idSector))
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
@app.route('/Grafico/<idpais>/<idProvinicia>/<idCiudad>/<idSector>/<idUbicacion>')
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
            
            sql2 = "SELECT Id AS Month, `Total_Personas_Casa` As Sales_Figure, `Total_personas_Salida` AS Perc, Time_Aprox_Salida AS TimeSalida FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `Id_ubicacion`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad, idSector, idUbicacion))
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

            sql2 = "SELECT SUM(Total_Personas_Casa) AS Male FROM `Data` WHERE `Id_Pais`=%s"
            cursor.execute(sql2, (idpais))
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)

            #///////////////////////////////

            sql3 = "SELECT SUM(Total_personas_Salida) AS Female FROM `Data` WHERE `Id_Pais`=%s"
            cursor.execute(sql3, (idpais))
            resultFemale = cursor.fetchall()
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)  


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

            sql2 = "SELECT SUM(Total_Personas_Casa) AS Male FROM `Data` WHERE `Id_Pais`=%s  AND `Id_Region`=%s"
            cursor.execute(sql2, (idpais, idProvinicia))
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)

            #///////////////////////////////

            sql3 = "SELECT SUM(Total_personas_Salida) AS Female FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s"
            cursor.execute(sql3, (idpais, idProvinicia))
            resultFemale = cursor.fetchall()
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)    

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
@app.route('/PieChart/<idpais>/<idProvinicia>/<idCiudad>')
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

            sql2 = "SELECT SUM(Total_Personas_Casa) AS Male FROM `Data` WHERE `Id_Pais`=%s  AND `Id_Region`=%s AND `Id_City`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad))
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)

            #///////////////////////////////

            sql3 = "SELECT SUM(Total_personas_Salida) AS Female FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s"
            cursor.execute(sql3, (idpais, idProvinicia, idCiudad))
            resultFemale = cursor.fetchall()
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)   

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
@app.route('/PieChart/<idpais>/<idProvinicia>/<idCiudad>/<idSector>')
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

            sql2 = "SELECT SUM(Total_Personas_Casa) AS Male FROM `Data` WHERE `Id_Pais`=%s  AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad, idSector))
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)

            #///////////////////////////////

            sql3 = "SELECT SUM(Total_personas_Salida) AS Female FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s"
            cursor.execute(sql3, (idpais, idProvinicia, idCiudad, idSector))
            resultFemale = cursor.fetchall()
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)     

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
@app.route('/PieChart/<idpais>/<idProvinicia>/<idCiudad>/<idSector>/<idUbicacion>')
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

            sql2 = "SELECT SUM(Total_Personas_Casa) AS Male FROM `Data` WHERE `Id_Pais`=%s  AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `Id_ubicacion`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad, idSector, idUbicacion))
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)

            #///////////////////////////////

            sql3 = "SELECT SUM(Total_personas_Salida) AS Female FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `Id_ubicacion`=%s"
            cursor.execute(sql3, (idpais, idProvinicia, idCiudad, idSector, idUbicacion))
            resultFemale = cursor.fetchall()
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)       

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

#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#
# Grafico Tres 
# Expuestos
#
#//////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////


#//////////////////////////////////////////
# Chart - Grafico Expuestos Pais 
#//////////////////////////////////////////
@app.route('/Expuestos/<idpais>')
def Expuestostpais(idpais):
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

            sql2 = "SELECT SUM(Total_personas_Salida) AS Male FROM `Data` WHERE `Id_Pais`=%s"
            cursor.execute(sql2, idpais)
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)
            
            #///////////////////////////////
            #sql3 = "SELECT COUNT(Id_Genero) AS Female FROM `json_metrics` WHERE `Id_Genero`=%s"
            sql3 = "SELECT SUM(Total_personas_Salida) AS Female FROM `Data` WHERE `Id_Pais`=%s"
            cursor.execute(sql3, idpais)
            resultFemale = cursor.fetchall() 
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)

            #////////////////////////////////
            total = male + Female  
            

        return jsonify({"Expuetas": male, "Riesgo": Female,"Total": total, "message": "Lista de Personas expuestas y en riesgo"})
                                   
    finally:
        connection.close()

#//////////////////////////////////////////
# Chart - Grafico  Expuestos Provinicia
#//////////////////////////////////////////
@app.route('/Expuestos/<idpais>/<idProvinicia>')
def ExpuestosProvinicia(idpais, idProvinicia):
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
            sql2 = "SELECT SUM(Total_personas_Salida) AS Male FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s"
            cursor.execute(sql2, (idpais, idProvinicia))
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)
            #print(resultMale)
            #///////////////////////////////
            #sql3 = "SELECT COUNT(Id_Genero) AS Female FROM `json_metrics` WHERE `Id_Genero`=%s"
            sql3 = "SELECT SUM(Total_personas_Salida) AS Female FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s"
            cursor.execute(sql3, (idpais, idProvinicia))
            resultFemale = cursor.fetchall() 
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)
            total = male + Female  
            #print(resultFemale)   

        return jsonify({"Expuetas": male, "Riesgo": Female,"Total": total, "message": "Lista de Personas expuestas y en riesgo"})
                                   
    finally:
        connection.close()


#//////////////////////////////////////////
# Chart - Grafico  Expuestos Ciudad
#//////////////////////////////////////////
@app.route('/Expuestos/<idpais>/<idProvinicia>/<idCiudad>')
def ExpuestosCiudad(idpais, idProvinicia, idCiudad):
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
            sql2 = "SELECT SUM(Total_personas_Salida) AS Male FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad))
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)
            #print(resultMale)
            #///////////////////////////////
            #sql3 = "SELECT COUNT(Id_Genero) AS Female FROM `json_metrics` WHERE `Id_Genero`=%s"
            sql3 = "SELECT SUM(Total_personas_Salida) AS Female FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s"
            cursor.execute(sql3, (idpais, idProvinicia, idCiudad))
            resultFemale = cursor.fetchall() 
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)
            total = male + Female  
            #print(resultFemale)   

        return jsonify({"Expuetas": male, "Riesgo": Female,"Total": total, "message": "Lista de Personas expuestas y en riesgo"})
                                   
    finally:
        connection.close()

#//////////////////////////////////////////
# Chart - Grafico Expuestos Sector
#//////////////////////////////////////////
@app.route('/Expuestos/<idpais>/<idProvinicia>/<idCiudad>/<idSector>')
def ExpuestosSector(idpais, idProvinicia, idCiudad, idSector):
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
            sql2 = "SELECT SUM(Total_personas_Salida) AS Male FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad, idSector))
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)
            #print(resultMale)
            #///////////////////////////////
            #sql3 = "SELECT COUNT(Id_Genero) AS Female FROM `json_metrics` WHERE `Id_Genero`=%s"
            sql3 = "SELECT SUM(Total_personas_Salida) AS Female FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s"
            cursor.execute(sql3, (idpais, idProvinicia, idCiudad, idSector))
            resultFemale = cursor.fetchall() 
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)
            total = male + Female  
            #print(resultFemale)   

        return jsonify({"Expuetas": male, "Riesgo": Female,"Total": total, "message": "Lista de Personas expuestas y en riesgo"})
                                   
    finally:
        connection.close()


#//////////////////////////////////////////
# Chart - Grafico Expuestos Ubicacion
#//////////////////////////////////////////
@app.route('/Expuestos/<idpais>/<idProvinicia>/<idCiudad>/<idSector>/<idUbicacion>')
def Expuestosubicacion(idpais, idProvinicia, idCiudad, idSector, idUbicacion):
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
            sql2 = "SELECT SUM(Total_personas_Salida) AS Male FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `Id_ubicacion`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad,idSector, idUbicacion))
            resultMale = cursor.fetchall()
            male = int(resultMale[0]['Male'])
            print("Male: ", male)
            #print(resultMale)
            #///////////////////////////////
            #sql3 = "SELECT COUNT(Id_Genero) AS Female FROM `json_metrics` WHERE `Id_Genero`=%s"
            sql3 = "SELECT SUM(Total_personas_Salida) AS Female FROM `Data` WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `Id_ubicacion`=%s"
            cursor.execute(sql3, (idpais, idProvinicia, idCiudad,idSector, idUbicacion))
            resultFemale = cursor.fetchall() 
            Female = int(resultFemale[0]['Female'])
            print("Female: ", Female)
            total = male + Female  
            #print(resultFemale)   

        return jsonify({"Expuetas": male, "Riesgo": Female,"Total": total, "message": "Lista de Personas expuestas y en riesgo"})
                                   
    finally:
        connection.close()


#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#
# Grafico Cuatro  
# Motivo
#
#//////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////


#//////////////////////////////////////////
# Chart - Grafico motivo Pais 
#//////////////////////////////////////////
@app.route('/motivo/<idpais>')

def motivopais(idpais):
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
            
            sql1 = "SELECT COUNT(MotivoSalida) AS Alimento FROM `Data`  WHERE `Id_Pais`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql1, (idpais, Alimento))
            resultAlimento = cursor.fetchall()
            Alimento = int(resultAlimento[0]['Alimento'])
            print("Alimento: ", Alimento)
            #input()
            
            #///////////////////////////////
                       
            sql2 = "SELECT COUNT(MotivoSalida) AS Trabajo FROM `Data`  WHERE `Id_Pais`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql2, (idpais, Trabajo))
            resultTrabajo = cursor.fetchall()
            Trabajo = int(resultTrabajo[0]['Trabajo'])
            print("Trabajo: ", Trabajo)
            #input()

            #///////////////////////////////
            
            sql3 = "SELECT COUNT(MotivoSalida) AS Medicina FROM `Data`  WHERE `Id_Pais`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql3, (idpais, Medicina))
            resultMedicina = cursor.fetchall()
            Medicina = int(resultMedicina[0]['Medicina'])
            print("Medicina: ", Medicina)
            #input()
            
            #///////////////////////////////
                       
            sql4 = "SELECT COUNT(MotivoSalida) AS anteriores FROM `Data`  WHERE `Id_Pais`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql4, (idpais, anteriores))
            resultanteriores = cursor.fetchall()
            anteriores = int(resultanteriores[0]['anteriores'])
            print("anteriores: ", anteriores)
            #input()

            #///////////////////////////////
                       
            sql5 = "SELECT COUNT(MotivoSalida) AS otros FROM `Data`  WHERE `Id_Pais`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql5, (idpais, otros))
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

#//////////////////////////////////////////
# Chart - Grafico  motivo Provinicia
#//////////////////////////////////////////
@app.route('/motivo/<idpais>/<idProvinicia>')
def motivoProvinicia(idpais, idProvinicia):
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
            
            sql1 = "SELECT COUNT(MotivoSalida) AS Alimento FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql1, (idpais, idProvinicia, Alimento))
            resultAlimento = cursor.fetchall()
            Alimento = int(resultAlimento[0]['Alimento'])
            print("Alimento: ", Alimento)
            #input()
            
            #///////////////////////////////
                       
            sql2 = "SELECT COUNT(MotivoSalida) AS Trabajo FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, Trabajo))
            resultTrabajo = cursor.fetchall()
            Trabajo = int(resultTrabajo[0]['Trabajo'])
            print("Trabajo: ", Trabajo)
            #input()

            #///////////////////////////////
            
            sql3 = "SELECT COUNT(MotivoSalida) AS Medicina FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql3, (idpais, idProvinicia, Medicina))
            resultMedicina = cursor.fetchall()
            Medicina = int(resultMedicina[0]['Medicina'])
            print("Medicina: ", Medicina)
            #input()
            
            #///////////////////////////////
                       
            sql4 = "SELECT COUNT(MotivoSalida) AS anteriores FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql4, (idpais, idProvinicia, anteriores))
            resultanteriores = cursor.fetchall()
            anteriores = int(resultanteriores[0]['anteriores'])
            print("anteriores: ", anteriores)
            #input()

            #///////////////////////////////
                       
            sql5 = "SELECT COUNT(MotivoSalida) AS otros FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql5, (idpais, idProvinicia, otros))
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


#//////////////////////////////////////////
# Chart - Grafico  motivo Ciudad
#//////////////////////////////////////////
@app.route('/motivo/<idpais>/<idProvinicia>/<idCiudad>')
def motivoCiudad(idpais, idProvinicia, idCiudad):
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
            
            sql1 = "SELECT COUNT(MotivoSalida) AS Alimento FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql1, (idpais, idProvinicia, idCiudad, Alimento))
            resultAlimento = cursor.fetchall()
            Alimento = int(resultAlimento[0]['Alimento'])
            print("Alimento: ", Alimento)
            #input()
            
            #///////////////////////////////
                       
            sql2 = "SELECT COUNT(MotivoSalida) AS Trabajo FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad, Alimento))
            resultTrabajo = cursor.fetchall()
            Trabajo = int(resultTrabajo[0]['Trabajo'])
            print("Trabajo: ", Trabajo)
            #input()

            #///////////////////////////////
            
            sql3 = "SELECT COUNT(MotivoSalida) AS Medicina FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql3, (idpais, idProvinicia, idCiudad, Alimento))
            resultMedicina = cursor.fetchall()
            Medicina = int(resultMedicina[0]['Medicina'])
            print("Medicina: ", Medicina)
            #input()
            
            #///////////////////////////////
                       
            sql4 = "SELECT COUNT(MotivoSalida) AS anteriores FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql4, (idpais, idProvinicia, idCiudad, Alimento))
            resultanteriores = cursor.fetchall()
            anteriores = int(resultanteriores[0]['anteriores'])
            print("anteriores: ", anteriores)
            #input()

            #///////////////////////////////
                       
            sql5 = "SELECT COUNT(MotivoSalida) AS otros FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql5, (idpais, idProvinicia, idCiudad, Alimento))
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

#//////////////////////////////////////////
# Chart - Grafico motivo Sector
#//////////////////////////////////////////
@app.route('/motivo/<idpais>/<idProvinicia>/<idCiudad>/<idSector>')
def motivoSector(idpais, idProvinicia, idCiudad, idSector):
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
            
            sql1 = "SELECT COUNT(MotivoSalida) AS Alimento FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql1, (idpais, idProvinicia, idCiudad, idSector, Alimento))
            resultAlimento = cursor.fetchall()
            Alimento = int(resultAlimento[0]['Alimento'])
            print("Alimento: ", Alimento)
            #input()
            
            #///////////////////////////////
                       
            sql2 = "SELECT COUNT(MotivoSalida) AS Trabajo FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad, idSector, Alimento))
            resultTrabajo = cursor.fetchall()
            Trabajo = int(resultTrabajo[0]['Trabajo'])
            print("Trabajo: ", Trabajo)
            #input()

            #///////////////////////////////
            
            sql3 = "SELECT COUNT(MotivoSalida) AS Medicina FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql3, (idpais, idProvinicia, idCiudad, idSector, Alimento))
            resultMedicina = cursor.fetchall()
            Medicina = int(resultMedicina[0]['Medicina'])
            print("Medicina: ", Medicina)
            #input()
            
            #///////////////////////////////
                       
            sql4 = "SELECT COUNT(MotivoSalida) AS anteriores FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql4, (idpais, idProvinicia, idCiudad, idSector, Alimento))
            resultanteriores = cursor.fetchall()
            anteriores = int(resultanteriores[0]['anteriores'])
            print("anteriores: ", anteriores)
            #input()

            #///////////////////////////////
                       
            sql5 = "SELECT COUNT(MotivoSalida) AS otros FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql5, (idpais, idProvinicia, idCiudad, idSector, Alimento))
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


#//////////////////////////////////////////
# Chart - Grafico motivo Ubicacion
#//////////////////////////////////////////
@app.route('/motivo/<idpais>/<idProvinicia>/<idCiudad>/<idSector>/<idUbicacion>')
def motivoubicacion(idpais, idProvinicia, idCiudad, idSector, idUbicacion):
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
            
            sql1 = "SELECT COUNT(MotivoSalida) AS Alimento FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `Id_ubicacion`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql1, (idpais, idProvinicia, idCiudad, idSector, idUbicacion, Alimento))
            resultAlimento = cursor.fetchall()
            Alimento = int(resultAlimento[0]['Alimento'])
            print("Alimento: ", Alimento)
            #input()
            
            #///////////////////////////////
                       
            sql2 = "SELECT COUNT(MotivoSalida) AS Trabajo FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `Id_ubicacion`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql2, (idpais, idProvinicia, idCiudad, idSector, idUbicacion, Alimento))
            resultTrabajo = cursor.fetchall()
            Trabajo = int(resultTrabajo[0]['Trabajo'])
            print("Trabajo: ", Trabajo)
            #input()

            #///////////////////////////////
            
            sql3 = "SELECT COUNT(MotivoSalida) AS Medicina FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `Id_ubicacion`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql3, (idpais, idProvinicia, idCiudad, idSector, idUbicacion, Alimento))
            resultMedicina = cursor.fetchall()
            Medicina = int(resultMedicina[0]['Medicina'])
            print("Medicina: ", Medicina)
            #input()
            
            #///////////////////////////////
                       
            sql4 = "SELECT COUNT(MotivoSalida) AS anteriores FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `Id_ubicacion`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql4, (idpais, idProvinicia, idCiudad, idSector, idUbicacion, Alimento))
            resultanteriores = cursor.fetchall()
            anteriores = int(resultanteriores[0]['anteriores'])
            print("anteriores: ", anteriores)
            #input()

            #///////////////////////////////
                       
            sql5 = "SELECT COUNT(MotivoSalida) AS otros FROM `Data`  WHERE `Id_Pais`=%s AND `Id_Region`=%s AND `Id_City`=%s AND `Id_Sector`=%s AND `Id_ubicacion`=%s AND `MotivoSalida`=%s"
            cursor.execute(sql5, (idpais, idProvinicia, idCiudad, idSector, idUbicacion, Alimento))
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
    app.run(host='192.168.100.51', port=5060, debug=True)
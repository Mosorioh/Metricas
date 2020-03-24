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
# Chart - main Line
#//////////////////////////////////////////
@app.route('/SendDatos')
def SendDatos():
    if request.method == 'POST':
        Pais = request.form['Pais']
        Region = request.form['Provincia']
        City = request.form['Ciudad']
        IdSector = request.form['Sector']
        IdUbicacion = request.form['Ubicacion']

    # ////////////////////////////////
    # Print data

        print ("Pais: ", Pais)
        print ("Region: ", Region)
        print ("City: ", City)
        print ("Sector: ", IdSector)
        print ("IdUbicacion: ", IdUbicacion)

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
    app.run(host='192.168.100.51', port=5060, debug=True)
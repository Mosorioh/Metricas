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
# Api Pais
#//////////////////////////////////////////
@app.route('/test')
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
            #sql2 = "SELECT substring(DatePeticion,1,19) AS Month, `Total_Personas_Casa` As Sales_Figure, `Total_personas_Salida` AS Perc FROM `Data`"
            sql2 = "SELECT Id AS Month, `Total_Personas_Casa` As Sales_Figure, `Total_personas_Salida` AS Perc FROM `Data`"
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
    app.run(host='192.168.100.51', port=5060, debug=True)
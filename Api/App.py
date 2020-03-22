from flask import Flask, request
from flask import render_template

app=Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return 'Api rest Covid-19'

@app.route('/pais')
def select():
    # Connect to the database
    connection = pymysql.connect(host='192.168.2.161',
                                user='Qatest',
                                password='Quito.2019',
                                db='automatizacion',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT COUNT(Genero) AS Total FROM `json_metrics` "
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
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
        return jsonify(
            #show all data
            {"Total Personas": result, "Male": resultMale, "Female": resultFemale},
            {"Message": "Datos Totales por Genero"}
            #show one result of data
            #{"Data": result[0], "message": "datos Web Change"}
            )
    finally:
        connection.close()


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
        print (Pais)
        print (Region)
        print (City)
        #x = Pais + Region + City +Sector + TotalPersonas + TotalSalidas + intervaloSalida 
    return render_template('Validar-Registro.html')

if __name__ == '__main__':
    #app.run( )
    app.run(port=5050, debug=True)
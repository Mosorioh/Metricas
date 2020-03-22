from flask import Flask, request
from flask import render_template

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
        print (Pais)
        print (Region)
        print (City)
        #x = Pais + Region + City +Sector + TotalPersonas + TotalSalidas + intervaloSalida 
    return render_template('Validar-Registro.html')

if __name__ == '__main__':
    #app.run( )
    app.run(port=5050, debug=True)
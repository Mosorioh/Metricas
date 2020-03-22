from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Api rest Covid-19'

@app.route('/Registro', methods=['POST'])
def Registro():
    if request.method == 'POST':
        Pais = request.form['Pais']
        Region = request.form['Provincia']
        City = request.form['Ciudad']
        print (Pais)
        print (Region)
        print (City)
        x = Pais + Region + City
    return x

if __name__ == '__main__':
    #app.run( )
    app.run(port=5050, debug=True)
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Bienvenido a la página de inicio'

@app.route('/aprueba')
def aprueba():
    return 'Esta es la página de prueba'

@app.route('/comprobando')
def comprobando():
    return 'Estás en la página de comprobación'

if __name__ == '__main__':
    # Cambiar el puerto a 5001
    app.run(port=5001, debug=True)

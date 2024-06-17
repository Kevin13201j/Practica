from flask import Flask
#importar
# declara la ubicacion de las carpetas
app = Flask(__name__)
 
@app.route('/aprueba')
def aprueba():
    return 'Esta es la página de prueba'

if __name__ =='__main__':
    app.run()


 

    

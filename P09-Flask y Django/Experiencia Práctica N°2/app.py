from flask import Flask
from flask import render_template

app = Flask(__name__)

data = [
    {
        'element': 'EMPIEZA LA AVENTURA'
    },
    {
        'element': 'INICIAR TEST'
    },
    {
        'element': 'VER'
    },
    {
        'element': 'ENTERATE'
    }
 
]


@app.route('/')
def index():
    return render_template('index.html', titulo="BIENVENIDOS AL MUNDO DE LOS MAGOS")
from flask import Flask, render_template
app = Flask(__name__)
 
data = [
    {
        'element': 'AÑADIR AL CARRITO'
    }, 
]
 
 
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', titulo="IShop")

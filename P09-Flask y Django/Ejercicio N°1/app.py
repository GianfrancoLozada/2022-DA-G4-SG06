from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return "<h1>Bienvenido - SUCRIBETE!</h1>"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True, port = 5000)


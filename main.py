from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_users():
    return '<h1>Merhaba Flask & Docker</h2>'

@app.route('/test')
def test():
    return '<h1>test Flask & Docker app</h2>'



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
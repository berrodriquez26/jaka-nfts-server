from flask import Flask, send_file, jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola Bernardo</p>"

@app.route('/mexico')
def mexico():
    filename = 'mexico.jpeg'
    return send_file(filename, mimetype='image/jpeg')

@app.route('/argentina')
def argentina():
    filename = 'argentina.png'
    return send_file(filename, mimetype='image/png')

@app.route("/mexico-json")
def mexico_json():
    mexico = {
    "name": "Mexico JSON",
    "description": "Testeando con una imagen",
    "image": "https://ipfs.io/ipfs/bafkreihz65lvxubnjpw7t7dzwvijbpwjl6eu2pr2cvdcp7zxhayj6nf5zq"
    }
    return jsonify(mexico)

@app.route("/argentina-json")
def argentina_json():
    mexico = {
    "name": "Argentina JSON",
    "description": "Testeando con una imagen",
    "image": "https://ipfs.io/ipfs/bafkreihz65lvxubnjpw7t7dzwvijbpwjl6eu2pr2cvdcp7zxhayj6nf5zq"
    }
    return jsonify(mexico)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello", 200

@app.route('/error/503', methods=['GET'])
def devuelve_503():
    return "Server error", 503

@app.route('/error/404', methods=['GET'])
def devuelve_404():
    return "Not found", 404

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80)
    app.run()

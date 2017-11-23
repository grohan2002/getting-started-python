import os
from flask import Flask
from flask import Response
from flask import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/cities.json')
def cities():
    data = {"cities" : ["Amsterdam","Berlin","New York","San Francisco","Tokyo","Mumbai"]}
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp

@app.route('/countries.json')
def countries():
    data = {"countries" : ["Netherlands","Germany","USA-East","USA-West","Japan","India"]}
    resp = Response(json.dumps(data), status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

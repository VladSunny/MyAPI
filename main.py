from flask import Flask, request
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/hello/')
def hello_name():
    name = request.args.get('name', 'World')  # Получаем параметр name, значение по умолчанию - 'World'
    return {'message': f'Hello {name}'}

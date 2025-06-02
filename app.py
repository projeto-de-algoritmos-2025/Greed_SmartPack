# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from algoritmo import knapsack_fracionado

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    itens = data['itens']
    peso_max = data['peso_max']
    resultado = knapsack_fracionado(itens, peso_max, volume_max=float('inf'))  # Volume não é mais considerado
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)

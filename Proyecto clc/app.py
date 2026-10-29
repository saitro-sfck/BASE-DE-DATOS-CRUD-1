from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    datos = request.get_json()
    op = datos.get('operacion')
    
    try:
        # Operaciones binarias (dos números)
        if op in ['sumar', 'restar', 'multiplicar', 'dividir', 'potencia']:
            num1 = float(datos.get('num1'))
            num2 = float(datos.get('num2'))

            if op == 'sumar':
                res = num1 + num2
            elif op == 'restar':
                res = num1 - num2
            elif op == 'multiplicar':
                res = num1 * num2
            elif op == 'dividir':
                if num2 == 0:
                    return jsonify({'error': 'No se puede dividir entre cero'}), 400
                res = num1 / num2
            elif op == 'potencia':
                res = num1 ** num2

        # Operaciones unarias (un solo número)
        elif op in ['raiz', 'seno', 'coseno', 'tangente', 'log10', 'ln', 'factorial']:
            num = float(datos.get('num1'))

            if op == 'raiz':
                if num < 0:
                    return jsonify({'error': 'Raíz negativa no permitida'}), 400
                res = math.sqrt(num)
            elif op == 'seno':
                res = math.sin(math.radians(num))
            elif op == 'coseno':
                res = math.cos(math.radians(num))
            elif op == 'tangente':
                # Evitar tangentes indefinidas (90°, 270°, etc.)
                if (num - 90) % 180 == 0:
                    return jsonify({'error': 'Tangente indefinida'}), 400
                res = math.tan(math.radians(num))
            elif op == 'log10':
                if num <= 0:
                    return jsonify({'error': 'Logaritmo solo para x > 0'}), 400
                res = math.log10(num)
            elif op == 'ln':
                if num <= 0:
                    return jsonify({'error': 'Ln solo para x > 0'}), 400
                res = math.log(num)
            elif op == 'factorial':
                if num < 0 or not num.is_integer():
                    return jsonify({'error': 'Factorial solo para enteros ≥ 0'}), 400
                res = math.factorial(int(num))
        else:
            return jsonify({'error': 'Operación no válida'}), 400

        # Redondear ligeramente para evitar residuos de coma flotante como 0.0000000000000001
        if isinstance(res, float):
            res = round(res, 8)
            # Quitar ceros decimales innecesarios si es entero exacto
            if res.is_integer():
                res = int(res)

        return jsonify({'resultado': res})

    except (ValueError, OverflowError):
        return jsonify({'error': 'Error de cálculo o número fuera de rango'}), 400

if __name__ == '__main__':
    app.run(debug=True)
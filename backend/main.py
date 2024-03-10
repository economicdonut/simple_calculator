from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ensures that the input values are valid integers
def validate_input(data):
    a = data.get('a')
    b = data.get('b')  
    try:
        a = int(a)
        b = int(b)
        return a, b
    except (ValueError, TypeError):
        return None, None

# route for addition
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    a, b = validate_input(data)
    if a is None or b is None:
        return jsonify({'error': 'Invalid input. Please provide integer values for a and b.'}), 400
    result = a + b
    return jsonify({'result': result})

# route for subtraction
@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    a, b = validate_input(data)
    if a is None or b is None:
        return jsonify({'error': 'Invalid input. Please provide integer values for a and b.'}), 400
    result = a - b
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

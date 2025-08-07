from flask import Flask, request, jsonify

app = Flask(__name__)

# 1. /hello endpoint
@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, welcome to the RAG 30-day sprint!'})

# 2. /calculate endpoint
@app.route('/calculate', methods=['GET'])
def calculate():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a + b
        return jsonify({'a': a, 'b': b, 'sum': result})
    except (TypeError, ValueError):
        return jsonify({'error': 'Please provide valid numbers using ?a=5&b=10'}), 400

# 3. /ai-ready endpoint
@app.route('/ai-ready', methods=['GET'])
def ai_ready():
    return jsonify({
        'message': 'You are ready to build AI apps. Keep pushing, learn daily, and ship projects!'
    })

if __name__ == '__main__':
    app.run(debug=True)

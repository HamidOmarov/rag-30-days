from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/hello')
def hello():
    # Return a greeting message as JSON
    return jsonify({"message": "Hello, World!"})

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get 'a' and 'b' from request and return their sum as JSON
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    return jsonify({"sum": a + b})

@app.route('/ai-ready')
def ai_ready():
    return jsonify({
        "message": "Day 1 of 30: Learning Python for AI",
        "progress": "3%"
    })

# Run the Flask application
if __name__ == '__main__':  
    app.run(debug=True)     
    
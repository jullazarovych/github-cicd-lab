from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hi, this is GitHub Actions CI/CD.</h1>"

@app.route('/status')
def status():
    return jsonify({"status": "OK", "platform": "GitHub"})

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = a + b
    return jsonify({"operation": "add", "a": a, "b": b, "result": result})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
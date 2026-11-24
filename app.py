from flask import Flask, jsonify

app = Flask(__name__)

visits = 0

@app.route("/")
def home():
    return jsonify(message="DockLab is alive! 🐳")

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/visits")
def count():
    global visits
    visits = visits + 1
    return jsonify(visits=visits)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, jsonify

app = Flask(__name__)

DATA_FILE = "/data/visits.txt"

def read_visits():
    try:
        with open(DATA_FILE) as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def write_visits(n):
    with open(DATA_FILE, "w") as f:
        f.write(str(n))

@app.route("/")
def home():
    return jsonify(message="DockLab is alive! 🐳")

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/visits")
def count():
    n = read_visits() + 1
    write_visits(n)
    return jsonify(visits=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
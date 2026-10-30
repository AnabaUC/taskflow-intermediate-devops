from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn Docker", "completed": False},
    {"id": 2, "title": "Learn Kubernetes", "completed": False},
    {"id": 3, "title": "Build a CI/CD pipeline", "completed": False}
]


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to TaskFlow - Managed with DevOps!",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200


@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
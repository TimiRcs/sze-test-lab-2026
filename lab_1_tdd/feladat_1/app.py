from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

# In-memory data store
todos = [
    {"id": 1, "task": "Learn TDD", "done": False},
    {"id": 2, "task": "Build a Flask API", "done": True},
]
@app.route("/")
def index():
    return "Welcome to the Todo API!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_id = max(todo['id'] for todo in todos) + 1 if todos else 1
    new_todo = {"id": new_id, "task": data['task'], "done": False}
    todos.append(new_todo)
    return jsonify(new_todo), 201
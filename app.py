from flask import Flask, jsonify, request
from database import create_tables
import task_controller
app = Flask(__name__)

@app.route('/task', methods=["GET"])
def get_tasks():
    
    try:
        tasks = task_controller.get_tasks()
        return jsonify({"tarefas": tasks})
    except Exception as e:
        return jsonify({"message": "Erro ao pegar tarefas"}), 400

@app.route("/task", methods=["POST"])
def insert_game():
    try:
        game_details = request.get_json()
        name = game_details.get("name")
        description = game_details.get("description")
        result = task_controller.insert_task(name, description)
        return jsonify({"message": "Tarefa criada com sucesso!"})
    except Exception as e:
        return jsonify({"message": "Erro ao cadastrar tarefa"}), 400
if __name__ == "__main__":
    create_tables()
    app.run(host='0.0.0.0', port=5000, debug=False)
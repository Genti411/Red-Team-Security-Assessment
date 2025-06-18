from flask import Flask, request, jsonify

app = Flask(__name__)
command_queue = []

@app.route('/get', methods=['POST'])
def get_command():
    return jsonify({"cmd": command_queue.pop(0) if command_queue else "noop"})

@app.route('/add', methods=['POST'])
def add_command():
    cmd = request.json.get("cmd")
    command_queue.append(cmd)
    return jsonify({"status": "added"})

if __name__ == "__main__":
    app.run(port=8080)
